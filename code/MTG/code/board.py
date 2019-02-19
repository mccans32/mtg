import pygame

pygame.init()
pygame.mixer.init()
PLAYER_1_HAND_SPRITE_CARD_GROUP = pygame.sprite.Group()
PLAYER_2_HAND_SPRITE_CARD_GROUP = pygame.sprite.Group()
PLAYER_1_LAND_SPRITE_CARD_GROUP = pygame.sprite.Group()
PLAYER_2_LAND_SPRITE_CARD_GROUP = pygame.sprite.Group()


class CardSprite(pygame.sprite.Sprite):
    # sprite class for all teh cards
    def __init__(self, card, x, y, w, h, back_texture = None):
            pygame.sprite.Sprite.__init__(self)
            if back_texture == None:
                card_texture = pygame.image.load(card.texture)            
            else:
                card_texture = pygame.image.load(back_texture) 
            self.image = pygame.transform.scale(card_texture,(int(w), int(h)))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.clicked = False
            self.card = card


class BoardSection():

    def __init__(self, screen, name, x, y, w, h, colour, is_border=True):
        self.screen = screen
        self.colour = colour
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.w = int(w)
        self.h = int(h)
        self.is_border = is_border
        self.border_size = int(screen.get_width()*0.002)

    def draw(self):
        if self.is_border:
            pygame.draw.rect(self.screen, (0,0,0), [self.x, self.y, self.w , self.h])
            pygame.draw.rect(self.screen, self.colour, [self.x + self.border_size, self.y + self.border_size, self.w - (2*self.border_size), self.h - (2* self.border_size)])
        else:
            pygame.draw.rect(self.screen, self.colour, [self.x, self.y, self.w, self.h])


