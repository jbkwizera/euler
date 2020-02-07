public class Reversible {
    public static int reverse(int x) {
        int v = 0;
        while (x > 0) {
            int rem = x % 10;
            v = v * 10 + rem;
            x = x / 10;
        }
        return v;
    }
    public static int odd(int n) {
        if (n == 0) return 0;
        while (n > 0) {
            if (n % 2 == 0) return 0;
            n /= 10;
        }
        return 1;
    }
    public static void main(String[] args) {
        int x = Integer.parseInt(args[0]);
        int count = 0;
        for (int n = 0; n < x; n++) {
            int v = reverse(n);
            if ((v + "").length() == (n + "").length())
                if (odd(n + v) > 0) count++;
        }
        StdOut.println(count);
    }
}
