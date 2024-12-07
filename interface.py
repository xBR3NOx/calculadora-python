def exibir_menu():
    print("\n=== Calculadora ===")
    print("Escolha uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

def obter_numeros():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        return num1, num2
    except ValueError:
        print("Erro: por favor, insira números válidos.")
        return obter_numeros()

def exibir_resultado(resultado):
    print(f"Resultado: {resultado}")
