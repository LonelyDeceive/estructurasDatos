edad = int(input("Edad/ "))
nombre = input("Nombre/ ")
cover = int(input("Cover? ($$)/ "))

if edad < 18 or cover < 50000:
    print('No se permite el ingreso')
else:
    print("Puede ingresar")
    print("Nombre: " , nombre, "\n"
          "Edad: " , edad, "\n"
          "Cover: $" , cover, sep="")
