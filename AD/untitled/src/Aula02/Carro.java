package Aula02;

public class Carro {
    private String nome;
    private Boolean ligado;
    private Boolean destruido;
    private int blindagem;
    private Boolean armamento;

    public Carro(String nome){
        this.nome =nome;
        this.ligado = false;
        this.destruido= false;
        this.blindagem = 0;
        this.armamento = false;
    }
    public String getNome(){
        return this.nome;
    }
    public Boolean getLigado(){
        return this.ligado;
    }
    public void setLigado(Boolean ligado){
        this.ligado = ligado;
    }
    public Boolean getDestruido(){
        return this.destruido;
    }
    public void setDestruido(Boolean destruido){

    }

    public Boolean getArmamento() {
        return armamento;
    }

    public int getBlindagem() {
        return blindagem;
    }

    public void sofrerDano(int dano){
         this.blindagem -= dano;
         if(this.blindagem <=0){
             this.blindagem = 0;
             this.ligado = false;
             this.destruido = true;
         }
    }

    public void setArmamento(Boolean armamento) {
        this.armamento = armamento;
    }

    public void setBlindagem(int blindagem) {
        this.blindagem = blindagem;
    }


    public void info(){
        System.out.println("---------------------------------------");
        System.out.println("Nome: "+this.nome);
        System.out.println("Ligado: "+ (this.ligado ?"Sim":"Não"));
        System.out.println("Detruido: "+(this.destruido ?"Sim":"Não"));
        System.out.println("Blindagem: "+this.blindagem);
        System.out.println("Armamento: "+ (this.armamento ?"Sim":"Não"));
    }
}

