package exercicios.exercicio01;

public class CorTeste {
  public static void main(String [] args) {
    Cor rgb = new Cor(); 
    rgb.setCor(500, 250, 200);
    System.out.println("RGB:(" + rgb.getRed() + "," + rgb.getGreen() + "," +
     rgb.getBlue() + ")");

    rgb.setCor(500,200);
    System.out.println("RGB:(" + rgb.getRed() + "," + rgb.getGreen() + ")");
  }
}
