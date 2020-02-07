import java.util.HashSet;
public class Collatz {
    static HashSet<Integer> db = new HashSet<Integer>();
    public static void main(String[] args) {
        Stopwatch s = new Stopwatch();
        eval(10);
        HashSet<Integer> db1 = new HashSet<Integer>(db);
        db1.add(1);
        db = new HashSet<Integer>();
        eval(89);

        int N = Integer.parseInt(args[0]);
        int count  = 0;
        for (int i = 1; i < N; i++) {
            int v  = i;
            while (!db.contains(v) && !db1.contains(v))
                v = sumd(v);
            if (!db1.contains(v))
                count += 1;
        }
        StdOut.println(count);
        StdOut.println("Took: " + s.elapsedTime());
    }
    public static int sumd(int N) {
        int sum = 0;
        while (N > 0) {
            int d = N % 10;
            sum += (d * d);
            N /= 10;
        }
        return sum;
    }
    public static int[] comp(int N) {
        int[] a = new int[2];
        int squ = (int) Math.sqrt(N);
        if (squ*squ == N) {
            a[0] = squ;
            a[1] = squ * 10;
            return a;
        }
        for (int sqv = 1; sqv <= N/sqv; sqv++) {
            int u = N - sqv*sqv;
            squ   = (int) Math.sqrt(u);
            if (squ*squ == u) {
                a[0] = sqv*10 + squ;
                a[1] = squ*10 + sqv;
                return a;
            }
        }
        return a;
    }
    public static void eval(int N) {
        db.add(N);
        int[] a = comp(N);
        if (a[0] == 0) {
            db.add(N);
            return;
        }
        else {
            eval(a[0]);
            eval(a[1]);
        }
    }
}
