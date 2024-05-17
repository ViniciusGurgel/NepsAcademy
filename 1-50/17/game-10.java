import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        int N = obj.nextInt();
        int D = obj.nextInt();
        int A = obj.nextInt();
        int result = (A > D) ? D + (N - A) : D - A; 
        System.out.println(result);
        obj.close();
    }
}
