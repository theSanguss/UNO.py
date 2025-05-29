from rich.console import Console
from rich.panel import Panel
from rich.text import Text    # Using Text() objects is the easiest way to change text alignment, can also be used for styling
from rich.table import Table
from rich.rule import Rule
from rich import box
from rich.align import Align
from rich.spinner import Spinner
from rich.live import Live
from rich.progress import (
    Progress,
    TextColumn,
    BarColumn,
    TaskProgressColumn
)
from pyfiglet import figlet_format
from cli_tools import inputHandler, assignInputToVar, InputError
from time import sleep

console = Console(highlight = False)

def trueColour(colour):
    # Doesn't affect gameplay, only used for card representation
    true_colours = {
        "red": "#D72600",
        "yellow": "#ECD407",
        "green": "#379711",
        "blue": "#0956BF"
    }
    
    return true_colours.get(colour, colour)

def progress_bar(message, number_of_iters, time_per_iter):
    # Fully customised progress bar, % is stuck as a float tho, imma pretend its intentional lmao
    progress = Progress(
        TextColumn("[orange1]{task.description}"),
        BarColumn(bar_width = console.width // 2, style = "orange3 dim", complete_style = "orange3", finished_style = "orange1"),
        TaskProgressColumn(text_format = "{task.percentage}%",style = "orange3", markup = False),
        refresh_per_second = 25
    )

    with progress:
        task = progress.add_task(message, total = number_of_iters)
        for _ in range(108):
            sleep(time_per_iter)
            progress.update(task, advance = 1)

def spinner(message, loading_time, func, *args):
    spinner = Spinner("line", text = f"[orange1]{message}[/orange1]" , style = "orange1 dim")

    sleep(0.1)
    with Live(spinner, refresh_per_second = 25, transient = True):
        sleep(loading_time)
        return func(*args)

def print_heading(heading, style, char = "/", *, dimmen = True):
    console.print(Rule(title = heading, style = f"{"dim" if dimmen == True else ""} {style}", characters = char), style = f"{style} b")


def print_instructions():
    print_heading("INSTRUCTIONS", "orange3")
    print()
    print()

    No1 = "When choosing to play a card, enter the number corresponding to the position of the card in your hand. " \
        "This number is given at the bottom-right corner of each card. When choosing to draw, simply enter [b]'draw'[/b].\n"
    
    No2 = "When playing a card while having two cards, remember to type [b]'uno [dim]<[/dim]card number[dim]>[/dim]'[/b] instead to declare UNO as well, and thus avoid being caught. " \
        "When drawing a card while having one card, in case the card can be played, remember to type [b]'uno draw'[/b] instead to ensure UNO is declared in that scenario.\n"
    
    No3 = "If a player forgets to declare UNO when they're supposed to, and doesn't get caught by anyone else, " \
        "just after you're prompted to proceed to the next turn, type [b]'gotcha [dim]<[/dim]current player's name[dim]>[/dim]'[/b] to catch them.\n"
    
    No4 = "[b i]Cheat Code:[/b i] Typing [b]'show all hands'[/b] just after being prompted to continue once setup is completed, " \
        "allows you to see the hand of the current player each turn.\n"
    
    No5 = "[b i]About Setup:[/b i] If no name is entered for the player, [b]ALFREDO[/b] is taken by default. " \
        "Entering [b]'random'[/b] as the number of players chooses a random number of players.\n\n"

    instructions_display = Table.grid()
    
    instructions_display.add_column()
    instructions_display.add_column()
    
    instructions_display.add_row("[dim]  ❖  [/dim]", No1)
    instructions_display.add_row("[dim]  ❖  [/dim]", No2)
    instructions_display.add_row("[dim]  ❖  [/dim]", No3)
    instructions_display.add_row("[dim]  ❖  [/dim]", No4)
    instructions_display.add_row("[dim]  ❖  [/dim]", No5)

    console.print(instructions_display, style = "orange3")
    
    console.print(Align("[orange1 b]-- PRESS CTRL+C AT ANY TIME TO EXIT UNO.PY --[/orange1 b]", align = "center"))


def display_players_and_top_card(player, players, direction, top_card):
    # Arrow chars -> 🠇, 🠅
    panel = Align(Panel(
                Panel(
                    Text(top_card.value, style = "b", justify = "center"),
                    title = f"[i]{top_card.type}[/i]",
                    style = f"{trueColour(top_card.colour)} on grey7",
                    expand = False,
                    padding = (1, 1)
                ),
                title = f"[b]{"🠇 ═══ 🠇" if direction == 1 else "🠅 ═══ 🠅"}[/b]",
                subtitle = f"[b]{"🠇 ═══ 🠇" if direction == 1 else "🠅 ═══ 🠅"}[/b]",
                border_style = "orange1 b",
                padding = (0, 1),
                expand = False,
                box = box.DOUBLE
    ), align = "center")

    player_display = Table.grid(expand = True, pad_edge = True)

    player_display.add_column(width = 1)
    player_display.add_column(width = console.width // 3)
    player_display.add_column(width = console.width // 3)
    player_display.add_column(width = console.width // 3)

    left_player_list = ""
    right_player_list = ""

    for a_player in players[:((len(players) + 1) // 2)]:
        left_player_list += f"{a_player}{"[gold1 b]⠀<<[/gold1 b]" if a_player.name == player.name else ""}\n"

    for a_player in players[((len(players) + 1) // 2):]:
        right_player_list += f"{a_player}{"[gold1 b]⠀<<[/gold1 b]" if a_player.name == player.name else ""}\n"

    player_display.add_row("⠀", left_player_list, panel, right_player_list)

    console.print(player_display, style = "orange3 b")


def display_hand(player):
    hand_display = Table.grid(padding = (1, 2))
    card_panels = []
    
    for i, card in enumerate(player.hand):
        panel = Panel(
            Text(card.value, style = "b", justify = "center"),
            title = f"[i]{card.type}[/i]",
            style = f"{trueColour(card.colour)} on grey7",
            subtitle = f"[dim i]{i + 1}[/dim i]",
            subtitle_align = "right",
            expand = False,
            padding = (1, 1)
        )

        card_panels.append(panel)

    # Creates the tabular/grid display for the cards in hand
    # The display will be 15 columns wide, and will wrap to the next line if there are more than 15 cards in hand
    if len(card_panels) <= 15:    
        for x in card_panels:
            hand_display.add_column()

        hand_display.add_row(*card_panels)
    else:
        for x in card_panels[:15]:
            hand_display.add_column()

        hand_display.add_row(*card_panels[:15])
        
        for k in range(15, len(card_panels), 15):
            hand_display.add_row(*card_panels[k:k+15])
    
    # Prints out a nice header for the hand display
    print_heading(f"{player.name}'S HAND", "orange3")
    print()
    print()

    # Actually prints out the hand display onto the console
    console.print(hand_display)


def print_victory_msg(winner_name):
    # Both pyfiglet and rich are amazing for this to work so easily
    console.print(
        Align(Text(
            figlet_format(winner_name, font = "o8", width = console.width),
            style = "orange1 b"
            )
        , align = "center"))
    sleep(1.5)

    console.print(
        Align(Text(
            figlet_format("wins...", font = "o8", width = console.width),
            style = "orange3 b"
            )
        , align = "center"))
    sleep(1.5)

    console.print(
        Align(Text(
            figlet_format("UNO !", font = "univers"),
            style = "gold1 b"
            )
        , align = "center"))
    sleep(1.5)


def get_card_choice(player, top_card):
    def validateCardChoice(user_input, player, top_card):
        uno_time = False

        if user_input == "draw": 
            return "draw"
        
        if user_input == "uno draw" and len(player.hand) == 1:
            player.uno = True
            return "draw"
        
        if user_input[:4] == "uno " and len(player.hand) == 2:
            uno_time = True
            user_input = user_input[4:]
        
        choice = assignInputToVar(user_input, valid_choices = tuple(map(str, range(1, len(player.hand) + 1))))

        card_choice = player.hand[int(choice) - 1]

        if not card_choice.is_playable_on(top_card):
            raise InputError("Chosen card cannot be played!")
        
        if uno_time:
            player.uno = True
        
        return int(choice)

    actual_choice = inputHandler(
        "Choose a card to play, or draw a card: ",
        validateCardChoice,
        input_type = str,
        player = player,
        top_card = top_card
    )

    return actual_choice


def get_colour_choice():
    choice = inputHandler(
        "Choose a colour to set the card to: ",
        assignInputToVar,
        input_type = str,
        valid_choices = ("red", "yellow", "blue", "green")
    )

    return choice


def get_draw_4_choice(prev_player_name):
    choice = inputHandler(
        f"Choose to either challenge {prev_player_name}, or draw 4 cards: ",
        assignInputToVar,
        input_type = str,
        valid_choices = ("challenge", "draw")
    )

    return choice
