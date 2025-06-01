try:
    from pyautogui import press, hotkey, moveTo, size
except Exception:
    pass

from rich.console import Console
from time import sleep
from os import system
from platform import system as os    # Named 'os' to avoid confusion with 'system'
import cursor

console = Console(highlight = False)    # Initializes the Console() func

class InputError(Exception):
    '''
    Custom error for use in *inputHandler()*, as well as in functions used as parameters within it.

    This error object is imported separately from *cli_tools*, and is not included with *inputHandler*.
    '''

# Properly clears the screen on any terminal/console, unlike console.clear()
def clear(clear_lines = 0):
    '''
    Clears the console or terminal. Should work for all major OS types.

    Can also clear a given number of lines(from bottom to top), using the *clear_lines* parameter.
    '''

    if clear_lines > 0:
        print("\033[A\033[K" * clear_lines, end = "\r")
    else:
        if "Windows" in os():
            system('cls')
        else:
            system('clear')

def toggleFullscreen():
    '''
    Attempts to automatically toggle fullscreen and move the mouse cursor out of sight.

    If, for **any** reason, it fails to perform this, it prompts the user to do it themselves.
    '''

    try:
        screen_width, screen_height = size()
        moveTo(screen_width - 2, screen_height - 2)    # Moves mouse cursor to bottom-right corner
        
        if "Darwin" in os():
            hotkey("ctrl", "command", "f")
        else:
            press("f11")
            
    except Exception:
        cursor.hide()
        console.input("[orange1][dim]>>>[/dim] [b]PRESS [i]F11/CTRL+CMD+F[/i] TO TOGGLE FULLSCREEN MODE, AND THEN PRESS [i]ENTER[/i] TO CONTINUE ... [/b][/orange1]")
        print()

# Reusable error handling function for both input and function call, function parameters are passed through **kwargs
def inputHandler(
        prompt, func, *,
        style = "orange1", error_style = "orange_red1", input_type = int, allow_negatives = False,
        input_arg_name = "user_input", char_limit = "line", **kwargs):
    
    '''The **greatest** input-error-handling function to exist (probably).'''

    cursor.show()
    prompt = prompt[:console.width - 3]

    def clearErrorMsg():
        first_input_line = console.width - (len(prompt) + 3)
        if first_input_line <= len(str(user_input)) < console.width:    # Accounts for disrepancy in width of 1st line
            print("\033[A\033[K" * 3, end = "\r")
        else:
            # Clears all lines used for inputting and error msg, moves cursor back to start new input line at same place
            print("\033[A\033[K" * (3 + (len(str(user_input)) - first_input_line) // console.width) , end = "\r")
    
    if char_limit == "line":
        char_limit = console.width - len(prompt) - 4    # Actual console width from insertion point - 1 char

    while True:
        try:
            user_input = console.input(f"[{style}][dim]>>[/dim] {prompt}[/{style}]")

            if len(user_input) > char_limit:
                if char_limit == (console.width - len(prompt) - 4):
                    raise InputError("Input cannot exceed or equal the length of the line!")
                else:
                    raise InputError(f"Input cannot exceed {char_limit} characters!")
                
            user_input = input_type(user_input)

            if (input_type == int or input_type == float) and not allow_negatives and user_input < 0:    # Substantiates allow_negatives
                raise ValueError
            
            return func(**{input_arg_name: user_input}, **kwargs)
        
        except ValueError:    # Handles invalid inputs, also handles empty inputs
            cursor.hide()
            console.print(f"[{error_style}][dim]//[/dim] Invalid input![/{error_style}]")
            sleep(1.5)
            clearErrorMsg()   # Clears error msg and prev input, moves cursor back to start of line
            cursor.show()

        except InputError as e:    # Handles invalid function calls, e.g. drawing more cards than available in iter
            cursor.hide()
            console.print(f"[{error_style}][dim]//[/dim] {e}[/{error_style}]", no_wrap = True)
            sleep(2)
            clearErrorMsg()
            cursor.show()

# Premade func for simply giving user_input as the val of inputHandler()
def assignInputToVar(user_input, valid_choices = (), invalid_choices = ()):    # choice kwargs default to empty tuples
    '''
    Function to be used in conjunction with *inputHandler()*.

    Helps in doing what the name says, by directly returning user input.

    Can filter out invalid inputs using the *valid_choices* and *invalid_choices* parameters.
    '''
    
    # Note: If a choice arg is a dict, only the keys will be accessed. For accesing values, format as tuple(dict.values()) 
    if (valid_choices != ()) and user_input not in valid_choices:
        if len(str(user_input)) > console.width // 1.5:
            raise InputError(f"{str(user_input)[:int(console.width // 1.5)]}... is invalid to enter!")
        else:
            raise InputError(f"{user_input} is invalid to enter!")
    
    for i in invalid_choices:    # Choice args can be set to any kind of iterable
        if user_input == i:
            raise InputError(f"{i} is invalid to enter!")
    
    return user_input
