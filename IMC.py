
def obter_nome():
    while True:
        nome = input("Como você se chama: ")
        if nome.replace(" ", "").isalpha():
            return nome
        print("Digite um nome válido.")

def obter_altura():
    while True:
        altura = input("Escreva sua altura (ex: 1.75 ou 1,75): ")
        
        # Permite tanto ponto quanto vírgula
        altura = altura.replace(",", ".")  # Substitui vírgula por ponto
        if altura.count(".") == 1 and altura.replace(".", "").isdigit():
            altura = float(altura)
            if altura > 0:
                return altura
        
        print("Digite uma altura válida (ex: 1.75 ou 1,75).")

def obter_peso():
    while True:
        peso = input("Escreva seu peso: ")
        
      
        peso = peso.replace(",", ".")  
        if peso.replace(".", "", 1).isdigit() and peso.count(".") <= 1:
            peso = float(peso)
            if peso > 0:
                return peso
        
        print("Digite um peso válido")

print("Bem-vindo à Calculadora de IMC")
nome = obter_nome()
altura = obter_altura()
peso = obter_peso()

IMC = int(peso / (altura ** 2))
print(f"Olá {nome}, seu IMC é {IMC:.2f}")

# Classificação do IMC
if IMC < 16:
    print("Seu peso está muito abaixo, procure ajuda médica.")
elif IMC < 17:
    print("Seu peso está um pouco abaixo.")
elif IMC < 18.5:
    print("Seu peso está abaixo do normal.")
elif IMC < 25:
    print("Seu peso está normal.")
elif IMC < 30:
    print("Sobrepeso, se cuide.")
elif IMC < 35:
    print("Obesidade 1, procure ajuda médica.")
elif IMC < 40:
    print("Obesidade 2 (grave), procure ajuda médica.")
else:
    print("Obesidade 3 (severa), procure ajuda médica.")
