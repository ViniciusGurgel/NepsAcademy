import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        int P = obj.nextInt();
        int R = obj.nextInt();
        char result = (P == 0) ? 'C' : (R == 0) ? 'B' : 'A';
        System.out.println(result);
        obj.close();
    }
}
