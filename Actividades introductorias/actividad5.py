# Implementa un programa que solicite al usuario que ingrese una lista de números.
# Luego, imprime la lista pero detén la impresión si encuentras un número negativo.
# Nota: utilice la sentencia break cuando haga falta

numeros = []
num = 0

while num != 999:
    num = int (input ("ingrese numeros (999 para finalizar carga): "))
    if num != 999:
        numeros.append(num)

for num in numeros:
    if num < 0:
        break
    print (num)
   
print (numeros)
