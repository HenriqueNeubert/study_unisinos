//Exercício 2. Crie uma classe chamada Computador, que possui 4 atributos, 
//sendo eles a marca, a velocidade, o ano de fabricação e um atributo que indica
//se o computador é novo.
package exercicios.exercicio02;

public class Computador{
  private String marca;
  private float velocidade;
  private int AnoFabricacao;
  private boolean novo;

  Computador(){} 

  public void setComputador(String marca, float velocidade, int AnoFabricacao, boolean novo){
    this.marca = marca;
    this.velocidade = velocidade;
    this.AnoFabricacao = AnoFabricacao;
    if(AnoFabricacao < 2023){
      this.novo = novo;
      System.out.println("SEMINOVO!");
    }else{
      System.out.println("NOVO!");
    }
  }
  public String getMarca(){
    return marca;
  }
  public float getVelocidade(){
    return velocidade;
  }
  public int getAnoFabricacao(){
    return AnoFabricacao;
  }
  public boolean getNovo(){
    return novo;
  }
}

