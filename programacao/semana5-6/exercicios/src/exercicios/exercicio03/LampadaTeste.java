package exercicios.exercicio03;

public class LampadaTeste {
  public static void main(String [] args) {
    Lampada ligar = new Lampada();
    ligar.ligada = true;
    ligar.setLampada(true);
    System.out.println(ligar.getLampada());    
  }  
}
