def calcular_area():
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))
    
    area_rectangulo = b * c
    area_triangulo = ((a-c)*(b))/2
    area_total = area_rectangulo + area_triangulo
    return area_total

print(calcular_area())