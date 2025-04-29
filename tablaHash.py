class TablaHash:
    def __init__(self, size:int):
        self.hashLen = size
        self.hashT = [None] * self.hashLen

    def hashInum(self, name: str) -> int:
        hashVal = hash(name) % self.hashLen
        return hashVal

    def add(self, name: str, num: int) -> None:
        index = self.hashInum(name)
        if self.hashT[index] == None:
            self.hashT[index] = [(name, num)]
        else:
            self.hashT[index].append((name, num))

    def search(self, name: str) -> None:
        index = self.hashInum(name)
        nameFound = True
        if self.hashT[index] != None:
            for searchName, resultKey in self.hashT[index]:
                if searchName == name:
                    nameFound = True
                    print("Numero de",searchName,":",resultKey)
            if nameFound == False:
                print("No se encuentra el numero de",name)
        elif self.hashT[index] == None:
            print("No se encuentra el numero de",name)

    def dele(self, name: str) -> None:
        index = self.hashInum(name)
        if self.hashT[index] != None:
            for i, (n, t) in enumerate(self.hashT[index]):
                if n == name:
                    print("Se ha eliminado",name,"con numero", t)
                    del self.hashT[index][i]
        else:
            return print(f"Contacto '{name}' no encontrado.")

    def listAll(self) -> None:
        print("\nDirectorio Actual")
        for searchIt in self.hashT:
            if searchIt != None:
                for resname, resnum in searchIt:
                    print(f"Nombre: {resname}, Teléfono: {resnum}")

tamañoTabla = 10
dir = TablaHash(tamañoTabla)
dir.add("Jhon", 315781451)
dir.add("William", 3008715512)
dir.add("Sofia", 312487952)
dir.search("Jhon")
dir.search("William")
dir.search("Sofia")
dir.dele("William")
dir.search("William")
dir.listAll()