public class TesteCarta{
    public static void main(String[] args){
        Carta c; 
        c = new Carta("Paus", 3, '3');
        String naipe = c.getNaipe();
        System.out.println("Original: " + naipe);
        
        c.setNaipe("Copas");
        naipe = c.getNaipe();
        System.out.println("Novo: " + naipe);
    }
}