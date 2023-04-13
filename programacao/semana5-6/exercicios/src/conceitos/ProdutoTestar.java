package conceitos;
public class ProdutoTestar {
  public static void main(String [] args){

    //construtor padrão:
    Produto p1 = new Produto();
    p1.nome = "Lapis";
    p1.marca = "Bic";
    p1.valor = 1.50f;
    //construtor de 2 param
    Produto p2 = new Produto("Caneta", "Faber");
    p2.valor = 1.69f;
    //construtor de 3 param
    Produto p3 = new Produto("Borracha", "Mercur", 1.89f);

    //objeto p1

    System.out.println("Nome:" + p1.nome + " Marca:" + p1.marca + " Valor:" + p1.valor);
  }
}
