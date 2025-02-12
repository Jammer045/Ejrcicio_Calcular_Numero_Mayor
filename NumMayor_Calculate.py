# Solicitar al usuario que ingrese tres números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

# Encontrar el número más pequeño usando la función min()
mas_pequeno = min(num1, num2, num3)

# Imprimir el resultado
print(f"El número más pequeño es: {mas_pequeno}")