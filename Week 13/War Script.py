from deck import Deck
from player import Player
import pygame
import pygame_gui

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))

class Game:
    def __init__(self):
        p1Name = input("Enter player 1 name: ")
        p2Name = input("Enter player 2 name: ")
        self.deck = Deck()
        self.p1 = Player(p1Name)
        self.p2 = Player(p2Name)
        self.sprite1: pygame.surface
        self.sprite2: pygame.surface

        
    def winner(self, win):
        '''This function displays the winner to the console'''        
        print(f"{win} wins this battle!")
        
    def pickCard(self, surface, p1Name, p2Name, p1Card, p2Card):
        '''This function displays the draw card event to the console'''
        p1Card = "Assets/Cards/" + str(p1Card).replace(" ", "_").lower() + ".png"
        p2Card = "Assets/Cards/" + str(p2Card).replace(" ", "_").lower() + ".png"
        print("sprite loaded")
        self.sprite1 = pygame.image.load(p1Card).convert_alpha()
        self.sprite2 = pygame.image.load(p2Card).convert_alpha()  
        print("images loaded")
        ################################

        self.draw_card(surface)

        ################################
        print(f"{p1Name} drew {p1Card} and {p2Name} drew {p2Card}")
    
    def draw_card(self, surface):
        print("draw card")
        surface.blit(self.sprite1,(50, 50))
        surface.blit(self.sprite2,(150, 50))
        
    
    def play(self, surface):
        cards = self.deck.cards
        print("Begin the War!")
        while len(cards) >= 2:
            response = input("Press 'q' to quit. Press any other key to play: ")
            if response == 'q':
                break
            p1Card = self.deck.removeCard()
            p2Card = self.deck.removeCard()
            p1Name = self.p1.name
            p2Name = self.p2.name
            # DEBUG
            self.pickCard(surface, p1Name, p2Name, p1Card, p2Card)
            if p1Card > p2Card:
                self.p1.wins += 1
                self.winner(self.p1.name)
            elif p1Card < p2Card:
                self.p2.wins += 1
                self.winner(self.p2.name)
                
        win = self.totalWinner(self.p1, self.p2)
        print(f"The war is over! {win} is the victor!")
    
    def totalWinner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie"

pygame.init()
game = Game()

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#33CC66'))

manager = pygame_gui.UIManager((800, 600))

clock = pygame.time.Clock()
is_running = True
random_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                            text='Randomize',
                                            manager=manager)
#game.play(window_surface)
#test = pygame.image.load("Assets/Cards/2_of_clubs.png").convert_alpha()
while is_running:
    time_delta = 60/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            pygame.quit()
            exit()
        manager.process_events(event)
    manager.update(time_delta)
    game.draw_card(background)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    pygame.display.update()
    clock.tick(60)
