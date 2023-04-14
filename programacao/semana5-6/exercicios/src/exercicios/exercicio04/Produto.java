//Exercício 4. Crie uma classe chamada Produto, que possui um nome, um valor, 
//uma descrição (tipo String) e uma quantidade em estoque.


package exercicios.exercicio04;

public class Produto{
  String nome;
  float valor;
  String descricao;
  float quantidade;
  Produto(){}
  Produto(String nome, float valor, String descricao, float quantidade){
    this.nome = nome;
    this.valor = valor;
    this.descricao = descricao;
    this.quantidade = quantidade;
  }

  Produto(String nome, float valor){
    this.nome = nome;
    this.valor = valor;
  }

  Produto(String nome){
    this.nome = nome;
  }
}