class Board():

    def __init__(self, display, display_size, player_1, player_2):
        self.display = display
        self.display_size = display_size
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_1_hand_box = None
        self.player_2_hand_box = None
        self.player_1_land_box = None
        self.player_2_land_box = None
        self.player_1_graveyard = None
        self.player_2_graveyard = None
        self.player_1_battlefield_box = None
        self.player_2_battlefield_box = None
        self.player_1_deck = None
        self.player_2_deck = None
        self.player_1_life_sec = None
        self.player_2_life_sec = None

    def draw_hand(self, player):
        cards = player.hand
        if player == self.player_1:
            PLAYER_1_HAND_SPRITE_CARD_GROUP.empty()
            if len(cards) <= 8:
                padding_w = (self.player_1_hand_box.w/8)/8
                card_h = (self.player_1_hand_box.h/10)*8
                card_w = (card_h*63)/88
                i = 0
                while i < len(cards):
                    x = self.player_1_hand_box.x + (padding_w*(i+1)) + (card_w*(i))
                    y = self.player_1_hand_box.y + (self.player_1_hand_box.h - card_h)/2
                    card_sprite = CardSprite(cards[i] , x, y, card_w, card_h)
                    PLAYER_1_HAND_SPRITE_CARD_GROUP.add(card_sprite)
                    i += 1
            PLAYER_1_HAND_SPRITE_CARD_GROUP.draw(self.display)
        else:
            PLAYER_2_HAND_SPRITE_CARD_GROUP.empty()
            if len(cards) <= 8:
                padding_w = (self.player_1_hand_box.w/8)/8
                card_h = (self.player_1_hand_box.h/10)*8
                card_w = (card_h*63)/88
                i = 0
                while i < len(cards):
                    x = self.player_2_hand_box.x + (padding_w*(i+1)) + (card_w*(i))
                    y = self.player_2_hand_box.y + (self.player_2_hand_box.h - card_h)/2
                    card_sprite = CardSprite(cards[i], x, y, card_w, card_h, "./images/cardback.jpg")
                    PLAYER_2_HAND_SPRITE_CARD_GROUP.add(card_sprite)
                    i += 1
            PLAYER_2_HAND_SPRITE_CARD_GROUP.draw(self.display)


    def draw_land(self, player):
        return





    def draw_board(self):
        player_1 = self.player_1
        player_2 = self.player_2
        display = self.display
        (display_w, display_h) = self.display_size

        display.fill((255,255,255))



        ## Graveyards##########################################################################
        player_1_graveyard_x = 0
        player_1_graveyard_y = (display_h/16)*13
        player_1_graveyard_w = (display_w/8)
        player_1_graveyard_h = (display_h/16)*3
        player_1_graveyard_colour = (165, 165, 165)

        player_1_graveyard = BoardSection(display, "graveyard", player_1_graveyard_x, player_1_graveyard_y, player_1_graveyard_w, player_1_graveyard_h, player_1_graveyard_colour)
        self.player_1_graveyard = player_1_graveyard
        player_1_graveyard.draw()

        player_2_graveyard_x = player_1_graveyard_x
        player_2_graveyard_y = 0
        player_2_graveyard_w = player_1_graveyard_w
        player_2_graveyard_h = player_1_graveyard_h
        player_2_graveyard_colour = player_1_graveyard_colour

        player_2_graveyard = BoardSection(display, "graveyard", player_2_graveyard_x, player_2_graveyard_y, player_2_graveyard_w, player_2_graveyard_h, player_2_graveyard_colour)
        self.player_2_graveyard = player_2_graveyard
        player_2_graveyard.draw()

        player_1_graveyard_box_w = player_1_graveyard_w*(0.33)
        player_1_graveyard_box_h = player_1_graveyard_box_w*(88/63)
        player_1_graveyard_box_x = player_1_graveyard_x + (player_1_graveyard_w*(0.5))
        player_1_graveyard_box_y = player_1_graveyard_y + ((player_1_graveyard_h-player_1_graveyard_box_h)/2)
        player_1_graveyard_box_colour = (255,255,255)

        player_1_graveyard_box = BoardSection(display, "graveyard_box", player_1_graveyard_box_x, player_1_graveyard_box_y, player_1_graveyard_box_w, player_1_graveyard_box_h, player_1_graveyard_box_colour)
        player_1_graveyard_box.draw()

        player_2_graveyard_box_w = player_1_graveyard_box_w
        player_2_graveyard_box_h = player_1_graveyard_box_h
        player_2_graveyard_box_x = player_1_graveyard_box_x
        player_2_graveyard_box_y = player_2_graveyard_y + ((player_2_graveyard_h-player_2_graveyard_box_h)/2)
        player_2_graveyard_box_colour = player_1_graveyard_box_colour

        player_2_graveyard_box = BoardSection(display, "graveyard_box", player_2_graveyard_box_x, player_2_graveyard_box_y, player_2_graveyard_box_w, player_2_graveyard_box_h, player_2_graveyard_box_colour)
        player_2_graveyard_box.draw()

        graveyard_font = pygame.font.Font(pygame.font.get_default_font(), int(player_1_graveyard_h*0.5))

        player_1_graveyard_text = graveyard_font.render(str(len(player_1.graveyard)), False, (0,0,0))
        player_1_graveyard_text_rec = player_1_graveyard_text.get_rect()
        player_1_graveyard_text_rec.center = ((player_1_graveyard_x+(player_1_graveyard_w/4)), (player_1_graveyard_y+(player_1_graveyard_h/2)))
        display.blit(player_1_graveyard_text, player_1_graveyard_text_rec)

        player_2_graveyard_text = graveyard_font.render(str(len(player_2.graveyard)), False, (0,0,0))
        player_2_graveyard_text_rec = player_2_graveyard_text.get_rect()
        player_2_graveyard_text_rec.center = ((player_2_graveyard_x+(player_2_graveyard_w/4)), (player_2_graveyard_y+(player_2_graveyard_h/2)))
        display.blit(player_2_graveyard_text, player_2_graveyard_text_rec)

        #### Hands ####################################################
        player_1_hand_x = player_1_graveyard_x + player_1_graveyard_w
        player_1_hand_y = player_1_graveyard_y
        player_1_hand_w = (display_w/8)*6
        player_1_hand_h = player_1_graveyard_h
        player_1_hand_colour = (37, 236, 247)

        player_1_hand = BoardSection(display, "hand", player_1_hand_x, player_1_hand_y, player_1_hand_w, player_1_hand_h, player_1_hand_colour)
        self.player_1_hand_box = player_1_hand
        player_1_hand.draw()

        player_2_hand_x = player_2_graveyard_x + player_2_graveyard_w
        player_2_hand_y = player_2_graveyard_y
        player_2_hand_w = player_1_hand_w
        player_2_hand_h = player_1_hand_h
        player_2_hand_colour = player_1_hand_colour

        player_2_hand = BoardSection(display, "hand", player_2_hand_x, player_2_hand_y, player_2_hand_w, player_2_hand_h, player_2_hand_colour)
        self.player_2_hand_box = player_2_hand
        player_2_hand.draw()
        ###################################################################

       ## Decks ######################################################################################
        player_1_deck_x = player_1_hand_x + player_1_hand_w
        player_1_deck_y = player_1_hand_y
        player_1_deck_w = player_1_graveyard_w
        player_1_deck_h = player_1_graveyard_h
        player_1_deck_colour = (0, 165, 165)

        player_1_deck = BoardSection(display, "deck", player_1_deck_x, player_1_deck_y, player_1_deck_w, player_1_deck_h, player_1_deck_colour)
        self.player_1_deck = player_1_deck
        player_1_deck.draw()
        
        player_2_deck_x = player_1_deck_x
        player_2_deck_y = player_2_hand_y
        player_2_deck_w = player_1_deck_w
        player_2_deck_h = player_1_deck_h
        player_2_deck_colour = player_1_deck_colour

        player_2_deck = BoardSection(display, "deck", player_2_deck_x, player_2_deck_y, player_2_deck_w, player_2_deck_h, player_2_deck_colour)
        player_2_deck.draw()

        player_1_deck_box_w = player_1_graveyard_box_w
        player_1_deck_box_h = player_1_graveyard_box_h
        player_1_deck_box_x = player_1_deck_x + (player_1_deck_w*(0.5))
        player_1_deck_box_y = player_1_deck_y + ((player_1_deck_h-player_1_deck_box_h)/2)
        player_1_deck_box_colour = (255,255,255)

        player_1_deck_box = BoardSection(display, "deck_box", player_1_deck_box_x, player_1_deck_box_y, player_1_deck_box_w, player_1_deck_box_h, player_1_deck_box_colour)
        player_1_deck_box.draw()

        player_2_deck_box_w = player_1_deck_box_w
        player_2_deck_box_h = player_1_deck_box_h
        player_2_deck_box_x = player_1_deck_box_x
        player_2_deck_box_y = player_2_deck_y + ((player_2_deck_h-player_2_deck_box_h)/2)
        player_2_deck_box_colour = player_1_deck_box_colour

        player_2_deck_box = BoardSection(display, "deck_box", player_2_deck_box_x, player_2_deck_box_y, player_2_deck_box_w, player_2_deck_box_h, player_2_deck_box_colour)
        player_2_deck_box.draw()

        deck_font = pygame.font.Font(pygame.font.get_default_font(), int(player_1_deck_w*0.4))

        player_1_deck_text = deck_font.render(str(player_1.deck.size), False, (0,0,0))
        player_1_deck_text_rec = player_1_deck_text.get_rect()
        player_1_deck_text_rec.center = ((player_1_deck_x+(player_1_deck_w/4)), (player_1_deck_y+(player_1_deck_h/2)))
        display.blit(player_1_deck_text, player_1_deck_text_rec)

        player_2_deck_text = deck_font.render(str(player_2.deck.size), False, (0,0,0))
        player_2_deck_text_rec = player_2_deck_text.get_rect()
        player_2_deck_text_rec.center = ((player_2_deck_x+(player_2_deck_w/4)), (player_2_deck_y+(player_2_deck_h/2)))
        display.blit(player_2_deck_text, player_2_deck_text_rec)
        #############################################################################################################################

        ## Lands ###########################################################
        player_1_lands_x = 0
        player_1_lands_y = (display_h/16)*11
        player_1_lands_w = (display_w/8)*7
        player_1_lands_h = display_h - player_1_lands_y - player_1_graveyard_h
        player_1_lands_colour = (0, 255, 0)

        player_1_lands = BoardSection(display, "lands", player_1_lands_x, player_1_lands_y, player_1_lands_w, player_1_lands_h, player_1_lands_colour)
        self.player_1_land_box = player_1_lands
        player_1_lands.draw()

        player_2_lands_x = 0
        player_2_lands_y = (display_h/16)*3
        player_2_lands_w = player_1_lands_w
        player_2_lands_h = player_1_lands_h
        player_2_lands_colour = player_1_lands_colour

        player_2_lands = BoardSection(display, "lands", player_1_lands_x, player_2_lands_y, player_2_lands_w, player_2_lands_h, player_2_lands_colour)
        self.player_2_land_box = player_2_lands
        player_2_lands.draw()
        #######################################################################

       ## Life Sections ####################################################################################################
        player_1_life_sec_x = player_1_lands_x + player_1_lands_w
        player_1_life_sec_y = player_1_lands_y
        player_1_life_sec_w = player_1_deck_w
        player_1_life_sec_h = player_1_lands_h
        player_1_life_sec_colour = (222, 188, 224)

        player_1_life_sec = BoardSection(display, "life_sec", player_1_life_sec_x, player_1_life_sec_y, player_1_life_sec_w, player_1_life_sec_h, player_1_life_sec_colour)
        self.player_1_life_sec = player_1_life_sec
        player_1_life_sec.draw()

        player_2_life_sec_x = player_1_life_sec_x
        player_2_life_sec_y = player_2_lands_y
        player_2_life_sec_w = player_1_life_sec_w
        player_2_life_sec_h = player_1_life_sec_h
        player_2_life_sec_colour = player_1_life_sec_colour

        player_2_life_sec = BoardSection(display, "life_sec", player_2_life_sec_x, player_2_life_sec_y, player_2_life_sec_w, player_2_life_sec_h, player_2_life_sec_colour)
        self.player_2_life_sec = player_2_life_sec
        player_2_life_sec.draw()

        player_1_life_w = (player_1_life_sec_w*0.5)
        player_1_life_h = player_1_life_w
        player_1_life_x = player_1_life_sec_x + (player_1_life_w/2)
        player_1_life_y = player_1_life_sec.y + ((player_1_life_sec.h - player_1_life_h) / 2)
        player_1_life_colour = (255, 255, 255)

        player_1_life = BoardSection(display, "life", player_1_life_x, player_1_life_y, player_1_life_w, player_1_life_h, player_1_life_colour)
        player_1_life.draw()

        player_2_life_w = player_1_life_w
        player_2_life_h = player_2_life_w
        player_2_life_x = player_1_life_x
        player_2_life_y = player_2_life_sec_y + ((player_2_life_sec_h - player_2_life_h) / 2)
        player_2_life_colour = player_1_life_colour

        player_2_life = BoardSection(display, "life", player_2_life_x, player_2_life_y, player_2_life_w, player_2_life_h, player_2_life_colour)
        player_2_life.draw()

        life_font = pygame.font.Font(pygame.font.get_default_font(), int(player_1_life.h*0.5))

        player_1_life_text = life_font.render(str(player_1.life), False, (0,0,0))
        player_1_life_rec = player_1_life_text.get_rect()
        player_1_life_rec.center = ((player_1_life_sec_x+(player_1_life_sec_w/2)), (player_1_life_sec_y+(player_1_life_sec_h/2)))
        display.blit(player_1_life_text, player_1_life_rec)

        player_2_life_text = life_font.render(str(player_2.life), False, (0,0,0))
        player_2_life_rec = player_2_life_text.get_rect()
        player_2_life_rec.center = ((player_2_life_sec_x+(player_2_life_sec_w/2)), (player_2_life_sec_y+(player_2_life_sec_h/2)))
        display.blit(player_2_life_text, player_2_life_rec)
        ###################################################################################################################

        ## Battlefields####################################################################
        player_1_battlefield_x = 0
        player_1_battlefield_y = display_h/2
        player_1_battlefield_w = display_w
        player_1_battlefield_h = (display_h/2) - player_1_graveyard_h - player_1_lands_h
        player_1_battlefield_colour = (211, 132, 6)

        player_1_battlefield = BoardSection(display, "battlefield", player_1_battlefield_x, player_1_battlefield_y, player_1_battlefield_w, player_1_battlefield_h, player_1_battlefield_colour)
        self.player_1_battlefield_box = player_1_battlefield
        player_1_battlefield.draw()

        player_2_battlefield_x = 0
        player_2_battlefield_y = player_2_graveyard_h + player_2_lands_h
        player_2_battlefield_w = player_1_battlefield_w
        player_2_battlefield_h = player_1_battlefield_h
        player_2_battlefield_colour = player_1_battlefield_colour

        player_2_battlefield = BoardSection(display, "battlefield", player_2_battlefield_x, player_2_battlefield_y, player_2_battlefield_w, player_2_battlefield_h, player_2_battlefield_colour)
        self.player_2_battlefield_box = player_2_battlefield
        player_2_battlefield.draw()
        ##############

