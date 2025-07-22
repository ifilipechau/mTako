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
    
    def levantar_dinheiro(self, codigo, valor):
        """
        Simula um levantamento de dinheiro num agente, descontando do saldo.
        """
        if valor > self.saldo:
            return "Saldo insuficiente."
        self.saldo -= valor
        return f"Levantamento de {valor:.2f} MZN feito no agente {codigo}. Saldo: {self.saldo:.2f} MZN."

    def consultar_saldo(self, pin):
        """
        Mostra o saldo apenas se o PIN estiver correcto.
        """
        if pin != self.pin:
            return "PIN incorrecto."
        return f"Seu saldo é {self.saldo:2f} MZN."
    