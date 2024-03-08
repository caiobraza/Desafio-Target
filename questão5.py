def inverter_string(string):
    # Criar uma string vazia para armazenar a string invertida
    string_invertida = ""

    # Iterar sobre os caracteres da string original em ordem reversa
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]

    return string_invertida

# Exemplo de uso
string_original = input("Digite uma string para inverter: ")
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)
