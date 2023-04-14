// Exercício 6. Pesquise (se necessário) e responda: o que é sobrecarga de métodos? 
  Sobrecarga é quando temos dois ou mais métodos com o mesmo nome, mas que
diferenciam nos parâmetros ou tipo de retorno. Por exemplo, é possível criar mais de
um construtor para uma classe, cada um recebendo parâmetros diferentes.



// Exercício 8. O que são atributos? E o que são métodos?
  Atributos são as propriedades de um objeto. Métodos são as ações que um objeto 
pode realizar.


// Exercício 9. O  que  é  e  para  que  serve um  método construtor? Quais  as  
duas características necessárias para que um método seja o construtor da classe? 
Exemplifique sua resposta.
  O método construtor serve para inicializar os atributos da classe. Para ser o método
construtor da classe precisa ter o mesmo nome da classe e não possuir tipo de
retorno. 
  


// Exercício 10. O que são e para que servem os métodos de acesso de uma classe? Exemplifique sua resposta.
  Servem para pegar ou modificar informações de um determinado atributo da classe.
O método de acesso GET serve para pegar a informação armazenada no atributo,
enquanto o SET serve para modificar a informação do atributo.
Por exemplo, os métodos de acesso de um atributo nome do tipo String em uma
classe qualquer seria desta forma: 
  public String getNome(){
    return nome;
  }
  public void setNome(String nome){
    this.nome = nome;
  }

// Exercício 11.  Seja x  uma variável inteira. Pesquise e responda: qual a diferença entre a utilização de x++  e ++x  no código? Exemplifique sua resposta.
  A utilização de ++x faz a adição de 1 na variável x (incremento) e na mesma
linha esse valor já pode ser usado com essa modificação (ou seja, primeiro soma
e depois usa). 
  Já x++ também faz a adição de 1 na variável x, porém essa modificação
ocorrerá após a utilização da variável (ou seja, usa e depois soma).
  int x = 10;
  System.out.println(++x); //imprime 11
  System.out.println(x++); //imprime 11
  System.out.println(x); //imprime 12



// Exercício 13. Pesquisa (se necessário) e responda: o que é o método toString()?
 Como seria um exemplo de método toString()  dentro da classe ContaCorrente  
 descrita no exercício 12?
    O método toString retorna uma representação no formato de texto de determinado
objeto de uma classe. Por exemplo, na classe ContaCorrente (do exercício 12),
poderemos fazer o método toString retornar de várias formas, uma delas pode ser
vista abaixo:

  public String toString(){
    return "Número da conta: " + getNumeroConta() + "Saldo
    atual: " + getSaldoAtual();
  }
  Desta forma, quando fizermos:
    ContaCorrente c = new ContaCorrente();
    System.out.println(c);

  A impressão na tela será o retorno do método toString (não importando o conteúdo
dos atributos). Caso não houvesse a implementação explícita do toString, a impressão
na tela, neste exemplo, seria algo como ContaCorrente@CODIGO_HEXADECIMAL,
mostrando onde a referência está alocada na memória.