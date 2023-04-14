// Exercício 6. Pesquise (se necessário) e responda: o que é sobrecarga de métodos? 
  Sobrecarga de métodos seria quando mais de um método é criado utilizando o 
mesmo nome com parâmetros diferentes. Sendo em quantidade ou tipos. 


// Exercício 8. O que são atributos? E o que são métodos?
  Atributos são as propriedades de um objeto. Métodos são as ações que um objeto 
pode realizar.


// Exercício 9. O  que  é  e  para  que  serve um  método construtor? Quais  as  
duas características necessárias para que um método seja o construtor da classe? 
Exemplifique sua resposta.
  


// Exercício 10. O que são e para que servem os métodos de acesso de uma classe? Exemplifique sua resposta.
  São get e set, eles servem tanto para pegar quanto para renomear um atributo.


// Exercício 11.  Seja x  uma variável inteira. Pesquise e responda: qual a diferença entre a utilização de x++  e ++x  no código? Exemplifique sua resposta.
  A instrução ++i, incrementa a variável iantes dela ser utilizada no comando. Já a instrução i++, incrementa a variável idepois dela ser utilizada no comando.


// Exercício 13. Pesquisa (se necessário) e responda: o que é o método toString()?
 Como seria um exemplo de método toString()  dentro da classe ContaCorrente  
 descrita no exercício 12?
    É um metodo padrão da linguagem que funciona para formatar e organizar objetos. 
    ///CÓDIGO
    public String toString(){
      return "Número da conta:" + getNumero() + "\nSaldo: R$" + 
      getSaldo();
    }
    System.out.println(usuario.toString());
    ///CÓDIGO


// Exercício 14. Considerando a classe abaixo, crie um método  main  que chama
todos os métodos desta classe. A última linha de código deve ser a chamada ao
método imprimeInformacoes(), na qual todas as informações devem aparecer 
corretamente.

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