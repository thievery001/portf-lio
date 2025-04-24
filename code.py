#Inicio do Portifólio
print("Olá pessoal, nós do grupo de desenvolvimento (Vinícius Taiguara, Paulo Vitor, Gabriel Felipe, Maycon Henrique e Giovane Henrique), estamos criando este portifólio para explicar para vocês um pouco do que estamos aprendendo até o momento no curso de Análise e Desenvolvimento de Sistemas")

#Partindo para o assunto
print("Dando início ao assunto, começaremos a falar do (print), que em português, significa imprimir, onde no Python, sua função é imprimir algo na tela. Uma observação importante é que para o (print) funcionar e imprima algo na dela, será necessário o uso das duas aspas ou aspas simples")
print("Outra observação é que se usado as o (print) sem aspas, poderá acabando chamar a variavel que está sendo usada, caso contrario poderá trazer um erro no código, se não existir essa variavel em específico")

#Exemplo
print("como por exemplo: ")
print("Olá mundo!")

#Continuidade do Assunto
print("Agora falaremos da função (input), que tem como finalidade fazer que o usuário possa digitar algo na dela, isso é mais utilizado para fazer perguntas para os usuários.")
print("Uma observação importante é que em alguns caso do input vem acompanhado de algumas funções anteriores, como o float, int, str. Que em alguns casos são utilizados em casos mais específicos.")
print("Em geral a função final do (input) é a digitação que poderá ser feita pelo usuário na tela.")
print("Como por exemplo: ")
print("nome = input(Digite seu nome: ")

#Exemplo
print("nome = input(Digite seu nome: )")
print("Após o comando dado, o usuário poderá digitar na tela.")


# Loops de repetição For e While

# Loop For

print(''' Loop For: O loop for em Python é uma estrutura de controle que permite iterar sobre uma sequência (como uma lista, uma string ou uma faixa de números), executando um bloco de código repetidamente para cada item da sequência.''')

# Loop While

print(''' Loop While: O loop while é um dos métodos fundamentais em Python para realizar a repetição de um bloco de código enquanto uma condição específica é verdadeira. Essa estrutura permite que programas executem tarefas repetitivas com eficiência, sem a necessidade de escrever o mesmo código várias vezes.''')

# Diferença de For e While

print(''' A principal diferença entre um loop for e um loop while reside na sua forma de controlar o número de iterações. Um loop for é geralmente usado quando se conhece o número exato de iterações antecipadamente, enquanto um loop while é usado quando a iteração é condicionada a uma condição, que pode não ser o número de iterações.''')

# Exemplo prático For

print('''for i in range(1, 11):
          print(i)''')

print('''numeros = [5, 10, 3, 8]
      soma = 0

      for n in numeros:
          soma += n

          print("Soma:", soma)''')

print('Explição exemplo 1: range(1, 11) vai de 1 até 10 (o 11 é exclusivo).')

print('Explicação exemplo 2: O loop percorre a lista numeros e soma cada item')

# Exemplo prático While

print('''contador = 1

      while contador <= 5:
          print(contador)
              contador += 1''')

print('Explicação: Enquanto o contador for menor ou igual a 5, ele imprime e soma + 1')

print('''senha_correta = "1234"
      senha = ""

      while senha != senha_correta:
          senha = input("Digite a senha: ")

          print("Acesso liberado!")''')

print('Explicação: O loop continua até o usuário digitar a senha correta')


#Exemplo
print("nome = input(Digite seu nome: )")
print("Após o comando dado, o usuário poderá digitar na tela.")
