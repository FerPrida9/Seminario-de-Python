# Escribe un programa que tome una lista de números enteros como entrada del usuario.
# Luego, convierte cada número en la lista a string y únelos en una sola cadena,
# separados por guiones ('-'). Sin embargo, excluye cualquier número que sea múltiplo
# de 3 de la cadena final.

listaNumeros = []
cadena = ""
num = 0

while num != 9999:
    num = int (input ("ingrese numeros (9999 para finalizar): "))
    if (num != 9999):
        listaNumeros.append (num)

for num in listaNumeros:
    if num % 3 != 0:
        cadena = cadena + str(num) + "-"

print (cadena)


    


