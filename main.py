import interface
import logica

def main():
    while True:
        interface.exibir_menu()
        opcao = input("Digite sua escolha: ")

        if opcao == "5":
            print("Saindo da calculadora. Até mais!")
            break

        if opcao in ["1", "2", "3", "4"]:
            num1, num2 = interface.obter_numeros()

            if opcao == "1":
                resultado = logica.somar(num1, num2)
            elif opcao == "2":
                resultado = logica.subtrair(num1, num2)
            elif opcao == "3":
                resultado = logica.multiplicar(num1, num2)
            elif opcao == "4":
                resultado = logica.dividir(num1, num2)

            interface.exibir_resultado(resultado)
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
