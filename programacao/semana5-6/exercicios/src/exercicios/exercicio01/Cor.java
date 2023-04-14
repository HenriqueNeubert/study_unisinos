//Exercício 1. Crie uma classe chamada Cor, que possui 3 inteiros como atributos,
//sendo eles r, g e b. 
package exercicios.exercicio01;

public class Cor{
    private int red;
    private int green;
    private int blue;

    Cor(){}
    public void setCor(int red, int green, int blue){
        this.red = red;
        this.green = green;
        this.blue = blue;
    }

    public void setCor(int red, int green){
        this.red = red;
        this.green = green;
    }

    public int getRed(){
        return red;
    }
    public int getGreen(){
        return green;
    }
    public int getBlue(){
        return blue;
    }
}
