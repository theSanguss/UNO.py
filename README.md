![Logo](/UNO_icon_new.ico)

<br>

- 🚀 _My first OOP Python project, as well as my first GitHub repository! (ignoring config repo)_
- 🎮 _Singleplayer turn-based card game with AI opponents._
- 📟 _Runs within the terminal, is lightweight in code, and primarily uses a CLI._
- 🐍 _Made with Python (version 3.12)._

<br>

> [!Note]\
> Despite the name, UNO.py isn't actually a single file, but I've titled it this since the very beginning of its development, and now it'd feel weird to change the name.

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

**If you are not a Windows user, and wish to get an executable file version of UNO.py**, you can use [PyInstaller](https://github.com/pyinstaller/pyinstaller/) to make it yourself. For more info on how to use PyInstaller to make an UNO.py executable, refer to the last question in the FAQ section.

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
> For optimal results, ensure that the terminal you're using isn't overly customised and doesn't make use of custom fonts, especially if you're not using Windows PowerShell.
>
> However, do note that background themes as well as custom text colouring have no impact on the UI. Even the images below show UNO.py running in a custom-themed PowerShell.
>
> Also, your terminal's font size should ideally be small enough so as to be able to navigate through the whole UI without ever scrolling. The initial setup screen is the largest in size, and if you don't want to reduce your font size, just disable the instructions from being displayed from within the declaration of `self.setup()` in the file `uno.py`.

<br>

## 4. How does the AI in this work?

The AI players in this are biased by a numerical property called their 'intellect'. I say 'biased', as a large part of their logic is based on random chance, and intellect only serves to vary this chance. In some cases, AIs with the lowest intellect are barred from making intelligent decisions.

<br>

## 5. Is it viable to convert this into an executable file using PyInstaller?

Yes, I have done this before and feel obliged to let you know that the [Pyfiglet library](https://github.com/pwaller/pyfiglet/) does **_not_** like working with [PyInstaller](https://github.com/pyinstaller/pyinstaller/) as is, and most of the things you'll find online to fix this (like hooks) are kinda a pain in the ass to figure out by yourself. However, running the below command solved this issue completely for me, and will probably work for others as well:

```bash
pyinstaller --onefile --name="UNO.py" --icon="UNO_icon_new.ico" --add-data "[insert filepath here]\site-packages\pyfiglet\fonts;.\pyfiglet\fonts" main.py
```

> [!Important]\
> Remember to replace `[insert filepath here]` with the path to the `site-packages` directory for Python on your own system.
>
> Make sure to run this command with the terminal directing to the `UNO.py` directory, so that PyInstaller can actually access the needed files.

> [!Caution]\
> This command has _not_ been tested yet on MacOS and Linux, and I'm fairly sure `.ico` files are only supported as file icons on Windows.
>
> So, exercise caution when running this command on a non-Windows operating system. Perhaps removing the `--icon` parameter is all that needs to be done.

<br>

**(￣ o ￣) . z Z**
