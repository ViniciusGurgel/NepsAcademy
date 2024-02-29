import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        int A = obj.nextInt();
        int B = obj.nextInt();
        String result = ((A+B) % 2 == 0) ? "Bino" : "Cino";
        System.out.println(result);
        obj.close();
    }
}
