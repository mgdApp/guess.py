import random

def main():
    print("—> Adivina el número <—\n")

    print("Se ha generado un número aleatorio entre 1 y 100, ¡intenta adivinarlo!")

    random_number = random.randint(1, 100)

    while True:

        user_number = int(input("\nIngresa un número: "))


        if user_number == random_number:
            print("¡Adivinaste el número!\n")
            break
        elif user_number > random_number:
            print(f"El número generado es menor que {user_number}.")
        elif user_number < random_number:
            print(f"El número generado es mayor que {user_number}.")
        else:
            print("Ingresa un número correcto.")

    try_again = input("¿Quieres jugar otra vez? [Y/N]: ")

    if try_again == "Y":
        print("----------------------------------------------------------------------")
        main()
    elif try_again == "N":
        print("\n¡Hasta luego!")
    else:
        print("Coloca una opción correcta la próxima vez.")

if __name__ == "__main__":
    main()