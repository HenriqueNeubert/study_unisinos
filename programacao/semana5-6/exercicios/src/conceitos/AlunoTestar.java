package conceitos;
public class AlunoTestar {
  public static void main(String [] args) { 
    //constructor
    Aluno aluno1 = new Aluno();

    // aluno1.nome = "Henrique";
    //set = alterar, renomear
    aluno1.setNome("Henrique");
    //get = pegar
    System.out.println(aluno1.getNome());

    // aluno1.idade = 500;
    aluno1.setIdade(50);
    System.out.println(aluno1.getIdade());
  }  
}
