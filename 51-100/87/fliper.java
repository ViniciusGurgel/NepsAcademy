import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        int P = obj.nextInt();
        int R = obj.nextInt();
        if(P == 0){
            System.out.println("C");
        }else if(R == 0){
            System.out.println("B");
        }else{
            System.out.println("A");
        }
        obj.close();
    }
}
