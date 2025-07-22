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
        """
        Subtrai o valor enviado do saldo, caso haja saldo suficiente.
        """
        if valor > self.saldo:
            return "saldo insuficiente."
        self.saldo -= valor
        return f"Enviado {valor:.2f} MZN para {numero}. Saldo actual: {self.saldo:.2f} MZN"
    
