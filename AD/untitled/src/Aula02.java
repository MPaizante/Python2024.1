public class Aula02 {
    public static void main(String[] args) {
    canal();
    System.out.println("Paizante");
    for (int i = 0; i < 3; i++){
        canal();
    }
    msg("Araujo",5);
    int r;
    r = soma2(10,5);
    System.out.println(r);

        System.out.println(soma(5,10,3,4,7,5));

        System.out.println(multiplicacao(5.0,2.578963));





    }

    public static void canal(){
        System.out.println("Matheus");
    }

    public static void msg(String m, int x) {
        for(int i =0; i < x; i++){
            System.out.println(m);
        }

    }
    public static int soma2(int x, int y){
        int s = x + y;
        return s;
    }
    public static int soma(int... numeros){
        int res =0;
        for(int x:numeros){
            res += x;
        }
        return res;
    }
    public static Double multiplicacao(Double... numeros){
        Double res =1.0;
        for (Double x:numeros){
            res = res * x;

        }
        return res;
    }
}
