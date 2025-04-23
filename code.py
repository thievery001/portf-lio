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
