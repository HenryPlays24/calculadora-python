🧮 Calculadora em Python
Este é um simples programa de calculadora em Python que permite ao usuário realizar operações básicas de soma, subtração, multiplicação e divisão entre dois números fornecidos.

📌 Funcionalidades
Operações suportadas: + (adição), - (subtração), * (multiplicação) e / (divisão).
Controle de erro para divisão por zero.
Validação da entrada do usuário para garantir que apenas números válidos sejam utilizados.
Uso de métodos getter e setter para manipulação segura dos atributos.
🚀 Como Executar
Certifique-se de ter Python 3.12 instalado em seu sistema. Para rodar o programa, execute o seguinte comando no terminal:

Python calculadora.py

📌 Exemplo de Uso

Digite um número: 10
Digite outro número: 5
Digite um operador (+, -, *, /): +

Você digitou o número: 10.0
Você digitou outro número: 5.0
Resultado: 15.0

Caso o usuário insira um operador inválido:

Digite um operador (+, -, *, /): x
Operadores Inválidos! Digite um operador válido.

Caso o usuário tente dividir por zero:

Digite um número: 7
Digite outro número: 0
Digite um operador (+, -, *, /): /
Resultado: Error: Divisão por Zero!

🛠 Estrutura do Código

O código é baseado em uma classe chamada Calculadora, que possui:

Atributos privados _numero1 e _numero2.

Métodos get_numero1() e get_numero2() → para acessar os números.

Métodos set_numero1(numero1) e set_numero2(numero2) → para modificar os números.

Método calcular(operador) → realiza a operação com base no operador informado.
