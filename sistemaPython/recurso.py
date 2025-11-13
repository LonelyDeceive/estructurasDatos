class Recurso:
    def __init__(self, id_proceso, ram, disco, cpu, vram):
        self.id = id_proceso
        self.ram = ram
        self.disco = disco
        self.cpu = cpu
        self.vram = vram
    
    def __str__(self):
        if self.vram == 0:
            return f"Ram: {self.ram} GB | Disco: {self.disco} GB | Cpu: {self.cpu} %"
        return f"Ram: {self.ram} GB | Disco: {self.disco} GB | Cpu: {self.cpu} % | [VRam: {self.vram}]"
    
class RecursosDisponibles:
    def __init__(self):
        self.ram = 4
        self.vram = 4
        self.disco = 25
        self.cpu = 0
        
    def liberar(self, recurso):
        self.ram = self.ram + recurso.ram
        self.vram = self.vram + recurso.vram
        self.disco = self.disco + recurso.disco
        self.cpu = self.cpu - recurso.cpu
         
    def usedVRam(self, ram) -> float:
        return ram - float(self.ram)
        
    def reFree(self, ram, PDisco, PCPU):
        VPram = self.usedVRam(ram)
        if float(self.ram) - ram >= 0:
            if float(self.disco) - PDisco >= 0:
                if float(self.cpu) + PCPU <= 100:
                    self.ram = float(self.ram) - ram
                    self.disco = float(self.disco) - PDisco
                    self.cpu = float(self.cpu) + PCPU
                    return True
                else:  
                    print("Uso de CPU supera el 100%")
                    return False
            else:
                print("No hay suficiente espacio de disco")
                return False
        elif float(self.vram)-(ram - float(self.ram)) >= 0:
            if float(self.disco) - PDisco >= 0:
                if float(self.cpu) + PCPU <= 100:
                    usedRam = ram - VPram
                    self.ram = usedRam - float(self.ram)
                    self.vram = float(self.vram) - VPram
                    self.disco = float(self.disco) - PDisco
                    self.cpu = float(self.cpu) + PCPU
                    print("Memoria RAM insuficente, usando memoria virtual")
                    return True
                else:  
                    print("Uso de CPU supera el 100%")
                    return False
            else:
                print("No hay suficiente espacio de disco")
                return False
        print("Memoria RAM y memoria virtual insuficiente")
        return False
    