package Aula02;

public class Aula02 {
    public static void main(String[] args) {
    Carro carro1 =new Carro("Ferrari");
    Carro carro2 = new Carro("HRV");
    CarroCombate carro3 = new CarroCombate("X",100);
    CarroCombate carro4 = new CarroCombate("Pantera", 50);
    carro4.atirar();
    carro4.atirar();
    carro4.sofrerDano(30);
    carro1.setLigado(true);
    carro1.info();
    carro4.setLigado(true);
    carro4.info();





    }

}
