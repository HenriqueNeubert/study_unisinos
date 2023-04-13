package conceitos;
// public class App {
//     public static void main(String[] args) throws Exception {
//         System.out.println("Hello, World!!!");
//     }
// }

public class Carro {
    //Atributos
    String nome;
    String marca;
    int ano;
    int vel;

    //métodos
    void acelerar(int acelerar){
        vel += acelerar;
    }

    void freiar(int reduzir){
        vel -= reduzir;
    }

    void buzinar(){
        System.out.println("Biiiih!!!");
    }
}