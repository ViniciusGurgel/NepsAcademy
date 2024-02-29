import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        int x = obj.nextInt();
        String result = (x == 0) ? "nulo" : (x >= 0) ? "positivo" : "negativo";
        System.out.println(result);
        obj.close();
    }
}
