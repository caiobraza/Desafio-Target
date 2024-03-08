def fibonacci_sequence(numero):
    # Inicializar os dois primeiros números da sequência de Fibonacci
    a, b = 0, 1
    
    # Verificar se o número está na sequência de Fibonacci
    while b < numero:
        a, b = b, a + b
        if b == numero:
            return True
    
    return False

# Solicitar ao usuário para inserir um número
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

# Verificar se o número está na sequência de Fibonacci
if fibonacci_sequence(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")

