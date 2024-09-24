def main():
    """
    Função principal do programa.
    """
    while True:  # Laço infinito
        print("#######################################################")
        print("## CALCULADORA DO SISTEMAS INTERNACIONAL DE UNIDADES ##")
        print("#######################################################")

        print("\nEscolha uma conversão:")
        print("1. Comprimento (m para km)")
        print("2. Comprimento (km para m)")
        print("3. Massa (g para kg)")
        print("4. Massa (kg para g)")
        print("5. Volume (l para ml)")
        print("6. Volume (ml para l)")
        print("7. Velocidade (km/h para m/s)")
        print("8. Velocidade (m/s para km/h)")
        print("0. Sair")

        escolha = input("Digite sua escolha: ")

        if escolha == "0":  # Sai do programa quando a escolha é 0
            print("Saindo do programa.")
            break

        if escolha == "1":
            metros = float(input("Digite o valor em metros: "))
            quilometros = None
            print(f"{metros} metros são {quilometros} quilômetros.")
            
        elif escolha == "2":
            quilometros = float(input("Digite o valor em quilômetros: "))
            metros = None
            print(f"{quilometros} quilômetros são {metros} metros.")

        elif escolha == "3":
            gramas = float(input("Digite o valor em gramas: "))
            quilogramas = None
            print(f"{gramas} gramas são {quilogramas} quilogramas.")
           
        elif escolha == "4":
            quilogramas = float(input("Digite o valor em quilogramas: "))
            gramas = None
            print(f"{quilogramas} quilogramas são {gramas} gramas.")

        elif escolha == "5":
            litros = float(input("Digite o valor em litros: "))
            mililitros = None
            print(f"{litros} litros são {mililitros} mililitros.")

        elif escolha == "6":
            mililitros = float(input("Digite o valor em mililitros: "))
            litros = None
            print(f"{mililitros} mililitros são {litros} litros.")

        elif escolha == "7":
            kmph = float(input("Digite o valor em km/h: "))
            mps = None
            print(f"{kmph} km/h são {mps} m/s.")

        elif escolha == "8":
            mps = float(input("Digite o valor em m/s: "))
            kmph = None
            print(f"{mps} m/s são {kmph} km/h.")

        else:
            print("Escolha inválida. Por favor, tente novamente.")

# ----------------------------------------------------------------------------------------
if __name__ == "__main__":  # Garante que se o módulo for importado não será executado
    main()  # Chamada da função principal
