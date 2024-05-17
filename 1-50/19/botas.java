import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        int N = Integer.parseInt(obj.nextLine());
        List<String[]> lista = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            lista.add(obj.nextLine().split(" "));
        }

        int count = 0;
        int i = 0;

        while (i < lista.size()) {
            String number = lista.get(i)[0];
            String character = lista.get(i)[1];
            int j = i + 1;
            boolean found = false;
            while (j < lista.size()) {
                if (number.equals(lista.get(j)[0]) && !character.equals(lista.get(j)[1])) {
                    lista.remove(j);
                    lista.remove(i);
                    count++;
                    found = true;
                    break;
                }
                j++;
            }
            if (!found) {
                i++;
            }
        }
        System.out.println(count);
        obj.close();
    }
}
