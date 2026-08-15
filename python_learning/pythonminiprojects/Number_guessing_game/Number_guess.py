import random
prime_numbers = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
    31, 37, 41, 43, 47, 53, 59, 61, 67, 
    71, 73, 79, 83, 89, 97
]

#kullanicidan girdi aliyoruz:
def get_guess():
    while True:
        try:
            user_guess=int(input("Guess a number from (0-100): "))
            if 0 <= user_guess <= 100:
                return user_guess
            else:
                 print("Out of range!, please enter a number between 0 and 100")
        except ValueError:
            print("Please, enter a valid number from (0-100)")

#bilgisayardan sayi aliyoruz           
def get_number(mod):
        if mod == "standart":
            return random.randint(0,100)
        else:
            return random.choice(prime_numbers)
    
    
#mod seçimi    
def get_mode_choice():
    print("---Choose a game mode!---")
    print("1- Standart Mode (0-100)")
    print("2- Prime Numbers Mode (0-100)")
    while True:
        mode_choice=input("Enter your choice ( 1 or 2 ) ").strip()
        if mode_choice== "1":
            return  "standart"
        elif mode_choice== "2":
            print("--> Prime mode selected! The target number is a prime number.")
            return  "prime"
        else:
            print("İnvlaid choice! Please enter 1 or 2")

#zorluk seçimi
def difficulty_choice():
    print("\n---Choose A Difficulty---")
    while True:
        dif = input("Please chose a difficulty:\n-easy\n-medium\n-hard\n-> ").strip().lower()
        if dif == "easy":
            return 11
        elif dif == "medium":
            return 9
        elif dif == "hard":
            return 7
        else:
            print("İnvlaid difficulty level!please choose: easy, medium or hard.")   

#tahminin, bilgisayarin seçtiği sayıdan düşük mü büyük mü olduğu
def compare_guesses(user,computer):

    if user < computer:
        print("--------------")
        print("Enter a greater number!")
    else:
        print("--------------")
        print("Enter a less number!")

#mevcut yapilari birleştiriyoruz
def  play_game(given_attempts):
    mode = get_mode_choice()
    computer = get_number(mode)
    attempts = 0  
    guess_history = []
    while True:
        user  = get_guess()
        attempts+=1
        remaning_attemps = given_attempts - attempts
        guess_history.append(user)
        if user == computer:
            print(f"Congratulations, you guessed the number!\nNumber is: {computer}")
            print(f"You guesses so far: {guess_history}")
            return attempts
        else:
            compare_guesses(user,computer)
            print(f"Total used attemps: {attempts}\nRemaning attempts: {remaning_attemps}")
            print(f"You guesses so far: {guess_history}")
            print("--------------")
            if remaning_attemps==0:
                print(f"Game over! Correct number was: {computer}")
                print(f"Your final guesses: {guess_history}")
                return None


#Ana oyun döngüsü:
def main():
    best_score = None #en az deneme sayisi. başlangiçta yok
    while True:
        attempts_limit = difficulty_choice()
        result = play_game(attempts_limit)
        if result is not None:
            if best_score is None or best_score < result :
                best_score = result
                print(f"New Best score! you won in [{best_score} attempts]")
            else:
                print(f"Your score this round: [{result} attempts] \n---Best Score: [{best_score} attempts]")
        if best_score is not None:
            print(f"Your current best score(Least Attempts): [{best_score}]")
            
        play_again = input("\nDo you want to play again?(yes/no) ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! goodbye.")
            break
        
        
if __name__ == "__main__":
    main()