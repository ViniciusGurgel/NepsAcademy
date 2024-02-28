import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        int L = obj.nextInt();
        int quadrado = L * L;
        System.out.println(quadrado);
        obj.close();
    }
}
