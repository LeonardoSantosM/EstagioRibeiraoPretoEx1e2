#1
'''def fibonacci(numero_desajado):
    # Colocando o primeiro valor da sequência de fibonacci
    primeiro_fibonacci = 1
    # Segundo valor da sequência de fibonacci
    segundo_fibonacci = 0
    # definindo uma variavel para receber o valor temporario
    while primeiro_fibonacci <= numero_desajado:
        if primeiro_fibonacci == numero_desajado:
            return f'O número pertence á sequência Fibonacci'
        temp = primeiro_fibonacci
        primeiro_fibonacci = segundo_fibonacci + primeiro_fibonacci
        segundo_fibonacci = temp
    return f'O número não pertence á sequência Fibonacci'

numero_desejado = int(input(f'Digite um numero: '))

resultado = fibonacci(numero_desejado)

print(resultado)'''

#2
def verificar_a(string):

    string_lower = string.lower()

    count_a = string_lower.count('a')

    if count_a > 0:
        print(f"A letra 'a' ocorre {count_a} na frase.")
    else:
        print("Não tem 'a' na frase")


texto = input("Digite uma frase: ")
verificar_a(texto)
