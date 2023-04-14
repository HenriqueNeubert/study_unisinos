package exercicios.exercicio04;

public class ProdutoTeste {
  public static void main(String [] args) {
    Produto prod = new Produto();
    prod.nome = "Caderno";
    prod.descricao = "Caderno tilibra capa dura.";
    prod.quantidade = 25f;
    prod.valor = 12.50f;
    System.out.println("Produto:" + prod.nome + "\nDescrição:" + prod.descricao
    + "\nQuantidade:" + prod.quantidade + "\nValor:" + prod.valor);

    prod.nome = "Caderno";
    prod.valor = 12.50f;
    System.out.println("Borracha:" + prod.nome + "\nValor:" + prod.valor);

    prod.nome = "Apontador";
    System.out.println("Produto:" + prod.nome);
  }
}
