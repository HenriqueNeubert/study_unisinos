//Exercício 3. Crie uma classe chamada Lampada, que possui um atributo indicando 
//se a lâmpada está ligada.

package exercicios.exercicio03;

public class Lampada{
  boolean ligada;
  String cor;

  Lampada(){}
  public void setLampada(boolean ligada){
    if(ligada){
      this.ligada = ligada;
      System.out.println("LIGADA!");
    }else{
      this.ligada = ligada;
      System.out.println("DESLIGADA!");
    }
  }
  public void setLampada(boolean ligada, String cor){
    if(ligada){
      this.ligada = ligada;
      System.out.println("LIGADA!");
    }else{
      this.ligada = ligada;
      System.out.println("DESLIGADA!");
    }
    this.cor = cor;
  }

  public boolean getStatus(){
    return ligada;
  }
  public String getCor(){
    return cor;
  }

}

