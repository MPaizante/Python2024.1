import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Scanner;
public class Ola {
    public static void main(String[] args) {
        int [] num = {20,2,40,10,11,98,77,12,0,3};
        for (int i = 0; i < num.length; i++){
            System.out.printf("%d  ",num[i]);
        }

        Arrays.sort(num);
        System.out.println();
        for (int n:num){
            System.out.printf("%d  ",n);
        }
        final  int tam = 10;
        int [] numeros = new int[tam];
        System.arraycopy(num, 0 ,numeros,0, tam);
        System.out.println();
        System.out.printf("São iguais: %s", Arrays.equals(num,numeros));




    }

}
