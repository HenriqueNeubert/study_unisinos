//Exercício 3. Crie uma classe chamada Lampada, que possui um atributo indicando 
//se a lâmpada está ligada.

package exercicios.exercicio03;

public class Lampada{
  boolean ligada;
}

// public static void main(String [] args) {}

// Exercício 4. Crie uma classe chamada Produto, que possui um nome, um valor, uma descrição (tipo String) e uma quantidade em estoque.

// Exercício 5. Crie um construtor para cada uma das classes criadas.

// Exercício 6. Pesquise (se necessário) e responda: o que é sobrecarga de métodos? 

// Exercício 7. Sobrecarregue o método construtor das classes criadas nos exercícios 1, 2, 3 e 4, criando mais um método deste tipo em cada uma delas.

// Exercício 8. O que são atributos? E o que são métodos?

// Exercício 9. O  que  é  e  para  que  serve um  método construtor? Quais  as  duas características necessárias para que um método seja o construtor da classe? Exemplifique sua resposta.

// Exercício 10. O que são e para que servem os métodos de acesso de uma classe? Exemplifique sua resposta.

// Exercício 11.  Seja x  uma variável inteira. Pesquise e responda: qual a diferença entre a utilização de x++  e ++x  no código? Exemplifique sua resposta.

// Exercício 12. Suponha  a  existência  de  uma  classe  chamada  ContaCorrente,  com  os  atributos número  da  conta  (do  tipo  int) e  saldo  atual  (do  tipo  double).  Sabendo  que  NÃO  FOI  CRIADO  UM CONSTRUTOR NA CLASSE ContaCorrente, apenas os métodos de acesso, escreva o método main para criar 3 contas correntes com as seguintes informações (número, saldo):

// Conta 1: 1234, 100.00
// Conta 2: 8765, -98.00
// Conta 3: 3342, 3445.80

// Exercício 13. Pesquisa (se necessário) e responda: o que é o método toString()? Como seria um exemplo de método toString()  dentro da classe ContaCorrente  descrita no exercício 12?

// Exercício 14. Considerando a classe abaixo, crie um método  main  que chama todos os métodos desta classe. A última linha de código deve ser a chamada ao método imprimeInformacoes(), na qual todas as informações devem aparecer corretamente.

// public class Empregado{
//    private String nome;
//    private char turno;
//    private double salario;
//    public void aumentaSalario(double aumento){
//       this.salario += aumento;
//    }
//    public double calculaAdicionalNoturno(){
//       if(turno == 'n')
//          turno = 'N';
//       if(turno == 'N')
//          return salario + salario*0.3;
//       return 0;
//    }
//    public void imprimeInformacoes(){
//       System.out.println("Nome: "+nome);
//       System.out.println("Turno: "+turno);
//       System.out.println("Salário: "+salário);
//       System.out.println("Adicional noturno: "+calculaAdicionalNoturno());
//    }
//    public Empregado(String nome){
//       this.nome = nome;
//    }
//    public void setTurno(char turno){
//       this.turno = turno;
//    }
//    public void setSalario(double salario){
//       this.salario = salario;
//    }
// }