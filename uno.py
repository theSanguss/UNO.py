from cli_tools import InputError, inputHandler, assignInputToVar, clear, toggleFullscreen
from rich.console import Console
from time import sleep
from random import randint, shuffle
from player import Player, AIPlayer
from deck import Deck
import cli
import cursor

# Highlighting is kinda annoying for heavily-styled projects like UNO.py, so i disable it
console = Console(highlight = False)

class Game:
    def __init__(self):
        self.players = []
        self.deck = Deck()
        self.show_all_hands = False    # User-enabled feature
        self.first_turn = True    # At end of play_turn, set False
        self.your_index = None    # Index of human players(taken after shuffle(self.players))
        self.player_index = 0    # Index of current player, updates every turn
        self.direction = 1  # 1 for downwards(left to right), -1 for upwards(vice versa)
        self.act_or_draw_4_already_played = False    # Handy bool for ensuring card effects only occur once


    def start(self):
        clear()
        toggleFullscreen()

        try:
            self.setup(show_instructions = True)
            clear()
            while self.play_turn():    # Has to run the whole func before getting return bool
                clear()   # Unintuitive ik, but does eliminate a bit of redundancy
            clear()
            self.victory_screen()
            clear()

        except KeyboardInterrupt:    # Triggered by using Ctrl+C (it won't copy shit during runtime)
            # Note: Using Ctrl+Shift+C works for copying instead
            clear()
            cursor.hide()
            console.print("[orange1][dim]///[/dim] [b]EXITING UNO.PY ... [/b][/orange1]")
            sleep(1)
            print()

        finally:
            cursor.show()
            toggleFullscreen()


    def setup(self, show_instructions):
        cli.print_heading("", "orange3", "_", dimmen = False)
        cli.print_heading("UNO.PY", "orange1 on grey7", "█", dimmen = False)
        cli.print_heading("", "orange3", "‾", dimmen = False)
        print()
        print()
        print()
        print()

        cli.print_heading("A CLI-based Python recreation of the classic card game [gold3 i]UNO[/gold3 i], made by [orange1]theSanguss[/orange1].", "orange3", "  •  ")
        print()
        print()
        print()
        print()
        print()
        
        if show_instructions:
            cli.print_instructions()
            print()
            print()
            print()

        cli.print_heading("CONSOLE", "orange3")
        print()
        print()

        cli.progress_bar("[dim]///[/dim] [b]BOOTING ... [/b]", 108, 0.05)    # THIS is what causes cursor to reapper after hding
        cursor.hide()
        print()

        console.print(f"[orange1][dim]///[/dim] [b]COMMENCING SETUP ... [/b]")
        sleep(0.8)
        print()

        # There's even more pasta types than mentioned here lol, amazing idea on my part
        AI_PLAYER_NAMES = ("fusilli", "macaroni", "bolognese", "spaghetti", "penne", "farfalle", "fettucine", "riccioli", "rigatoni")
        
        def validatePlayerName(user_input: str):
            if not user_input.isalnum():
                if user_input == "":
                    user_input = "alfredo"
                else:
                    raise InputError("Name/alias must contain alphanumeric characters only, and no spaces!")
            
            # User input converted to lowercase for properly comparing it with AI_PLAYER_NAMES
            return assignInputToVar(user_input.lower(), invalid_choices = AI_PLAYER_NAMES)

        your_name = inputHandler(
            "Enter your name/alias: ",
            validatePlayerName,
            input_type = str,
            char_limit = 10
        )

        number_of_players = inputHandler(
            "Enter the total number of players in the game (2-10): ",
            assignInputToVar,
            input_type = str,
            valid_choices = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "random")
        )

        if number_of_players == "random":
            number_of_players = randint(2, 10)
        else:
            number_of_players = int(number_of_players)

        self.players = ([Player(your_name)] + [AIPlayer(name) for name in AI_PLAYER_NAMES[:number_of_players - 1]])
        shuffle(self.players)

        for a_player in self.players:
            if a_player.name == your_name.upper():
                self.your_index = self.players.index(a_player)
            a_player.hand.extend(self.deck.draw(7))

        self.deck.discard_pile.extend(self.deck.draw())

        # Prevents +4s from ever being the 1st drawn card (cuz it's against UNO rules)
        while self.deck.discard_pile[-1].value == "+ 4":
            self.deck.cards.append(self.deck.discard_pile.pop())
            self.deck.shuffle()
            self.deck.discard_pile.extend(self.deck.draw())

        cursor.hide()
        sleep(1)
        print()
        continue_input = console.input("[orange1][dim]>>>[/dim] [b]SETUP COMPLETE. PRESS [i]ENTER[/i] TO CONTINUE ... [/b][/orange1]")

        if continue_input == "show all hands":
            self.show_all_hands = True


    def play_turn(self):
        top_card = self.deck.discard_pile[-1]

        # Reverse logic is completed here; at the next turn
        if not self.act_or_draw_4_already_played and len(self.players) != 2 and top_card.value == "⮂":
            self.direction = -self.direction
            self.act_or_draw_4_already_played = True

        self.player_index = (self.player_index + self.direction) % len(self.players)
        prev_player_index = (self.player_index - self.direction) % len(self.players)
        next_player_index = (self.player_index + self.direction) % len(self.players)
        player = self.players[self.player_index]

        cli.print_heading("", "orange3", "_", dimmen = False)
        cli.print_heading("UNO.PY", "orange1 on grey7", "█", dimmen = False)
        cli.print_heading("", "orange3", "‾", dimmen = False)
        print()
        print()

        cli.display_players_and_top_card(player, self.players, self.direction, top_card)
        print()
        print()
        print()

        # Shows hand of current player each turn is show_all_hands is True
        cli.display_hand(player) if self.show_all_hands else cli.display_hand(self.players[self.your_index])
        print()
        print()
        print()

        cli.print_heading("CONSOLE", "orange3")
        print()
        print()

        if self.first_turn:
            cli.progress_bar("[dim]///[/dim] [b]REBOOTING ... [/b]", 108, 0.03)    # THIS is what causes cursor to reapper after hiding
            cursor.hide()
            print()
        else:
            cursor.hide()

        console.print(f"[orange1][dim]///[/dim] [b]{player.name}'S TURN IS STARTING ... [/b]")
        sleep(1)
        print()

        if self.first_turn and top_card.type == "WIL":
            if isinstance(player, AIPlayer):
                top_card.colour = cli.spinner(" THINKING OF COLOUR TO CHOOSE ...", 2.5, player.think_wild, top_card)
                console.print(f"[orange3][dim]//[/dim] {player.name} chose to set the card to {top_card.colour}![/orange3]")
            else:
                top_card.colour = cli.get_colour_choice()
                console.print(f"[orange3][dim]//[/dim] {player.name} chose to set the card to {top_card.colour}![/orange3]")

        elif not self.act_or_draw_4_already_played and (top_card.value == "🛇" or (len(self.players) == 2 and top_card.value == "⮂")):
            console.print(f"[orange3][dim]//[/dim] {player.name} was forced to forfeit their turn![/orange3]")
            
            self.act_or_draw_4_already_played = True

        elif not self.act_or_draw_4_already_played and top_card.value == "+ 2":
            console.print(f"[orange3][dim]//[/dim] {player.name} was forced to draw 2 cards![/orange3]")
            player.hand.extend(self.deck.draw(2))

            player.uno = False
            self.act_or_draw_4_already_played = True

        elif not self.act_or_draw_4_already_played and top_card.value == "+ 4":
            if isinstance(player, AIPlayer):
                choice = cli.spinner(f" THINKING OF WHETHER TO CHALLENGE {self.players[prev_player_index].name} OR DRAW 4 CARDS ... ", 3, player.think_challenge, top_card, self.players[prev_player_index])
            else:
                choice = cli.get_draw_4_choice(self.players[prev_player_index].name)

            if choice == "draw":
                console.print(f"[orange3][dim]//[/dim] {player.name} chose to draw 4 cards, rather than challenge {self.players[prev_player_index].name}![/orange3]")
                player.hand.extend(self.deck.draw(4))

                player.uno = False
            else:
                illegal_card_count = 0

                for card in self.players[prev_player_index].hand:
                    if card.colour == self.deck.discard_pile[-2].colour:
                        illegal_card_count += 1

                if illegal_card_count == 0:
                    console.print(f"[orange3][dim]//[/dim] {player.name} chose to challenge {self.players[prev_player_index].name}, and lost! {player.name} was forced to draw 6 cards![/orange3]")
                    player.hand.extend(self.deck.draw(6))

                    player.uno = False
                else:
                    console.print(f"[orange3][dim]//[/dim] {player.name} chose to challenge {self.players[prev_player_index].name}, and won! {self.players[prev_player_index].name} was forced to draw 4 cards instead![/orange3]")
                    self.players[prev_player_index].hand.extend(self.deck.draw(4))

                    self.players[prev_player_index].uno = False

            self.act_or_draw_4_already_played = True

        else:
            if isinstance(player, AIPlayer):
                choice = cli.spinner(" THINKING OF CARD TO PLAY OR WHETHER TO DRAW A CARD ... ", 3, player.think, top_card, self.players[next_player_index])
            else:
                choice = cli.get_card_choice(player, top_card)

            if choice == "draw":
                player.hand.extend(self.deck.draw())
                drawn_card = player.hand[-1]

                if drawn_card.is_playable_on(top_card):
                    # Almost identical to standard logic, don't feel like making a func for a 6-line if-else tho
                    if drawn_card.type == "WIL":
                        if isinstance(player, AIPlayer):
                            is_draw_4 = True if drawn_card.value == "+ 4" else False
                            drawn_card.colour = cli.spinner(" THINKING OF COLOUR TO CHOOSE ...", 2.5, player.think_wild, top_card, self.players[next_player_index], is_draw_4)
                        else:
                            drawn_card.colour = cli.get_colour_choice()

                    console.print(f"[orange3][dim]//[/dim] {"[i]UNO![/i] " if player.uno and len(player.hand) == 2 else ""}" + \
                        f"{player.name} drew a {drawn_card}, and played it![/orange3]")

                    self.deck.discard_pile.append(player.hand.pop())
                    self.act_or_draw_4_already_played = False
                else:
                    console.print(f"[orange3][dim]//[/dim] {player.name} drew a card, and kept it![/orange3]")
                    player.uno = False

            else:
                played_card = player.hand[choice - 1]

                if played_card.type == "WIL":
                    if isinstance(player, AIPlayer):
                        is_draw_4 = True if played_card.value == "+ 4" else False
                        played_card.colour = cli.spinner(" THINKING OF COLOUR TO CHOOSE ...", 2.5, player.think_wild, top_card, self.players[next_player_index], is_draw_4)
                    else:
                        played_card.colour = cli.get_colour_choice()

                console.print(f"[orange3][dim]//[/dim] {"[i b]UNO![/i b] " if player.uno and len(player.hand) == 2 else ""}" + \
                    f"{player.name} chose to play a {played_card}![/orange3]")

                self.deck.discard_pile.append(player.hand.pop(choice - 1))
                self.act_or_draw_4_already_played = False
            
        cursor.hide()
        sleep(1)
        print()

        if len(player.hand) == 0:
            sleep(1)
            return False    # Stops the turn loop exactly here

        # Logic only completes at start of next turn, so the already_played bool ain't mentioned here
        if not self.act_or_draw_4_already_played and len(self.players) != 2 and self.deck.discard_pile[-1].value == "⮂":
            console.print(f"[orange3][dim]//[/dim] Turn order has now been reversed to go {"upwards" if self.direction == 1 else "downwards"}![/orange3]")
            sleep(1)
            print()

        if len(self.players) != 2 and len(player.hand) == 1 and (not player.uno) and (not self.act_or_draw_4_already_played) and randint(0, (len(self.players) // 4) + 2) <= 1:
            console.print(f"[orange3][dim]//[/dim] {player.name} was caught not saying [i]UNO[/i], and was forced to draw 4 cards![/orange3]")
            player.hand.extend(self.deck.draw(4))
            sleep(1)
            print()

        end_input = console.input(f"[orange1][dim]>>>[/dim] [b]PRESS [i]ENTER[/i] TO PROCEED TO NEXT TURN ... [/b][/orange1]")

        if isinstance(player, AIPlayer) and len(player.hand) == 1 and (not player.uno) and (not self.act_or_draw_4_already_played) and end_input[:7] == "gotcha " and end_input[7:].upper() == player.name:
            print("\033[A\033[K", end = "\r")
            console.print(f"[orange3][dim]//[/dim] {player.name} was caught not saying [i]UNO[/i], and was forced to draw 4 cards![/orange3]")
            player.hand.extend(self.deck.draw(4))
            sleep(1)
            print()
            console.input("[orange1][dim]>>>[/dim] [b]PRESS [i]ENTER[/i] TO PROCEED TO NEXT TURN ... [/b][/orange1]")   # No challenging here

        self.first_turn = False    # Ensures it goes from True to False and stays that way
        return True    # Keeps the turn loop going


    def victory_screen(self):
        cli.print_heading("", "orange3", "_", dimmen = False)
        cli.print_heading("UNO.PY", "orange1 on grey7", "█", dimmen = False)
        cli.print_heading("", "orange3", "‾", dimmen = False)
        print()
        print()
        print()

        for a_player in self.players:
            if len(a_player.hand) == 0:
                cli.print_victory_msg(a_player.name)    # at long last... (◡‿◡) victory...

        cli.print_heading("CONSOLE", "orange3")
        print()
        print()

        cli.progress_bar("[dim]///[/dim] [b]REBOOTING ... [/b]", 108, 0.015)
        cursor.hide()
        print()

        final_input = console.input("[orange1][dim]>>>[/dim] [b]PRESS [i]ENTER[/i] TO EXIT UNO.PY ... [/b][/orange1]")

        if final_input.lower() == "gg":
            print()
            console.print(f"[orange3][dim]//[/dim] GG, {self.players[self.your_index].name}![/orange3]")
            sleep(1)
            
        # That's all, folks! See ya next time!
