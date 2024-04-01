package Aula01;

public class Aula01Jogador {

    private int num;
    private int vidas;
    static  boolean alerta = false;
    static  int qtdJogadores = 0;

    static int pontosJogadores = 0;

    private final int MaxVidas = 3;
    public Aula01Jogador(int num){
        this.num = num;
        this.vidas = 1;
        qtdJogadores++;
        System.out.println("Jogar "+num+" criado!");
    }



    public int getVidas(){
        return this.vidas;
    }


    public void addVidas(){
        if (this.vidas < MaxVidas) {
            this.vidas++;
        }

    }
    static void pontos(){
        pontosJogadores +=10;
    }
    public void info(){
        System.out.printf("%nJogador: %d%n",this.num);
        System.out.printf("%nVidas: %d%n",this.vidas);
        System.out.printf("%nAlerta: %s%n",(alerta ? "Sim" :"Não"));
        System.out.printf("%nQuantidade de jogadores: %d%n",qtdJogadores);
        System.out.printf("%nPontos de jogadores: %d%n",pontosJogadores);
        System.out.println("-----------------------");
    }




















}
