my_first_variable = 1

''' \a - dźwięk systemu
    \t - tabulacja
    \n - nowa linijka
    \' - pisanie apostrofu
    \" - pisanie cudzysłowiu

    int - liczby całkowite
    float - rzeczywiste
    str - łańcuchy znaków
    bool - zmienne binarne '''

print("'hemlo worlmd'")

number_of_dogs = 101
print(number_of_dogs, "dalmatyńczyków", "\ndo końca życia i", my_first_variable, "dzień dłużej")

print("ile masz piesków?")
dogs_count = input()
print("masz", dogs_count, "piesków!")

''' to jest to samo co
    dogs_count = input("ile masz piesków?")
    print("masz", dogs_count, "piesków!") '''

print("cześć, jestem programem-figlarzem. Dodaję do Twojej liczby dwa.")
print("podaj swoją liczbę")
user_number = input()
print("nowa liczba to", int(user_number) + 2) #ważne jest int, bo trzeba zaznaczyć, że to jest liczba
