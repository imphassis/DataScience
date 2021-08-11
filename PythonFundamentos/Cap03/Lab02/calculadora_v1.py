# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")
print("""1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão""")
userChoice = input('Digite o número da operação desejada: ')
firstNumber = input('Digite o primeiro número: ')
secondNumber = input('Digite o segundo número: ')

oper = {1: lambda x, y: x+y, 2: lambda x, y: x-y, 3: lambda x,y :x*y, 4: lambda x,y :x/y}
result = oper[int(userChoice)](int(firstNumber), int(secondNumber))
print(f' O resultado da sua operação é {result}')