import java.math.BigInteger;
public class Scratch {
    public static void main(String[] args) {
		int N = Integer.parseInt(args[0]);
		int T = Integer.parseInt(args[1]);
		boolean[] man = new boolean[N];
		for (int i = 0; i < N; i++)
			man[i] = true;

		int count = N;
		for (int t = 0; t < T; t++) {
			StdOut.printf("T %2d  -- %5d\n", t, count);
			for (int i = 0; i < N; i++) {
				if (man[i] && StdRandom.bernoulli()) {
					man[i] = false;
					count--;
				}
			}
		}
	}
}
