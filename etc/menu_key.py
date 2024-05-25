import curses

def main(stdscr):
    stdscr.clear()

    # Daftar opsi menu
    options = ["Opsi 1", "Opsi 2", "Opsi 3", "Keluar"]

    current_row = 0

    while True:
        stdscr.clear()

        for i, option in enumerate(options):
            if i == current_row:
                stdscr.addstr(i, 0, "> " + option, curses.A_REVERSE)
            else:
                stdscr.addstr(i, 0, "  " + option)

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(options) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == len(options) - 1:  # Keluar dari program
                break
            else:
                stdscr.clear()
                stdscr.addstr(f"Anda memilih {options[current_row]}")
                stdscr.getch()  # Menunggu pengguna menekan tombol

# Menjalankan program
curses.wrapper(main)