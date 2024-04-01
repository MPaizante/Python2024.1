package Aula02;

public class CarroCombate extends Carro{
    private final int MaxArmamento = 100;
    private final int MinArmamento = 0;
    private int qtdArmamento = 0;


    public CarroCombate(String nome, int blindagem){
        super(nome);
        setArmamento(true);
        setBlindagem(blindagem);
        this.qtdArmamento = 100;
    }
    public void setQtdArmamento(int armamento){
        this.qtdArmamento += armamento;
        if(this.qtdArmamento > MaxArmamento){
            this.qtdArmamento = MaxArmamento;
        }else if(this.qtdArmamento < MinArmamento){
            this.qtdArmamento = MinArmamento;
        }
    }
    public int getQtdArmamento(){
        return this.qtdArmamento;
    }
    public void atirar(){
        if(this.qtdArmamento > MinArmamento){
            setQtdArmamento(-1);
        }else {
            System.out.println("Sem munição!");
        }
    }
    public void info(){
        super.info();
        System.out.println("Quantidade Armamento: "+ this.qtdArmamento);

    }
}
