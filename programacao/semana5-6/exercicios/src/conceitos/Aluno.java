package conceitos;
public class Aluno {
  //private = modificador de acesso
  private String nome;
  private int idade;

  //void = tipo de retorno (vazio)
  public void setNome(String nome){
    this.nome = nome;
  }
  //String = tipo de retorno (texto)
  public String getNome() {
    return nome;    
  }

  public void setIdade(int idade){
    if(idade >= 0 && idade <= 130){
      this.idade = idade;
      System.out.println("Idade Cadastrada");
    }
    else{
      System.out.println("Idade inválida");
    }
  }

  public int getIdade(){
    return idade;
  }
}
