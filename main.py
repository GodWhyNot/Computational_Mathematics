import Gauss_Method
import Ortho_Method
import Some_func


def main():
    choice = input("Please choose the method you want to use: \n"
                   "1. Gauss Method\n"
                   "2. Orthogonal Method\n"
                   "3. Some_func\n"
                   "4. Exit\n"
                   "Your choice: ")
    if choice == "1":
        Gauss_Method.Gauss_Method()
        main()
    elif choice == "2":
        Ortho_Method.Ortho_Method()
        main()
    elif choice == "3":
        Some_func.Some_func()
        main()
    elif choice == "4":
        exit()
    else:
        print("Invalid choice")
        main()


main()
