import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        int A = obj.nextInt();
        int B = obj.nextInt();
        int C = obj.nextInt();
        int result = (A == B) ? C : (B == C) ? A : B;
        System.out.println(result);
        obj.close();
    }
}
