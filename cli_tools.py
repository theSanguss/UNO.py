try:
    import pyautogui
except Exception:
    pass

from rich.console import Console
from time import sleep
import cursor
import sys

console = Console(highlight = False)    # Initialises the Console object/instance

class InputError(Exception):
    '''
    Custom error for use in *inputHandler*, as well as in functions used as parameters within it.

    This error object is imported separately from *cli_tools*, and is not included with *inputHandler*.
    '''

# Properly clears the screen on any terminal/console, unlike console.clear()
def clear(clear_lines = 0):
    '''
    Clears the console or terminal. Should work for all major OS types.

    Can also clear a given number of lines(from bottom to top), using the *clear_lines* parameter.
    '''

    if clear_lines == 0:
        sys.stdout.write("\033[2J\033[3J\033[H")    # ANSI escape code to clear screen & scrollback history, then move cursor to top-left corner
        sys.stdout.flush()
    else:
        sys.stdout.write("\033[A\033[K" * clear_lines)
        sys.stdout.write("\r")
        sys.stdout.flush()

def toggleFullscreen(move_cursor_to_centre = False):
    '''
    Attempts to automatically toggle fullscreen and move the mouse cursor out of sight.

    If, for some unknown reason, it fails to perform this, it prompts the user to do it themselves.
    '''

    try:
        pyautogui.FAILSAFE = False
        pyautogui.PAUSE = 0.025
        screen_width, screen_height = pyautogui.size()
        
        if not move_cursor_to_centre:
            pyautogui.moveTo(screen_width, screen_height // 2)    # Moves mouse cursor to bottom-right corner
        else:
            pyautogui.moveTo(screen_width // 2, screen_height // 2)    # Moves it to centre of screen

        if sys.platform == "darwin":
            pyautogui.hotkey("ctrl", "command", "f")
        else:
            pyautogui.press("f11")
            
    except Exception:
        cursor.hide()
        console.input("[orange1][dim]>>>[/dim] [b]PRESS [i]F11/CTRL+CMD+F[/i] TO TOGGLE FULLSCREEN MODE, AND THEN PRESS [i]ENTER[/i] TO CONTINUE ... [/b][/orange1]")
        clear()

# Reusable error handling function for both input and function call, function parameters are passed through **kwargs
def inputHandler(
        prompt: str, func, *,
        style = "orange1", error_style = "orange_red1", input_type = int, allow_negatives = False,
        input_arg_name = "user_input", char_limit: int | str = "line", min_line_limit = 9, **kwargs):
    
    '''
    Versatile input-handling/input-sanitising function.
    
    Designed to be mostly reusable in other CLI-based programs.
    '''

    cursor.show()
    prompt = (">> " + prompt).expandtabs()[:console.width - 1]    # Though adding ">> " is redundant, it helps expandtabs align to tab stops accurately 
    char_limit_is_line = False
    
    if char_limit == "line":
        char_limit = console.width - len(prompt) - 1
        
        if char_limit < min_line_limit:    # Sets the char limit to a fixed min val if line is too short
            char_limit = min_line_limit
        else:    # 'else' is used here since the line error msg(Ln 99) is no longer accurate if above condition is true
            char_limit_is_line = True

    while True:
        try:
            user_input = console.input(f"[{style}][dim]>>[/dim] {prompt[3:]}[/{style}]")    # ">> " in prompt str ignored
            input_len = len((prompt + user_input).expandtabs()) - len(prompt)

            if input_len > char_limit:
                if char_limit_is_line:
                    raise InputError("Input cannot exceed or equal the length of the line!")
                else:
                    raise InputError(f"Input cannot exceed {char_limit} character{'s' if char_limit != 1 else ''}!")
                
            user_input = input_type(user_input)    # 'input_type' param is a func like int, str, float, etc.

            if (input_type == int or input_type == float) and not allow_negatives and user_input < 0:    # Substantiates allow_negatives
                raise ValueError
            
            return func(**{input_arg_name: user_input}, **kwargs)
        
        except ValueError:    # Handles invalid inputs, also handles empty inputs
            cursor.hide()
            console.print(f"[{error_style}][dim]//[/dim] Invalid input![/{error_style}]")
            sleep(1.5)
            clear(3 + (input_len - (console.width - len(prompt))) // console.width)    # Clears all input & error msg lines, moves cursor to orig pos for new input
            cursor.show()

        except InputError as e:    # Handles invalid function calls, e.g. drawing more cards than available in iter
            cursor.hide()
            console.print(f"[{error_style}][dim]//[/dim] {e}[/{error_style}]", no_wrap = True)
            sleep(2)
            clear(3 + (input_len - (console.width - len(prompt))) // console.width)
            cursor.show()

# Premade func for simply giving user_input as the val of inputHandler
def assignInputToVar(user_input, valid_choices = (), invalid_choices = ()):    # choice kwargs default to empty tuples
    '''
    Function to be used in conjunction with *inputHandler*.

    Helps in doing what the name says, by directly returning user input.

    Can filter out invalid inputs using the *valid_choices* and *invalid_choices* parameters.
    '''
    
    # Note: If a choice arg is a dict, only the keys will be accessed. For accesing values, format as tuple(dict.values()) 
    if len(valid_choices) != 0 and (user_input not in valid_choices):
        if len(("// \" " + str(user_input)).expandtabs()) > console.width // 1.5:
            raise InputError(f"\" {('// \" ' + str(user_input)).expandtabs()[5:int(console.width // 1.5)]} ... \" is invalid to enter!")
        else:
            raise InputError(f"\" {user_input} \" is invalid to enter!")
    
    for i in invalid_choices:    # Choice args can be set to any kind of iterable
        if user_input == i:
            raise InputError(f"\" {i} \" is invalid to enter!")
    
    return user_input
