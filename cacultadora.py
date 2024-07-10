# Criar a classe
# chamada "Calculadora"
class Calculadora:
    
    # Criar o método
    # chamado 'soma':
    def soma(self, n1, n2):
        return n1 + n2
    
    # Criar o método
    # chamado 'subtracao':
    def subtracao(self, n1, n2):
        return n1 - n2
    
    # Criar o método
    # chamado 'multiplicacao':
    def multiplicacao(self, n1, n2):
        return n1 * n2
    
    # Criar o método
    # chamado 'divisao':
    def divisao(self, n1, n2):
        if n2 == 0:
            raise ValueError("Não há divisão por zero")
            # raise ZeroDivisionError("Não há divisão por zero")
        else:
            return n1 / n2
    