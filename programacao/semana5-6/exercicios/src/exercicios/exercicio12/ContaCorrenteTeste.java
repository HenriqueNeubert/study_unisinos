package exercicios.exercicio12;
// Conta 1: 1234, 100.00
// Conta 2: 8765, -98.00
// Conta 3: 3342, 3445.80
public class ContaCorrenteTeste {
  public static void main(String [] args) {
    ContaCorrente usuario = new ContaCorrente();
    usuario.setNumber(1234);
    usuario.setSaldo(100.00);
    System.out.println(usuario.toString());
    usuario.setNumber(8765);
    usuario.setSaldo(-98.00);
    System.out.println(usuario.toString());
    // System.out.println("Número da conta:" + usuario.getNumero() + "\nSaldo: R$" + usuario.getSaldo());
    usuario.setNumber(3342);
    usuario.setSaldo(3445.80);
    System.out.println(usuario.toString());
    // System.out.println("Número da conta:" + usuario.getNumero() + "\nSaldo: R$" + usuario.getSaldo());    
  }
}
