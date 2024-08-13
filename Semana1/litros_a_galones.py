def litros_a_galones():
    litros = float(input("Ingrese su produccion de leche (litros): "))
    galones = litros / 3.785
    return f"Su produccion del dia de hoy en galones es de {galones}"

print(litros_a_galones())