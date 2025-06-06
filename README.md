![Logo](/UNO_icon_new.ico)

<br>

- 🚀 _My first OOP Python project, as well as my first GitHub repository! (ignoring config repo)_
- 🎮 _Singleplayer turn-based card game with AI opponents._
- 📟 _Runs within the terminal, is lightweight in code, and primarily uses a CLI._
- 🐍 _Made with Python (version 3.12)._

<br>

> [!Note]\
> Despite the name, UNO.py isn't actually a single file, but I've titled it this since the very beginning of its development, and don't feel the need to change it.

<br>

![Setup Screen](/Gameplay%20Images/setup_screen.png)

![UI rich in Rich formatting](/Gameplay%20Images/variety_of_cards_in_hand.png)

<br>

## How to run?

**If you have Python installed** (MacOS and Linux usually have Python pre-installed), enter the following commands into your terminal:

```bash
git clone https://github.com/theSanguss/UNO.py.git
cd UNO.py
pip install -r requirements.txt
python main.py
```

**If you don't have Python, and if you happen to be a Windows user**, just download and run the EXE file `UNO.py.exe` available in this repository, which works as a standalone application.

**If you are not a Windows user, and wish to get an executable file version of UNO.py**, you can use [PyInstaller](https://github.com/pyinstaller/pyinstaller/) to make it yourself. For more info on how to use this tool to make an UNO.py executable, [refer to the last question in the FAQ section](#5-how-can-i-convert-this-into-an-executable-file-myself-using-pyinstaller).

## How to operate?

This is a CLI-based application, so entering in inputs as you normally would in a terminal is pretty much all you need to do.

Most inputs are intuitive and self-explanatory, and those that aren't are specified and detailed in-game.

> [!Note]\
> This program has been tested to work on MacOS and Linux, but certain issues like the the automatic toggling of fullscreen-mode still persist. So for the time being, users on systems hostile to [PyAutoGUI](https://github.com/asweigart/pyautogui/) (one example being Linux users using Wayland instead of X11) will have to make do with toggling fullscreen-mode manually.
>
> Please do file an issue if you encounter anything unexpected or problematic, especially if you're not a Windows user.

<br>

![UNO! declared & turn order reversed](/Gameplay%20Images/declared_uno_and%20reversed_turn_order.png)

![Victory Screen](/Gameplay%20Images/lesgo_i_win.png)

<br>

# FAQs :

## 1. Are the rules the same as normal UNO?

Yes, except for two things - viewing the cards of the player you challenge (isn't necessary here, cuz this ain't IRL), and the score system (cuz literally no one cares about that). Stacking, 'jump-in's and other such house rules haven't been implemented, **but if you wish to contribute to this project, I highly suggest starting with adding the functionality in the game loop for some of these to be available as custom rules during setup**.

<br>

## 2. Does this support local multiplayer?

No. It wouldn't be all too hard to implement by just adding multiple Player objects, but from a gameplay standpoint, it would be annoying to manange. **Feel free to fork this project and try implementing a Local Multiplayer system you think would work well. Again, contributions are welcome.**

<br>

## 3. How does the UI work?

This project makes extensive use of the wonderful [Rich library](https://github.com/Textualize/rich/) for its UI, so much so that it can serve as a showcase for several of Rich's versatile components and how they can be meshed together! It is still fundamentally text-based though, so maybe take a look at some of the tips below for better UI rendering:

> [!Tip]\
> For optimal results, ensure that the terminal you're using isn't overly customised and doesn't make use of custom fonts, especially if it's not Windows PowerShell. Background themes as well as custom text colouring have no impact on the UI.
>
> Windows Powershell's default font size is enough to get the proper UI experience, as it eliminates the need to ever scroll the UI. If you are not using Windows Powershell, or have changed the font size, you may have to reduce the font size. However, you might only have to do this to make the setup UI fit in one screen, so another thing you can do is to replace line 30 of the file `uno.py` with `self.setup(show_instructions = False)`, so that the long instructions list will be hidden.

<br>

## 4. How does the AI in this work?

The AI players in this are biased by a numerical property called their 'intellect'. I say 'biased', as a large part of their logic is based on random chance, and intellect only serves to vary this chance. In some cases, AIs with the lowest intellect are barred from making intelligent decisions.

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

After this, two new folders will be generated inside `UNO.py` - `build` and `dist`. `build` can be ignored, but it is within `dist` that the executable will be stored. The `--onefile` parameter in the above command creates a standalone executable file, which can be moved to any location in your system.

If you don't want the libraries to be bundled with the executable, and would prefer to run the executable from within the `dist` directory, rather than having it as a portable standalone, you can remove the `--onefile` parameter. This will also improve the executable's startup speed by some amount.

> [!Note]\
> The `--add-data` parameter is mandatory to include, as [Pyfiglet](https://github.com/pwaller/pyfiglet/), a font library used with this project, requires a filepath to be specified for it to be able to access its font files.
>
> `.ico` files are not supported as file icons on systems other than Windows, so you'll have to convert `UNO-icon-new.ico` to a different file format (like `.icns` for MacOS and `.png` for Linux) in order to use it in the `--icon` parameter.

> [!Warning]\
> This command hasn't been tested on other systems, and there is no guarantee that it will work for all users. However, this is the easiest method I know of which also resolves all issues with Pyfiglet, and has worked flawlessly for me, which is why I recommend using it.

<br>

**(￣ o ￣) . z Z**
