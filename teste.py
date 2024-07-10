# Importando o pacote
# de testes unitários
import unittest

# Importando a classe
# 'Calculadora' pelo arquivo
# 'calculadora.py'
from calculadora import Calculadora

# Criando a classe de testes
# unitários chamada 'TestCalculadora'
class TestCalculadora(unittest.TestCase):
    
    # Criando o método de definição
    # do objeto que herdará a classe
    # 'Calculadora' chamado 'setUp'
    def setUp(self):
        self.calc = Calculadora()
        
    # Criando o teste do método
    # 'soma' da classe 'Calculadora'
    def test_soma(self):
        self.assertEqual(self.calc.soma(10, 20), 30)
        self.assertEqual(self.calc.soma(123, 456), 579)
        
    # Criando o teste do método
    # 'subtracao' da classe 'Calculadora'
    def test_subtracao(self):
        self.assertEqual(self.calc.subtracao(20, 10), 10)
        self.assertEqual(self.calc.subtracao(789, 456), 333)
        
    # Criando o teste do método
    # 'multiplicacao' da classe 'Calculadora'
    def test_multiplicacao(self):
        self.assertEqual(self.calc.multiplicacao(20, 10), 200)
        self.assertEqual(self.calc.multiplicacao(12, 34), 408)
        
    # Criando o teste do método
    # 'divisao' da classe 'Calculadora'
    def test_divisao(self):
        self.assertEqual(self.calc.divisao(20, 10), 2)
        self.assertEqual(self.calc.divisao(10, 20), 0.5)
        self.assertEqual(self.calc.divisao(10, 20), 0.5)
        self.assertRaises(ValueError, self.calc.divisao, 10, 0)
        
    
    # Criando o teste do método
    # 'divisao' da classe 'Calculadora'
    # para uma divisão por zero
    # def test_divisao_por_zero(self):
    #     with self.assertRaises(ZeroDivisionError):
    #         self.calc.divisao(10,0)
        
# Chamando a classe de
# Testes Unitários
if __name__ == '__main__':
    unittest.main()