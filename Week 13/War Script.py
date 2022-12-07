from deck import Deck
from player import Player
import pygame
import pygame_gui
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Aggie War')
window_surface = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

class Game:
    def __init__(self):
        self.deck = Deck()
        self.p1 = Player("Player 1")
        self.p2 = Player("Player 2")
        self.iterations = 0
        self.sprite1 = pygame.image.load("Assets/Cards/red_joker.png").convert_alpha()
        self.sprite2 = pygame.image.load("Assets/Cards/red_joker.png").convert_alpha()
        scale = 0.45
        self.sprite1 = pygame.transform.scale(self.sprite1, (int(self.sprite1.get_width() * scale), int(self.sprite1.get_height() * scale)))
        self.sprite2 = pygame.transform.scale(self.sprite2, (int(self.sprite2.get_width() * scale), int(self.sprite2.get_height() * scale)))

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
        
        scale = 0.45
        self.sprite1 = pygame.transform.scale(self.sprite1, (int(self.sprite1.get_width() * scale), int(self.sprite1.get_height() * scale)))
        self.sprite2 = pygame.transform.scale(self.sprite2, (int(self.sprite2.get_width() * scale), int(self.sprite2.get_height() * scale)))
        # print("images loaded")
        ################################

        self.draw_card(surface)

        ################################
        # print(f"{p1Name} drew {p1Card} and {p2Name} drew {p2Card}")
    
    def draw_card(self, surface):
        # print("draw card")
        surfaceWidth = surface.get_width()
        surfaceHeight = surface.get_height()
        sp1_rect = self.sprite1.get_rect(center = (surfaceWidth/4, surfaceHeight/2))
        sp2_rect = self.sprite2.get_rect(center = (surfaceWidth/4 + surfaceWidth/2, surfaceHeight/2))
        
        surface.blit(self.sprite1,sp1_rect)
        surface.blit(self.sprite2,sp2_rect)
        
    
    def play(self, surface):
        cards = self.deck.cards
        print("Begin the War!")
        if len(cards) >= 2:
            self.iterations += 1
            # response = input("Press 'q' to quit. Press any other key to play: ")
            # if response == 'q':
            #     break
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
            print(f"p1 wins: {self.p1.wins}")
            print(f"p2 wins: {self.p2.wins}")

            self.draw_score(surface)
            return False, None
            # self.sprite2 = pygame.transform.scale(self.sprite2, (int(self.sprite2.get_width() * scale), int(self.sprite2.get_height() * scale)))

        else:
            win = self.totalWinner(self.p1, self.p2)
            print(f"The war is over! {win} is the victor!")
            return True, win

    def draw_score(self, surface):
        pygame.font.init()
        pygame.display.flip()
        self.white = (255, 255, 255)
        self.font_path = "Assets/fonts/BebasNeue-Regular.ttf"
        self.myfont = pygame.font.Font(self.font_path, 32)
        self.myfont2 = pygame.font.Font(self.font_path, 40)
        p1_text = self.myfont.render(f"Player 1 has: {self.p1.wins} wins", 1, self.white)
        p2_text = self.myfont.render(f"Player 2 has: {self.p2.wins} wins", 1, self.white)
        iter_text = self.myfont2.render(f"Turns: {self.iterations}", 1, self.white)
        surfaceWidth = surface.get_width()
        surfaceHeight = surface.get_height()
        p1_rect = p1_text.get_rect(center = (surfaceWidth/4, surfaceHeight/8))
        p2_rect = p2_text.get_rect(center = (surfaceWidth/4 + surfaceWidth/2, surfaceHeight/8))
        iter_rect = iter_text.get_rect(center = (surfaceWidth/2, surfaceHeight/4+surfaceHeight/2+80))
        surface.blit(p1_text, p1_rect)
        surface.blit(p2_text, p2_rect)
        surface.blit(iter_text, iter_rect)

    def totalWinner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name + " is the winner!"
        if p1.wins < p2.wins:
            return p2.name + " is the winner!"
        return "It was a tie"
    
    def draw_winner(self, surface, winner):
        print(winner)
        font_path = "Assets/fonts/PressStart2P-Regular.ttf"
        myfont = pygame.font.Font(font_path, 32)
        surfaceWidth = surface.get_width()
        surfaceHeight = surface.get_height()
        win_text = myfont.render(f"{winner}", 1, self.white)
        win_rect = win_text.get_rect(center = (surfaceWidth/2, surfaceHeight/2))
        surface.blit(win_text, win_rect)
        
        
game = Game()

# background color and window size
background = pygame.Surface((800, 600))

manager = pygame_gui.UIManager((800, 600))

# Button test but i wanted to turn it into a randomizer for cards and stuff
clock = pygame.time.Clock()
is_running = True
random_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                            text='Randomize',
                                            manager=manager)
is_win = False
winner = None
#this code helps with performance and framrate issues
while is_running:
    time_delta = 60/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            pygame.quit()
            exit()
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == random_button:
                is_win, winner = game.play(background)
        manager.process_events(event)
    
    if is_win == True:
        background.fill(pygame.Color('#500000'))
        game.draw_winner(background, winner)
        game.draw_score(background)
        window_surface.blit(background, (0, 0))
    else:
        background.fill(pygame.Color('#500000'))
        manager.update(time_delta)
        game.draw_card(background)
        game.draw_score(background)
        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)
    
    

    pygame.display.update()
    clock.tick(60)
