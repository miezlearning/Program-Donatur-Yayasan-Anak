import os
import readchar

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu(menu, selected_index):
    clear_screen()
    print("Selamat datang")
    for i, item in enumerate(menu):
        if i == selected_index:
            print(f"> {item}")
        else:
            print(f"  {item}")

def menu_login():
    menu = ["Login", "Register", "Forgot Account", "Exit"]
    selected_index = 0

    print_menu(menu, selected_index)

    while True:
        key = readchar.readkey()
        if key == readchar.key.UP:
            selected_index = (selected_index - 1) % len(menu)
            print_menu(menu, selected_index)
        elif key == readchar.key.DOWN:
            selected_index = (selected_index + 1) % len(menu)
            print_menu(menu, selected_index)
        elif key == readchar.key.ENTER:
            if selected_index == 0:
                login()
            elif selected_index == 1:
                register()
            elif selected_index == 2:
                forgot_account()
            elif selected_index == 3:
                break
            print_menu(menu, selected_index)

def login():
    clear_screen()
    print("Login function called")
    input("Press Enter to return to menu...")

def register():
    clear_screen()
    print("Register function called")
    input("Press Enter to return to menu...")

def forgot_account():
    clear_screen()
    print("Forgot Account function called")
    input("Press Enter to return to menu...")

if __name__ == "__main__":
    menu_login()
