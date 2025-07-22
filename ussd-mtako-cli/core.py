# core.py

class Mtako:
    """
    Classe que simula funcionalidades básicas de um sistema M-tako.
    """

    def __init__(self):
        # Inicializa o saldo e o PIN padrão
        self.saldo = 1000.0
        self.pin = "1234"

    def enviar_dinheiro(self, numero, valor):
        