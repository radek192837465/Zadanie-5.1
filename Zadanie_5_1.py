import random

def guess_the_number():
    print("Witaj w grze 'Guess the Number'!")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Zgadnij liczbę od 1 do 100: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Liczba musi być w przedziale od 1 do 100. Spróbuj ponownie.")
            elif guess < number_to_guess:
                print("Za niska! Spróbuj ponownie.")
            elif guess > number_to_guess:
                print("Za wysoka! Spróbuj ponownie.")
            else:
                print(f"Gratulacje! Zgadłeś liczbę {number_to_guess} w {attempts} próbach.")
                break
        except ValueError:
            print("Nieprawidłowa wartość. Proszę podać liczbę całkowitą.")

if __name__ == "__main__":
    guess_the_number()
