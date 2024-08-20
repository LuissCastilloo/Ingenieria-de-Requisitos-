def pago_por_consumo():
    altura = float(input("Ingrese la altura de la alberca: "))
    ancho = float(input("Ingrese el ancho de la alberca: "))
    largo = float(input("Ingrese el largo de la alberca: "))
    costo_metro_cubico = float(input("Ingrese el costo del metro cubico: "))
    
    volumen_alberca = altura * ancho * largo
    pago = volumen_alberca * costo_metro_cubico
    return f"Su pago por {volumen_alberca}m^3 es de {pago}$"

print(pago_por_consumo())