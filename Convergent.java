import java.math.BigInteger;
public class Convergent {
    public static void main(String[] args) {
        int N = Integer.parseInt(args[0]);

        BigInteger ONE = new BigInteger("1");
        BigInteger TWO = new BigInteger("2");

        BigInteger num = ONE;
        BigInteger den = ONE;
        int count = 0;
        for (int i = 0; i < N; i++) {
            BigInteger tem = num;
            num = num.add(den.multiply(TWO));
            den = den.add(tem);
            if (num.toString().length() > den.toString().length())
                count++;
        }
        StdOut.println(count);
    }
}
