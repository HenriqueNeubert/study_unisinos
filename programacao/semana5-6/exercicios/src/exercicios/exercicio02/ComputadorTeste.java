package exercicios.exercicio02;

public class ComputadorTeste {
  public static void main(String [] args) {
    Computador pc = new Computador();
    pc.setComputador("DT-25", 300, 2015, false);

    System.out.println(pc.getMarca());
    System.out.println(pc.getAnoFabricacao());
    System.out.println(pc.getNovo());
    System.out.println(pc.getVelocidade());

    pc.setComputador("AR34", 2500);
    System.out.println(pc.getMarca());
    System.out.println(pc.getVelocidade());

  }
}
