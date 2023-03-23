#Ejemplo de un menú

num= int(input("menu: (numeros), 0 (salir) "))
while num !=0:

    x=0
    while x < 10:
        print("el valor de x es: ", x)
        x+=1

    print ("saliendo")
    num= int(input("menu: 1(numeros), 0 (salir) "))
    
print("gracias")