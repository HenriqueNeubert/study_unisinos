public class TesteFruta{
    public static void main(String[] args){
        Fruta item;
        item = new Fruta("Banana", 2.50);
        String nome = item.getNome();
        System.out.println(nome);
        
        double preco = item.getPreco();
        System.out.println(preco);
        
        item.setNome("Banana Caturra");
        item.setPreco(3.00);
        
        preco = item.getPreco();
        nome = item.getNome(); 
        System.out.println("Novo nome: " + nome + " e Novo preço: " + preco);
    
        double imposto = 0.5;
        double precoFinal = item.calculaPreco(imposto);   
        System.out.println("Preço Final: " + precoFinal);
    }
}