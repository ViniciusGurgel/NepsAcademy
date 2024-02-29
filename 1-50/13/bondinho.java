import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        int A = obj.nextInt();
        int M = obj.nextInt();
        char result = (A+M > 50) ? 'N' : 'S';
        System.out.println(result);
        obj.close();
    }
}
