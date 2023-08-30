#Monte uma função que recebe um salário por hora e o número de horas trabalhadas no mês, e retorne o salário a ser recebido.

def calcular_salario(hr_trab, sal_hr):
    salario = hr_trab * sal_hr
    return salario

salariohora = float(input('Digite o valor do seu salário por hora: '))
hora_trabalho = float(input('Digite o valor de quantas horas trabalhadas: '))

salario_total = calcular_salario(hora_trabalho, salariohora)

print('O salário a ser recebido é:', salario_total)

#Elabore uma função que receba três números e exiba na tela: (1) o produto do dobro do primeiro com metade do segundo; (2) a soma do triplo do primeiro com o terceiro; e (3) o terceiro elevado ao cubo.
print('-'*60)

def calculos(num1, num2, num3):
    cal1 = (num1 * 2) * (num2/2)
    cal2 = (num1 * 3) + num3
    cal3 = num3 ** 3

    print("Produto do dobro do primeiro com metade do segundo:", cal1)
    print("Soma do triplo do primeiro com o terceiro:", cal2)
    print("Terceiro elevado ao cubo:", cal3)

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

calculos(num1, num2, num3)

#Elabore uma função com as mesmas regras do exercício anterior, porém retornando os três resultados, ao invés de exibi-los na tela.
print('-'*60)

def calc(nume1, nume2, nume3):
    resul1 = (2 * nume1) * (nume2 / 2)
    resul2 = (3 * nume1) + nume3
    resul3 = nume3 ** 3

    return resul1, resul2, resul3

nume1 = float(input("Digite o primeiro número: "))
nume2 = float(input("Digite o segundo número: "))
nume3 = float(input("Digite o terceiro número: "))

resultados = calc(nume1, nume2, nume3)

print("Resultado 1:", resultados[0])
print("Resultado 2:", resultados[1])
print("Resultado 3:", resultados[2])



print('-'*30)

def bis(ano):
    resultado = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    return resultado

ano = int(input("Digite um ano: "))

resultado = bis(ano)
print('É um ano bissexto?', resultado)