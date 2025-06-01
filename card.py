
class Card:
    def __init__(self, type, colour, value):
        self.type = type
        self.colour = colour
        self.value = value

    def is_playable_on(self, top_card):
        if self.type == "WIL":
            return True
        if self.colour == top_card.colour or self.value == top_card.value:
            return True
        
        return False

    def __str__(self):
        def express_value(val):
            # Keys are reprs, vals are the actual values (alt reverse char -> ⇄)
            val_expressions = {
                "̲6": "6",
                "̲9": "9",
                "🛇": "skip",
                "⮂": "reverse",
            }

            return val_expressions.get(val, val)
        
        return f"WILD{" + 4" if self.value == "+ 4" else ""} card, set to {self.colour}" \
            if self.type == "WIL" else f"{self.colour} {express_value(self.value)}"
