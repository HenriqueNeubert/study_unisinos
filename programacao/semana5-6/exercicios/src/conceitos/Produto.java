public class Produto {

  //atributos
  String nome;
  String marca ;
  float valor;

  //construtor-mesmo nomo da classe
  //nomes de construtores podem se repetir, desde que o conteúdo seja diferente
  //mesmo que não seje usado, deve  haver um construtor  padrão(vazio)
  Produto(){}

  Produto(String nome){
    this.nome = nome;
  }

  Produto(String nome, String marca) {
    this.nome = nome;
    this.marca = marca;
  }

  Produto(String nome, String marca, float valor){
    this.nome = nome;
    this.marca = marca;
    this.valor = valor;
  }
}