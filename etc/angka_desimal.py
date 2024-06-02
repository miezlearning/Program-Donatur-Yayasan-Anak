import curses

def main(stdscr):
    curses.curs_set(1)  # Show the cursor
    stdscr.clear()
    stdscr.addstr(0, 0, "Enter number: ")
    
    input_str = ""
    
    while True:
        key = stdscr.getch()
        
        if key in (curses.KEY_BACKSPACE, 127, 8):
            input_str = input_str[:-1]
        elif 48 <= key <= 57:  # If key is a number (0-9)
            input_str += chr(key)
        elif key == 27:  # Escape key to exit
            break

        # Remove non-digit characters (not necessary in this case as we only add digits)
        numeric_value = ''.join(filter(str.isdigit, input_str))
        
        # Format the number with commas
        if numeric_value:
            formatted_value = "{:,}".format(int(numeric_value))
        else:
            formatted_value = ""
        
        # Clear the input line and print the formatted value
        stdscr.move(1, 0)
        stdscr.clrtoeol()
        stdscr.addstr(1, 0, formatted_value)
        stdscr.refresh()

curses.wrapper(main)
