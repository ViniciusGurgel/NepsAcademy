import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        int x = obj.nextInt();
        int soma = 0;
        for(int i = 0;i < x;i++){
            int L = obj.nextInt();
            int C = obj.nextInt();
            if(L > C){
                soma += C;
            }
        }
        System.out.println(soma);
        obj.close();
    }
}
