import java.lang.reflect.Array;
import java.security.SecureRandom;
import java.util.Arrays;
import java.util.Scanner;
public class Ola {
    public static void main(String[] args) {
       final int linhas = 3;
       final int colunas = 5;
       int [][] numeros = new int [linhas][colunas];


       for (int i = 0; i < linhas; i++){
           for (int j = 0; j < colunas;j++){
               numeros[i][j] = new SecureRandom().nextInt(100);

           }
        }

        for (int i = 0; i < linhas; i++){
            for (int j = 0; j < colunas;j++){
                System.out.printf("%2d | ",numeros[i][j]);

            }
            System.out.println();
        }
        System.out.println();
        for (int[] n:numeros){
            for (int v:n){
                System.out.printf("%4d | ",v);
            }
            System.out.println();
        }



    }

}
