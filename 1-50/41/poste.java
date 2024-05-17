import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        int N = Integer.parseInt(obj.nextLine());
        int[] lista = new int[N];
        for (int i = 0; i < N; i++) {
            lista[i] = obj.nextInt();
        }

        int count = 0;
        int count1 = 0;
        for(int i = 0;i < N;i++){
            if(lista[i] < 50){
                count++;
            }else if(lista[i] >= 85){
                continue;
            }else{
                count1++;
            }
        }

        System.out.println(count + " " + count1);
        obj.close();
    }
}
