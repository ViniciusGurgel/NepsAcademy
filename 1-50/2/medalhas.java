import java.util.Scanner;
import java.util.Arrays;

public class Main {
    
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        int t1 = obj.nextInt();
        int t2 = obj.nextInt();
        int t3 = obj.nextInt();
        int[][] lista = {{t1,1}, {t2,2}, {t3,3}};
        Arrays.sort(lista, (a, b) -> Integer.compare(a[0], b[0]));
        System.out.println(lista[0][1]);
        System.out.println(lista[1][1]);
        System.out.println(lista[2][1]);
        obj.close();
    }
}
