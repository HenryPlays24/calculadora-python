class Calculadora():
    def __init__(self, numero1=0.0, numero2=0.0):
        self._numero1 = numero1
        self._numero2 = numero2

    def get_numero1(self):
            return self._numero1
        
    def get_numero2(self):
            return self._numero2
        
        
    def set_numero1(self, numero1):
            self._numero1 = numero1

    def set_numero2(self, numero2):
            self._numero2 = numero2


    def calcular(self, operador):
        if operador == '+':
            return self._numero1 + self._numero2
        elif operador == '-':
            return self._numero1 - self._numero2
        elif operador == '*':
            return self._numero1 * self._numero2
        elif operador == '/':
            if self._numero2 == 0:
                return 'Error: Divisão por Zero!'
            return self._numero1 / self._numero2
        else:
            return 'Operador Invalido!'

try:             
    numero1 = float(input('Digite um número: '))
    numero2 = float(input('Digite outro número: '))

    operadores_validos = ['+', '-', '*', '/']

    operador = input('Digite um operador (+, -, *, /): ')
    while operador not in operadores_validos:
         print('Operadores Invalidos! Digite um operador válido.')
         break
    
    print(f'Você digitou o número: {numero1}')
    print(f'Você digitou outro número: {numero2}')

    calculadora = Calculadora(numero1, numero2)
    resultado = calculadora.calcular(operador)

    print(f"Resultado: {resultado}") 
     
except ValueError:
    print('Error: Digitou o número flutuante errado!')
