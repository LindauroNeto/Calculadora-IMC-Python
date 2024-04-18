# CÁLCULO IMC
import os

resposta = ''

while (resposta != 'nao'):
    
    os.system("cls")
    print("-------------------------------------------------------------")
    print("                         CÁLCULO IMC                         ")
    print("-------------------------------------------------------------")
    
    peso = float(input("Digite o seu peso: "))
    altu = float(input("Digite a sua altura: "))
    
    imc = peso / altu ** 2
    
    print("------------------------------------------------------------")
    print("                         RESULTADOS                         ")
    print("------------------------------------------------------------")
    
    if (imc < 18.5):
        print("Você está abaixo do peso ideal.")
    elif (imc >= 18.5 and imc < 24.9):
        print("Você está com o peso ideal.")  
    elif (imc >= 24.9 and imc < 29.9):
        print("Você está acima do peso ideal(sobrepeso).")
    elif (imc > 30):
        print("Você está em situação de obesidade, procure orientação médica.")
    
    print(f"PESO: {peso} kg")
    print(f"ALTURA: {altu} m")
    print(f"IMC: {round(imc, 2)}")
    
    print("------------------------------------------------------------")
    print("Você gostaria de fazer um novo cálculo?")
    
    while (True):
        resposta = input("Digite \'sim\' ou \'nao\': ")
        if (resposta == 'sim'):
            break
        elif (resposta == 'nao'):
            print("Obrigado por consultar a calculadora!")
            break
        else:
            print("Resposta inválida.")
            
            