package Aula01;

public class Aula01 {
    public static void main(String[] args) {

        int num = 0;
        Aula01Jogador.pontos();
        Aula01Jogador.pontos();
        Aula01Jogador.pontos();
        System.out.println("Alerta "+(Aula01Jogador.alerta ? "Sim": "Não"));
        Aula01Jogador j1 = new Aula01Jogador(++num);
        Aula01Jogador j2 = new Aula01Jogador(++num);
        Aula01Jogador j3 = new Aula01Jogador(++num);

        //j1.num = 10;
        //j2.num = 5;

        //System.out.println(j1.num);
        //System.out.println("O valor de j2 = "+j2.num);
        j1.addVidas();
        j1.addVidas();
        System.out.println("Vidas do Jogador 1 = " + j1.getVidas());
        Aula01Jogador.alerta = true;
        j1.info();
        j2.info();
        Aula01Jogador.alerta = false;
        j3.info();










    }


}
