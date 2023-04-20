public class TesteFruta{
    public static void main(String[] args){
        Fruta item1;
        Fruta item2;
        item1 = new Fruta("Banana", 2.50);
        item2 = new Fruta("Abacaxi", 6.00);
        
        System.out.println(item1.getNome());
        System.out.println(item2.getNome());
        
        double preco = item1.getPreco();
        System.out.println(item1.getPreco());
        
        item1.setNome("Banana Caturra");
        item1.setPreco(3.00);
        
        System.out.println("Novo nome: " + item1.getNome() + " e Novo preço: " + item1.getPreco());
    
        double imposto = 0.5;
        double precoFinal = item1.calculaPreco(imposto);   
        System.out.println("Preço Final: " + precoFinal);
    }
}