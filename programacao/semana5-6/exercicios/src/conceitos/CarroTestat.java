package conceitos;
public class CarroTestat {
  public static void main(String[] args){
    Carro c1 = new Carro();

    c1.nome = "Celta";
    c1.marca = "Chevrolet";
    c1.ano = 2015;
    c1.vel = 60;

    c1.acelerar(10);
    System.out.println("Velocidade: " + c1.vel   + "km/h");
    c1.freiar(30);
    System.out.println("Velocidade: " + c1.vel   + "km/h");

  }
}
