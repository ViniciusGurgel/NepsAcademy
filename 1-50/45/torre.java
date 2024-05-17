import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        int A = Integer.parseInt(obj.nextLine());
        int[][] lista = new int[A][A];
        for (int i = 0; i < A; i++) {
            String[] input = obj.nextLine().split(" ");
            for (int j = 0; j < A; j++) {
                lista[i][j] = Integer.parseInt(input[j]);
            }
        }

        int[][] nova_lista = new int[2][A];
        int[] linha = new int[A];
        int[] col = new int[A];
        for (int i = 0; i < A; i++) {
            int rowSum = 0;
            for (int j = 0; j < A; j++) {
                rowSum += lista[i][j];
                col[j] += lista[i][j];
            }
            linha[i] = rowSum;
        }
        
        nova_lista[0] = linha;
        nova_lista[1] = col;
        
        int[][] lista_final = new int[A][A];
        int maximo = 0;
        for (int i = 0; i < A; i++) {
            for (int j = 0; j < A; j++) {
                lista_final[i][j] = nova_lista[0][i] + nova_lista[1][j] - 2 * lista[i][j];
                maximo = Math.max(maximo, lista_final[i][j]);
            }
        }
        System.out.println(maximo);

        obj.close();
    }
}
