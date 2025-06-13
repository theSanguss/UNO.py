from random import randint, shuffle

class Player:
    def __init__(self, name):
        self.name = name.upper()    # Max length should be 10
        self.hand = []
        self.uno = False

    def __str__(self):
        return f"{self.name}{' ' * (11 - len(self.name))}:{' 🂠' * len(self.hand)}" + \
        f"{'[gold1 b i] UNO[/gold1 b i]' if self.uno == True else ''}"


class AIPlayer(Player):
    def __init__(self, name):
        super().__init__(name)   # Exact same properties as Player()
        self.intellect = randint(1, 3)    # 1 = stoopid, 2 = alright, 3 = smort

    def think(self, top_card, next_player):
        # Below vars contains the number of playable cards in hand
        playable_card_count = len([card for card in self.hand if card.is_playable_on(top_card)])
        playable_act_or_wil_count = len([card for card in self.hand if card.is_playable_on(top_card) and card.type != "NUM"])

        # Prepares the draw_4_is_safe bool
        draw_4_is_safe = True
        for card in self.hand:
            if card.colour == top_card.colour:
                draw_4_is_safe = False

        # Handy bools
        card_passed = False
        offensive_mode = True if randint(0, 2) == 0 else False

        # Skips rest of logic if no playable cards, easier that way
        if playable_card_count == 0:
            if len(self.hand) == 1:
                self.uno = randint(0, 5) <= self.intellect + 1
            
            return "draw"
        
        # Nice offensive strat, obv a desperate attempt tho
        if offensive_mode and self.intellect != 1 and len(next_player.hand) == 1 and len(self.hand) != 1 and playable_act_or_wil_count == 0:
            return "draw"
        
        # To ensure randomness, hand is shuffled before main logic
        shuffle(self.hand)

        for i, card in enumerate(self.hand):
            if card.is_playable_on(top_card):
                # Last card; always play it
                if len(self.hand) == 1:
                    return 1
                
                # Always say UNO with 2 cards if max intellect, else leave it to chance
                if len(self.hand) == 2:
                    self.uno = randint(0, 5) <= self.intellect + 2
                    return i + 1

                # Below two ifs roughly translate to imma screw u over
                if offensive_mode and len(next_player.hand) <= self.intellect and playable_act_or_wil_count >= 1 and card.type == "NUM":
                    continue
                
                if offensive_mode and len(next_player.hand) <= self.intellect and playable_act_or_wil_count >= 1:
                    return i + 1
                
                # Ensures wild isn't played on 2 playables (unless player's dum and loses 50 50)
                if randint(0, 1) != self.intellect and playable_card_count == 2:
                    if card.type != "WIL":
                        card_passed = True

                    if card.type == "WIL" and not card_passed:
                        card_passed = True
                        continue
                
                if playable_card_count <= 2:
                    # Higher chance to play a card if there are only 2 playable cards
                    play_threshold = self.intellect + (8 // len(self.hand))
                    if randint(0, play_threshold) != 0:
                        return i + 1
                
                # playable_card_count >= 2 * playable_act_or_wil_count same as p_c_c - p_a_o_w_c >= p_a_o_w_c
                if card.type == "NUM":
                    if playable_card_count >= 2 * playable_act_or_wil_count and self.intellect == 3:
                        return i + 1
                    
                    # 1 and 3 both return 3, 2 however returns 2
                    if randint(0, self.intellect**2 - 4*self.intellect + 6) <= 1:
                        return i + 1

                if card.type == "ACT":
                    # Inverse of the 1st if in NUM logic
                    if playable_card_count <= 2 * playable_act_or_wil_count and randint(0, 1) == 0:
                        return i + 1

                    if randint(0, self.intellect + 1) == 0:
                        return i + 1

                # Prevents non-stoop players from illegally playing +4s for 0 good reason
                if self.intellect != 1 and card.type == "+ 4" and (not draw_4_is_safe):
                    continue

                if card.type == "WIL":
                    # Low intellect AIs more likely to play WIL cards immediately
                    if randint(0, self.intellect * 3) <= 1:
                        return i + 1
        
        # If all else fails ...
        return "draw"
    

    def think_wild(self, top_card, next_player = None, is_draw_4 = False):
        # AI player chooses a colour based on the most common colour in their hand
        colours = ["red", "green", "blue", "yellow"]
        shuffle(colours)
        colour_count = {colour: 0 for colour in colours} # Measures no. of cards in hand of each colour(not counting white)

        for card in self.hand:
            if card.type != "WIL":
                colour_count[card.colour] += 1
        
        # Make sure to always pass next_player into the function
        if next_player != None and (not is_draw_4) and randint(0, 7 - (self.intellect * 2)) == 0:
            next_colour_count = {colour: 0 for colour in colours}
            
            for card in next_player.hand:
                if card.type != "WIL":
                    next_colour_count[card.colour] += 1
            
            chosen_colour = min(next_colour_count, key = next_colour_count.get)

            # Pretty much logic for saying let whoever's next draw 1 card hehehe
            if next_colour_count[chosen_colour] == 0 and colour_count[chosen_colour] != 0:
                return chosen_colour
            
            # Returns val for own hand, here next_player is left out
            return self.think_wild(top_card)
        
        # Chooses colour with the highest count; the first highest in case of a tie
        chosen_colour = max(colour_count, key = colour_count.get)
        
        if chosen_colour == top_card.colour and (not randint(0, 2) > self.intellect):
            colour_count.pop(chosen_colour)
            chosen_colour = max(colour_count, key = colour_count.get)

        return chosen_colour


    def think_challenge(self, top_card, prev_player):
        # Pretty much hax lmao
        if self.intellect == 3 and randint(0, 1) == 0:
            colour_count = 0

            for card in prev_player.hand:
                if card.colour == top_card.colour:
                    colour_count += 1

            return "challenge" if colour_count != 0 else "draw"

        # More likely to challenge out of desp
        if len(self.hand) <= 2:
            return "challenge" if randint(0, 3 - len(self.hand)) != 0 else "draw" 

        # 1 and 3 both return 2, 2 however returns 1
        return "challenge" if randint(0, self.intellect**2 - 4*self.intellect + 5) == 0 else "draw"
