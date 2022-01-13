suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack", "Queen", "King", "Ace")
values = {"Two": 2,"Three" :3 ,"Four" :4,"Five" :5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10, "Queen":10, "King":10, "Ace":11}

class Hand:
    def __init__(self):
        self.cards=[]
        self.value = 0
        self.aces = 0
    
    def add_card (self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces+=1

    def adjust_for_aces(self):
        while self.value>21 and self.aces:
            self.value -= 10
            self.aces -=1

    def hit(self,deck):
        self.add_card(deck.deal())
        self.adjust_for_aces()
        print(self.value)

    playing = True
    def hit_or_stand(self,deck):
        global playing
        while True: 
            x=input("Would you like to Hit or Stand? Enter 'h' or 's'.")
            print(x)
            if x =='h':
                self.hit(deck)
            elif x.lower =='s':
                print("Player Stands. Dealer is playing!")
            else:
                print("Sorry, please try again.")
                continue
            break
    