class Luhn:
    card_num = ""
    def __init__(self, card_string):
        self.card_num = card_string.strip()

    def valid(self):
        s = self.card_num.replace(" ", "")  # ignore spaces

        if len(s) <= 1 or not s.isdigit():
            return False
    
        total = 0
        for i, ch in enumerate(reversed(s)):
            digit = int(ch)
            if i % 2 == 1:          # double every 2nd digit from the right (excluding check digit)
                digit *= 2
                if digit > 9:
                    digit -= 9
            total += digit
    
        return total % 10 == 0
        
