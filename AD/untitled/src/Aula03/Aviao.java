package Aula03;

public class Aviao extends Veiculo{
    private int categoria;
    public Aviao(String nome, int categoria){
        super(nome,10);
        this.categoria = categoria;

    }
    public void info(){
        super.info();
        System.out.println("Nome: "+super.getNome());
        System.out.println("Categoria: "+this.categoria);
    }
}
