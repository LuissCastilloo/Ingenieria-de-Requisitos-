def metros_a_pulgadas():
    metros = float(input("Ingrese la cantidad de metros que necesita: "))
    pulgadas = metros/0.0254
    return f"la cantidad que debe pedir son {pulgadas} pulgadas"

print(metros_a_pulgadas())