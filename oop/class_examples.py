class DriversLicense:
    def __init__(self, name, age): 
        self.age = age
        self.name = name
        
    def check_age(self):
        
        if self.age >= 18: 
            return f"Olá, {self.name}, você está apto(a) a tirar a CNH"
        else: 
            return f"Olá, {self.name}, você não está apto(a) a tirar a CNH"
        
cnh = DriversLicense("Camila", 17)

print(cnh.name)
print(cnh.age)

print(cnh.check_age())

## Conceito de class child ou subclasse.

class CheckCPF(DriversLicense):
    pass

# cnh = CheckCPF("Camila", 15)
# print(cnh.check_age())






        
        