class Card:
    suits = ["diamonds", 
             "hearts", 
             "spades", 
             "clubs"]
    
    values = [None, None, "2", "3", 
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]
    
    def __init__(self, val, sui):
        '''Initialize the Card class'''
        self.value = val
        self.suit = sui
        
    def __lt__(self, card2):
        '''This function allows the < sign to work with the cards'''
        if self.value < card2.value:
            return True
        if self.value == card2.suit:
            if self.suit < card2.suit:
                return True
            else:
                return False
        return False
    
    def ___gt___(self, card2):
        '''This function allows the > sign to work with the cards'''
        if self.value > card2.value:
            return True
        if self.value == card2.value:
            if self.suit > card2.suit:
                return True
            else:
                return False
        return False
    
    def __repr__(self):
        '''This function makes a pretty string the displays the value/suit'''
        final = self.values[self.value] + " of " + self.suits[self.suit]
        return final