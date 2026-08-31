import random
options = ["rock","scissor","paper"]
#oyuncu girdisi
def get_player_choice():
    while True:
        player_choice = input("Please, enter:(rock, scissor or paper): ").strip().lower()
        if player_choice not in options:
            print("İnvlaid option, please enter: rock, scissor or paper ")
        else:
            return player_choice

#bilgisayar sayi belirler       
def get_computer_choice():
    return random.choice(options)

#kazanan ve kaybeden belirlenir
def get_winner():
    while True:
        player = get_player_choice()
        computer = get_computer_choice()
        print(f"[Computer chose: {computer}]")
        if player==computer:
            print("It's tie! there is no winner.")
            return "it's tie"
        elif player=="rock":
            if computer=="scissor":
                print("Rock beats scissor. Player WON!")
                return "player"
            else:
                print("Paper beats rock. Computer WON!")
                return "computer"
        elif player=="scissor":
            if computer=="paper":
                print("Scissor  beats paper. Player WON!")
                return "player"
            else:
                print("Rock beats scissor. Computer WON!")
                return "computer"  
        elif player=="paper":
            if computer=="rock":
                print("Paper beats rock. Player WON!")
                return "player"
            else:
                print("Scissor beats paper. Computer WON!")
                return "computer"
   
#ana döngü ve skor tablosu

def main():
    print("\n---Welcome to Rock Scissor Paper Game---")
    print("-->if you reach five win, you will win the game! or else computer will win the game!")
    print("---------------")
    while True:     
        player_score = 0
        computer_score = 0
        total_tour = 1
        while True:
            print(f"\n---Round {total_tour}---")
            winner = get_winner()
            if winner == "it's tie":
                print("No winner for this round")
                total_tour+=1
            else:
                if winner == "player":
                    player_score+=1                    
                    total_tour+=1
                    print(f"Player won this round\n[Player: {player_score}|Computer: {computer_score}]")
                else:
                    computer_score+=1
                    total_tour+=1
                    print(f"Computer won this round\n[Player: {player_score}|Computer: {computer_score}]")
            if player_score == 5:
                print("---------------")
                print(f"Player won the game!\n[Player: {player_score} |Computer: {computer_score}]")
                print(f"Total round: {total_tour}")
                break
            elif computer_score == 5:
                print("---------------")
                print(f"Computer won the game!\n[Player: {player_score} |Computer: {computer_score}]")
                print(f"Total round: {total_tour - 1}")
                break
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again != "yes":
            print("Thanks for playing! goodbye.")
            break
        
        
if __name__ == "__main__" :
    main()