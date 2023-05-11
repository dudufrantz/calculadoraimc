#desenvolva uma calculadora de imc, o programa deve pedir a altura e o peso calcular o imc e retornar para o usuario  o imc calculado
# e a categoria em que se encontra
# <18,5 abaixo do peso
# <24,9 peso normal  
# entre 25 e 29,9 sobrepeso
# igual ou maior q 30 obesidade


def calcular(peso,altura):
  imc = peso / (altura**2)
  return imc



def determinar(imc):
    if imc < 18.5:
        categoria = "abaixo do peso"
    elif imc < 24.9:
        categoria = "peso normal"
    elif imc > 29.9:
        categoria = "sobrepeso"
    else: 
        categoria = "obesidade"
    return categoria


peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura em metros: "))
imc = calcular (peso,altura)  


print ("seu imc é: ", imc)
print ("sua categoria é:", determinar(imc))



