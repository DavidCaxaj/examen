#Jeremy Vinicio Perdomo Valencia
#202308008

def operacion_numerica(numero):
    numero_operando = 1
    potenciacion = 2
    operacion = 0
    if numero<2 or numero>8:
        return 0
    else:
        for i in range(1,numero+1):
            operacion += numero_operando**potenciacion
            numero_operando+=1
            potenciacion+=1
    return operacion

numero = int(input("ingrese un numero mayor o igual a dos o menor igual a 8"))

resultado = operacion_numerica(numero)

print("el resultado es: ",resultado)
