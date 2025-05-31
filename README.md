![Logo](/UNO_icon_new.ico)

_My first OOP Python project. Runs fully within the terminal. Made with Python 3.12._

> [!Note]\
> Despite the name, UNO.py isn't actually a single file, but it's nicer to call it that. :P

## How to run?

Enter the following in your terminal:

```bash
git clone https://github.com/theSanguss/UNO.py.git
cd UNO.py
pip install -r requirements.txt
python main.py
```

> [!Warning]\
> This program has not yet been tested for MacOS and Linux.
>
> Please do file an issue if you encounter anything unexpected.

## How to operate?

This is a CLI-based application, so entering in inputs as you normally would in a terminal is pretty much all you need to do.

Most inputs are self-explanatory, and those that aren't are specified and detailed in-game.

## Is this just another boring CLI game?

Thankfully not. For this projects makes extensive use of the wonderful [Rich library](https://github.com/Textualize/rich/).

![UI rich in Rich formatting](/Gameplay%20Images/variety_of_cards_in_hand.png)

## Are the rules the same as normal UNO?

Yes, except for things like viewing the cards of the player you challenge (isn't necessary here, cuz this ain't IRL), and the score system (cuz literally no one cares about that).

## Does this support local multiplayer?

No. It wouldn't be all too hard to implement, but from a gameplay standpoint, it would be annoying to manange. Feel free to fork this project and try implementing a good Local Multiplayer system.

## How does the AI in this work?

The AI players in this are biased by a numerical property called their 'intellect'. I say 'biased', as a large part of their logic is based on random chance, and intellect only serves to vary this chance. In some cases, AIs with the lowest intellect are barred from making intelligent decisions.

## Can I convert this into an EXE file via PyInstaller?

Yes, I have done this before and feel obligated to let you know that the [pyfiglet library](https://github.com/pwaller/pyfiglet/) does **_not_** like working with PyInstaller as is, and most of the things you'll find online to fix (like hooks) this are kinda a pain in the ass to figure out by yourself. However, running the below command solved this issue completely for me, and will probably work for others as well:

```bash
pyinstaller --onefile --name="UNO.py" --icon="UNO_icon_new.ico" --add-data "[insert filepath here]\site-packages\pyfiglet\fonts;.\pyfiglet\fonts" main.py
```

> [!Note]\
> Remember to replace _[insert filepath here]_ with the path to the site-packages directory for Python on your system.

> [!Warning]\
> Again, this command has _not_ been tested on MacOS and Linux, and I'm fairly sure .ico files are only supported as icons on Windows.
>
> So, exercise caution when running this commmand on a non-Windows operating system.

### Well, that's about all I have to tell you. Here's some more gameplay screenshots to get you interested...

![UNO! declared & turn order reversed](/Gameplay%20Images/declared_uno_and%20reversed_turn_order.png)

![Victory Screen](/Gameplay%20Images/lesgo_i_win.png)
