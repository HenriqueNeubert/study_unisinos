// Exercício 12. Suponha  a  existência  de  uma  classe  chamada  ContaCorrente, 
// com  os  atributos número  da  conta  (do  tipo  int) e  saldo  atual  
// (do  tipo  double).  Sabendo  que  NÃO  FOI  CRIADO  UM CONSTRUTOR NA CLASSE 
// ContaCorrente, apenas os métodos de acesso, escreva o método main para criar 3 
// contas correntes com as seguintes informações (número, saldo):
// Conta 1: 1234, 100.00
// Conta 2: 8765, -98.00
// Conta 3: 3342, 3445.80
package exercicios.exercicio12;

public class ContaCorrente {
  private int numero;
  private double saldo;

  public void setNumber(int numero){
    this.numero = numero;
  }

  public void setSaldo(double saldo){
    this.saldo = saldo;
  }

  public int getNumero(){
    return numero;
  }

  public double getSaldo(){
    return saldo;
  }

}
