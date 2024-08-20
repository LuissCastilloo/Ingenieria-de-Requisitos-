def verificar_mayor_o_menor():
    valor1 = float(input("Ingrese el valor 1: "))
    valor2 = float(input("Ingrese el valor 2: "))
    if valor1 == valor2:
        return "Son iguales"
    elif valor1 > valor2:
        return "El valor 1 es el mayor"
    else:
        return "El valor 2 es el mayor"
    
print(verificar_mayor_o_menor())