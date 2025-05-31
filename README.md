![Logo](/UNO_icon_new.ico)

<br>

<i>
<ul>
<li>🚀 My first OOP Python project, as well as my first GitHub repository! (ignoring config repo)
<li>📟 Runs fully within the terminal, nothing extra.
<li>🐍 Made with Python (version 3.12).
</ul>
</i>

<br>

> [!Note]\
> Despite the name, UNO.py isn't actually a single file, but it's nicer to call it that. :-P

<br>

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

<br>

## How to operate?

This is a CLI-based application, so entering in inputs as you normally would in a terminal is pretty much all you need to do.

Most inputs are self-explanatory imo, and those that aren't are specified and detailed in-game.

<br>

## Is this just another boring CLI game?

Thankfully not. For this project makes extensive use of the wonderful [Rich library](https://github.com/Textualize/rich/), thus making it almost as user-friendly as an actual GUI!

![UI rich in Rich formatting](/Gameplay%20Images/variety_of_cards_in_hand.png)

<br>

## Are the rules the same as normal UNO?

Yes, except for two things - viewing the cards of the player you challenge (isn't necessary here, cuz this ain't IRL), and the score system (cuz literally no one cares about that).

<br>

## Does this support local multiplayer?

No. It wouldn't be all too hard to implement by just adding multiple Player objects, but from a gameplay standpoint, it would be annoying to manange. Feel free to fork this project and try implementing a good Local Multiplayer system. Maybe even have it run on a separate terminal for each non-AI player? Idk.

<br>

## How does the AI in this even work?

The AI players in this are biased by a numerical property called their 'intellect'. I say 'biased', as a large part of their logic is based on random chance, and intellect only serves to vary this chance. In some cases, AIs with the lowest intellect are barred from making intelligent decisions.

<br>

## Is it viable to convert this into an EXE file using PyInstaller?

Yes, I have done this before and feel obliged to let you know that the [Pyfiglet library](https://github.com/pwaller/pyfiglet/) does **_not_** like working with PyInstaller as is, and most of the things you'll find online to fix this (like hooks) are kinda a pain in the ass to figure out by yourself. However, running the below command solved this issue completely for me, and will probably work for others as well:

```bash
pyinstaller --onefile --name="UNO.py" --icon="UNO_icon_new.ico" --add-data "[insert filepath here]\site-packages\pyfiglet\fonts;.\pyfiglet\fonts" main.py
```

> [!Note]\
> Remember to replace _[insert filepath here]_ with the path to the _site-packages_ directory for Python on your system.
>
> Make sure to run this command with the terminal directing to the UNO.py directory.

> [!Warning]\
> Again, this command has _not_ been tested on MacOS and Linux, and I'm fairly sure .ico files are only supported as icons on Windows.
>
> So, exercise caution when running this command on a non-Windows operating system. Perhaps removing the _--icon_ parameter is all that needs to be done.

<br>

### Well, that's about all I have to tell you. Here's some more gameplay screenshots to get you interested...

![UNO! declared & turn order reversed](/Gameplay%20Images/declared_uno_and%20reversed_turn_order.png)

<br>

![Victory Screen](/Gameplay%20Images/lesgo_i_win.png)

**(￣ o ￣) . z Z**
