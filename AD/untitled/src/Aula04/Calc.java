package Aula04;
import java.util.Scanner;
public class Calc {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Numero n1 = new Numero(0);
        Numero n2 = new Numero(0);
        Numero res = new Numero(0);
        String opc = "S";

        while (opc.equals("s") || opc.equals("S")) {

            System.out.println("Digite o valor: ");
            n1.setValor(scanner.nextInt());
            System.out.println("Digite o valor: ");
            n2.setValor(scanner.nextInt());
            res.setValor(n1.getValor() + n2.getValor());
            System.out.println("Soma de " + n1.getValor() + " + " + n2.getValor() + " = " + res.getValor());
            System.out.println("Deseja somar outro valor ? ");
            opc = scanner.next();

        }

    }

}
