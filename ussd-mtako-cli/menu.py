# menu.py

def main_menu():
    """
    Retorna o menu principal do sistema USSD.
    """
    return """

Bem-vindo ao mTako CLI
1. Enviar Dinheiro
2. Levantar Dinheiro
3. Pagamento de Serviço
4. Consultar Saldo
5. Alterar PIN
0. Sair
Escolha uma opção: """

def get_service_menu(service):
    """
    Recebe uma opção do menu principal e retorna o submenu correspondente.
    """

    menus = {
        "1": "\n-- Enviar Dinheiro --\nDigite o número do destinatário:",
        "2": "\n-- Levantar Dinheiro --\nDigite o código do agente:",
        "3": "\n-- Pagamento de Serviços --\n1. EDM\n2. Água\n3. Internet\nEscolha:",
        "4": "\n-- Consultar Saldo --\nDigite seu PIN:",
        "5": "\n-- Alterar PIN --\nDigite o PIN actual:",
    }
    return menus.get(service, "\nOpção inválida.") # Retorna o menu ou mensagem de erro