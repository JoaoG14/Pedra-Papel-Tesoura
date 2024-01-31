import random

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["pedra", "tesoura", "papel"]
    user_input = input("Escolha pedra, papel, tesoura ou sair: ")
    computer_input = random.choice(options)

    if user_input == "sair":
        print("Jogo encerrado")
        print("Você ", user_points, "x", computer_points, " Computador")
        exit = True
        

    

    if user_input == "papel":
        if computer_input == "pedra":
            print("Você escolheu papel")
            print("O computador escolheu pedra")
            print("Você venceu")
            user_points += 1
        if computer_input == "papel":
            print("Você escolheu papel")
            print("O computador escolheu papel")
            print("Empate")
        if computer_input == "tesoura":
            print("Você escolheu papel")
            print("O computador escolheu tesoura")
            print("O computador ganhou")
            computer_points += 1
        print("Você ", user_points, "x", computer_points, " Computador")
  

    if user_input == "tesoura":
        if computer_input == "pedra":
            print("Você escolheu tesoura")
            print("O computador escolheu pedra")
            print("O computador venceu")
            computer_points += 1
        if computer_input == "papel":
            print("Você escolheu tesoura")
            print("O computador escolheu papel")
            print("Você venceu")
            user_points += 1
        if computer_input == "tesoura":
            print("Você escolheu tesoura")
            print("O computador escolheu tesoura")
            print("Empate")
        print("Você ", user_points, "x", computer_points, " Computador")
    
    
    if user_input == "pedra":
        if computer_input == "pedra":
            print("Você escolheu pedra")
            print("O computador escolheu pedra")
            print("Empate")
        if computer_input == "papel":
            print("Você escolheu pedra")
            print("O computador escolheu papel")
            print("O computador venceu")
            computer_points += 1
        if computer_input == "tesoura":
            print("Você escolheu pedra")
            print("O computador escolheu tesoura")
            print("Você venceu")
            user_points += 1
        print("Você ", user_points, "x", computer_points, " Computador")
 
         
