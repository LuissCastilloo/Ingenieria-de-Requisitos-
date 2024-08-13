def calcular_sueldo():
    salario_mensual = float(input("Ingrese su salario mensual: "))
    horas_semanales = float(input("Ingrese sus horas semanales trabajadas: "))
    horas_mensuales = float(input("Ingrese sus horas mensuales trabajadas: "))
    pago_por_hora = salario_mensual / horas_mensuales
    sueldo_semanal = pago_por_hora * horas_semanales
    
    return f"Su sueldo semanal es {sueldo_semanal}$ y su pago por hora trabajada es de {pago_por_hora}$"

print(calcular_sueldo())