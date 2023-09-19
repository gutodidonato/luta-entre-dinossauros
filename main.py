import random 
from logo import logo           


nomes_dinossauros = [
    "Tyrannosaurus rex",
    "Spinosaurus",
    "Giganotosaurus",
    "Carcharodontosaurus",
    "Allosaurus",
    "Brachiosaurus",
    "Triceratops",
    "Ankylosaurus",
    "Stegosaurus",
    "Apatosaurus",
]

forca_dinossauros = [
    900,  
    800,  
    750,  
    700,  
    700,  
    600,  
    400, 
    400,  
    400,  
    600,  
]

#valores aleatórios dentro da lista 
def valor_aleatorio(lista):
    aleatorio = random.randint(0,len(lista) - 1)
    return aleatorio

#f string para evitar ficar escrevendo
def chamar_dinossauro(indice):
    return print(f"O poderoso {nomes_dinossauros[indice]}") 

#partida emblocada
def partida(vida, pontos):
    dinossauro1 = valor_aleatorio(nomes_dinossauros)
    dinossauro2 = valor_aleatorio(nomes_dinossauros)
    while dinossauro2 == dinossauro1:
        dinossauro2 = valor_aleatorio(nomes_dinossauros)
    chamar_dinossauro(dinossauro1)
    print("Versus")
    chamar_dinossauro(dinossauro2)
    print("\n \n")
    chute = int(input(f"Quem é mais forte? {nomes_dinossauros[dinossauro1]} ou {nomes_dinossauros[dinossauro2]}, vote com 1 ou 2 \n "))
    if (chute == 1 and forca_dinossauros[dinossauro1] > forca_dinossauros[dinossauro2]) or (chute == 2 and forca_dinossauros[dinossauro2] > forca_dinossauros[dinossauro1]):
        print("Acertou")
        pontos += 1
        print(f"Você tem {vida} de vida e {pontos} de pontos \n\n")
    elif (chute == 1 and forca_dinossauros[dinossauro1] < forca_dinossauros[dinossauro2]) or (chute == 2 and forca_dinossauros[dinossauro2] < forca_dinossauros[dinossauro1]):
        print("Errou")
        vida -= 1
        print(f"Você tem {vida} de vida e {pontos} de pontos \n\n")
    else:
        print("empate \n\n\n")
        print(f"Você tem {vida} de vida e {pontos} de pontos \n\n")
    continuar = input("Deseja continuar? ")
    if continuar == "sim" or continuar == "s":
        partida(vida,pontos)
    
    
    

#escopo do jogo
def jogo_dinossauros():
    print(logo)
    vida = 3
    pontos = 0
    print("Bem vindo ao jogo de força dos dinossauros")
    partida(vida, pontos)

jogo_dinossauros()
    
    
    