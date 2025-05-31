![Logo](/UNO_icon_new.ico)

**My first OOP Python project. Runs fully within the terminal.**

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

## How to operate?

This is a CLI-based application, so entering in inputs as you normally would in a terminal is pretty much all you need to do.

Most inputs are self-explanatory, and those that aren't are specified and detailed in-game.

## Is this just another boring CLI?

Thankfully not. For this projects makes extensive use of the wonderful [Rich library](https://github.com/Textualize/rich/).

## Are the rules the same as normal UNO?

Yes, except for things like viewing the cards of the player you challenge (isn't necessary here, cuz this ain't IRL), and the score system (cuz literally no one cares about that).

## Does this support local multiplayer?

No. It wouldn't be all too hard to implement, but from a gameplay standpoint, it would be annoying to manange. Feel free to fork this project and try implementing a good Local Multiplayer system.

## How does the AI in this work?

The AI players in this are biased by a numerical property called their 'intellect'. I say 'biased', as a large part of their logic is based on random chance, and intellect only serves to vary this chance. In some cases, AIs with the lowest intellect are barred from making intelligent decisions.
