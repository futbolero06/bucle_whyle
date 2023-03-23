# programa para sumar los primeros numeros naturales

print("----------------")
#input

n=int(input("digite la cantidad de numeros naturales: "))

suma=0
i=1

while (i<=n):
    suma=suma+i
    i=i+1

print("la suma es: " + str(suma))