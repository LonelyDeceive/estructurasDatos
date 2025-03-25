def datos(data, data2):
    print("Datos")
    print(data, data2)
    a = data * 2
    b = data2 * 4
    datos2(a,b)

def datos2(data, data2):
    print("1.", data)
    print("2.", data2)
    c = data + data2
    datos3(c)

def datos3(data):
    print("Total", data)

num = datos(1,2)

print("")

