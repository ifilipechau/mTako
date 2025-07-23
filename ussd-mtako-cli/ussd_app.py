# ussd_app.py

# Importar funções e classes necessárias para o sistema

from menu import main_menu, get_service_menu
from core import Mtako

def run_ussd():
    """
    Função principal que executa o loop da aplicação USSD na linha de comandos.
    """
    mtako = Mtako() # Instancia o sistema

    while True:
        # Mostra o menu principal e espera a escolha do utilizador
        opcao = input(main_menu())

        # Encerrar a sessão
        if opcao == "0":
            print("Sessão terminada. Obrigado por usar M-Tako CLI.")
            break

        # Enviar Dinheiro
        elif opcao == "1":
            print(get_service_menu(opcao))
            numero = input("Número: ")
            valor = float(input("Valor a enviar (MZN): "))
            print(mtako.enviar_dinheiro(numero, valor))
        
        # Levantar Dinheiro
        elif opcao == "2":
            print(get_service_menu(opcao))
            codigo = input("Código do agente: ")
            valor = float(input("Valor a levantar (MZN): "))
            print(mtako.levantar_dinheiro(codigo, valor))
        
        # Pagamento de Serviços
        elif opcao == "3":
            print(get_service_menu(opcao))
            servico = input("Serviço: ")
            valor = float(input("Valor a pagar (MZN): "))
            print(f"{valor:.2f} MZN pago para serviço {servico}. Obrigado.")

        # Consultar Saldo
        elif opcao == "4":
            print(get_service_menu(opcao))
            pin = input("PIN: ")
            print(mtako.consultar_saldo(pin))

        # Alterar PIN
        elif opcao == "5":
            print(get_service_menu(opcao))
            old_pin = input("PIN actual: ")
            new_pin = input("Novo PIN: ")
            print(mtako.alterar_pin(old_pin, new_pin))

        # Opção inválida
        else:
            print("Opção inválida. Tente novamente.")

# Executa a função principal se este ficheiro for o ponto de entrada
if __name__ == "__main__":
    run_ussd()
            
