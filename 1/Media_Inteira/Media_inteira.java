import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        int A = obj.nextInt();
        int B = obj.nextInt();
        int media = (A+B) / 2;
        System.out.println(media);
        obj.close();
    }
}
