![Logo](/UNO_icon_new.ico)

<br>

- 🚀 _My first OOP Python project, as well as my first GitHub repository! (ignoring config repo)_
- 🎮 _Singleplayer turn-based card game with AI opponents._
- 📟 _Runs within the terminal, is lightweight in code, and uses a CLI combined with a TUI._
- 🐍 _Made with Python (version 3.12)._

<br>

> [!Note]\
> Despite its name, UNO.py is not a single script, but rather a collection of various modules, with the name being chosen purely for stylistic reasons.

<br>

![Setup Screen](/README%20Images/setup_screen.png)

![UI rich in Rich formatting](/README%20Images/variety_of_cards_in_hand.png)

<br>

## How to run?

Enter the following command in your terminal, in order to **clone the repository and run UNO.py**:

```bash
curl -fsSL "https://raw.githubusercontent.com/theSanguss/UNO.py/main/install.sh" | bash
```

**In case UNO.py didn't run successfully when initiated by the command above** (unsure as to why this happens), just execute the two commands below:

```bash
cd UNO.py
python main.py
```

**To rerun UNO.py**, ensure the working directory of your terminal (the folder your terminal is currently accessing) is the UNO.py repository folder, and enter the following command:

```bash
python main.py
```

**If you want a portable and easy-to-run version of the game**, just download and run one of the two Windows EXE files available in this repository – `UNO.py.exe` or `UNO-WOE.py.exe` (WOE stands for Windows-Optimised Edition). While the former has been created using the same code you see in this repository, the latter uses a slightly different version of the `toggleFullscreen` function defined in `cli_tools.py`, making use of the [keyboard](https://github.com/boppreh/keyboard/) and [mouse](https://github.com/boppreh/mouse/) libraries as a replacement to the [PyAutoGUI](https://github.com/asweigart/pyautogui/) library, as these two libraries are significantly more lightweight, reducing the time it takes to load UNO.py. [Click here](#6-what-code-was-modified-in-uno-woepyexe-aside-from-the-new-imports) to see the code that was modified.

**If you are not a Windows user, but still wish to get an executable file version of UNO.py**, you can use [PyInstaller](https://github.com/pyinstaller/pyinstaller/) to make it yourself. For more info on how to use this tool to make an UNO.py executable, [refer to the second-to-last question in the FAQ section](#5-how-can-i-convert-this-into-an-executable-file-myself-using-pyinstaller).

> [!Note]\
> This program has been tested to work on MacOS and Linux, but certain issues like the the automatic toggling of fullscreen mode still persist. So for the time being, users on systems hostile to [PyAutoGUI](https://github.com/asweigart/pyautogui/) (one example being Linux users using Wayland instead of X11) will have to make do with toggling fullscreen mode manually.
>
> Please do file an issue if you encounter anything unexpected or problematic, especially if you're not a Windows user.

<br>

## How to operate?

This is a CLI-based application, so entering in short inputs as commands and pressing _Enter_ when prompted to is all you really need to do, save for prematurely exiting the program (by pressing _Ctrl+C_).

All available inputs, as well as other important prerequisites, are specified within the Instructions displayed in the Setup Screen which appears upon running UNO.py.

> [!Warning]\
> If your system has a custom keybind for toggling fullscreen mode, that isn't _F11_ (or _Control+Command+F_ if you're using MacOS), **make sure to revert it back to the default keybind when running this program**, or instead modify the `toggleFullscreen` function in `cli_tools.py`. **Unintended results may occur if the _F11_ key/_Control+Command+F_ key combination is modified to serve a different purpose**.

<br>

![UNO! declared & turn order reversed](/README%20Images/declared_uno_and%20reversed_turn_order.png)

![Victory Screen](/README%20Images/lesgo_i_win.png)

<br>

# FAQs :

## 1. Are the rules the same as normal UNO?

Yes, except for two minor rules - viewing the cards of the player you challenge (isn't necessary here, as this rule is useless outside of a real-life setting), and the score system (most people don't even know it exists, and I doubt anyone actually uses it). Stacking, 'jump-in's and other such house rules haven't been implemented, **but if you wish to contribute to this project, I highly suggest starting with adding functionality to the game loop for some of these to be available as custom rules during setup**.

<br>

## 2. Does this support local multiplayer?

No. Technically, this could be implemented by just adding multiple `Player` objects, but it would be impractical from a gameplay standpoint (imagine making every other human player face away from the screen when it's your turn). **Feel free to fork this project and try implementing a Local Multiplayer system you think would work well. Again, contributions are welcome.**

<br>

## 3. How does the UI work?

This project makes extensive use of the wonderful [Rich library](https://github.com/Textualize/rich/) for its UI, so much so that it can serve as a showcase for several of Rich's versatile components and how they can be meshed together! It is still fully text-based though, so maybe take a look at some of the tips below for better UI rendering:

> [!Tip]\
> For optimal results, ensure that the terminal you're using can properly render all the special Unicode characters used in UNO.py. Custom terminal backgrounds and colour schemes have no impact on the UI itself.
>
> Using Windows Terminal's default font size (12pt), or anything lower, is enough to get the proper UI experience, as it eliminates the need to ever scroll the UI on a standard display (16:9). If you are not using Windows Terminal, or have increased the font size, you may have to reduce it. However, this might only be an issue for you on the Setup Screen, so another thing you can do is replace line 30 of the file `uno.py` with `self.setup(show_instructions = False)`, so that the long Instructions list will no longer be displayed.

<br>

## 4. How does the AI in this work?

The AI players in this are biased by a numerical property called their 'intellect'. I say 'biased', as a large part of their logic is based on random chance, and intellect mostly serves to vary this chance. This intellect comes in use for the AI in nearly all aspects of play. In some cases, AIs with the lowest intellect are barred or dissuaded from making intelligent decisions, while those with the highest intellect can perform certain advanced strategies that AIs of lower intellect cannot. Looking at the code in `player.py` should give you a good idea of exactly how the AI players function and what the different tactics they can employ are.

<br>

## 5. How can I convert this into an executable file myself using PyInstaller?

If you're not already familiar with [PyInstaller](https://github.com/pyinstaller/pyinstaller/), it's a CLI tool that helps bundle Python scripts, modules and libraries into executable files. If you don't already have PyInstaller, run the following command to install it (make sure you have Python installed so that `pip` is recognised by your system):

```bash
pip install pyinstaller
```

Then, after cloning this repository and opening UNO.py's folder in the terminal, run the command below to generate the executable (make sure to replace `[insert filepath here]` with the filepath to Python's `site-packages` folder on your system):

```bash
pyinstaller --onefile --name="UNO.py" --icon="UNO_icon_new.ico" --add-data "[insert filepath here]\site-packages\pyfiglet\fonts;.\pyfiglet\fonts" main.py
```

After this, two new folders will be generated inside `UNO.py` - `build` and `dist`. The folder `build` can be ignored, as it is within the folder `dist` that the executable will be stored. The `--onefile` parameter in the above command creates a standalone executable file, which can be moved to any location in your system.

If you don't want the libraries to be bundled with the executable, and would prefer to run the executable from within the `dist` directory, rather than having it as a portable standalone, you can remove the `--onefile` parameter. This will also help decrease the time it takes for the program to actually start.

> [!Note]\
> The `--add-data` parameter is mandatory to include, as [Pyfiglet](https://github.com/pwaller/pyfiglet/), a Python library used with this project for displaying text in fancy multi-line ASCII fonts (termed as Figlet fonts), requires a filepath to be specified for it to be able to access its font files.
>
> `.ico` files are not supported as file icons on systems other than Windows, so you'll have to convert `UNO-icon-new.ico` to a different file format (like `.icns` for MacOS and `.png` for Linux) in order to use it with the `--icon` parameter.

> [!Warning]\
> This command hasn't been tested on other systems, and there is no guarantee that it will work for all users. However, this is the easiest method I know of which also resolves all issues with Pyfiglet, and has worked flawlessly for me, which is why I recommend using it.

<br>

## 6. What code was modified in `UNO-WOE.py.exe`, aside from the new imports?

```
def toggleFullscreen(move_cursor_to_centre = False):
    '''
    Automatically toggles fullscreen and moves the mouse cursor out of sight. (Windows-only)
    '''

    if move_cursor_to_centre:
        mouse.move(800, 450)
    else:
        mouse.move(9999, 9999)

    keyboard.press("f11")
    sleep(0.02)
```

As you can see, this code, which makes use of the [keyboard](https://github.com/boppreh/keyboard/) and [mouse](https://github.com/boppreh/mouse/) libraries, is incredibly simple as compared to what is used in the standard version of UNO.py, so it's rather unfortunate that these libraries aren't well-compatible with non-Windows systems.

<br>

**(￣o￣) . z Z**
