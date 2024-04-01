package Aula03;

public class Veiculo {
    private String nome;
    private int tipo;
    public Veiculo(String nome, int tipo){
        this.nome = nome;
        this.tipo = tipo;

    }
    public void info(){
        System.out.println("Nome: "+this.nome);
        System.out.println("Tipo: "+this.tipo);
    }
    public String getNome(){
        return this.nome;
    }




}
