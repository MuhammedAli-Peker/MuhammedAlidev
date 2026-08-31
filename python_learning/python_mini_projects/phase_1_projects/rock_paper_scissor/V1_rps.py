import random
#freecodecamp version:
def get_choices():
    player_choice=input("Please, enter a choice(rock paper or scissor): ").strip().lower()
    options=["rock","paper","scissor"]
    computer_choice=random.choice(options)
    choices={"Player": player_choice,"Computer": computer_choice}
    print(f"Player's choice: {player_choice} | Computer's choice: {computer_choice}")
    return choices

def check_winner(player,computer):
    if player==computer:
        return "I's tie!"
    elif player=="rock":
        if computer=="scissor":
            return "Rock beats scissor! Player won."
        else:
            return "Paper beats rock! Player lost"
    elif player=="paper":
        if computer=="rock":
            return "Paper beats rock! Player won."
        else:
            return "scissor beats paper! Player lost"   
    elif player=="scissor":
        if computer=="paper":
            return "Scissor beats papaer! Player won."
        else:
            return "Rock beats scissor! Player lost"

choices=get_choices()
result=check_winner(choices["Player"],choices["Computer"])
print(result)