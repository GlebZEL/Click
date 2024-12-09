import pygame
import sys
from random import randint
pygame.init()
clock = pygame.time.Clock()  # создаем игровой таймер
FPS = 40
window = pygame.display.set_mode((500, 500))
window.fill((200,255,255))  # заливка цвета фона
BLACK=(0,0,0)

class Area():
    def __init__(self,x,y,width,hight,color=None):
        self.rect=pygame.Rect( x,y,width,hight)
        self.fill_color=color
    def n_color(self,newcolor):
        self.fill_color=newcolor
    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)
    def outline(self, frame_color, thickness):
        pygame.draw.rect(window, frame_color, self.rect, thickness)
    
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)

class Label(Area):
    def set_text(self, text, fsize=12, text_color=BLACK) :
        self.text=pygame.font.SysFont('segoeprint', fsize).render(text, True, text_color)
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        window.blit(self.text, (self.rect.x + shift_x, self.rect.y + shift_y))

cards=[]
num_cards=4
X = 80
for i in range(num_cards):
    body=Label(X,320,70,100,(191,127,48))
    body.set_text('Click',35)
    body.draw(3,20)
    body.outline((124,138,61),7)
    cards.append(body)
    X+=90
time_square=Label(10,10,70,100,(200,255,255))
time_square.set_text('Время:',45)
time_square.draw(3,20)
stopwatch=Label(10,60,70,85,(200,255,255))
stopwatch.set_text('10',45)
stopwatch.draw(3,20)
counter_1=Label(380,10,70,100,(200,255,255))
counter_1.set_text('Счет:',45)
counter_1.draw(3,20)
counter_2=Label(385,60,70,85,(200,255,255))
counter_2.set_text('0',45)
counter_2.draw(3,20)

wait=0

start_time = 10
timer_event = pygame.USEREVENT
pygame.time.set_timer(timer_event, 1000)

points=0

game_play=True

while True:
    if game_play:

        if wait==0:
            wait=25
            click=randint(1, num_cards)
            for i in range(num_cards):
                cards[i].n_color((191,127,48))
                if(i+1)==click:
                    cards[i].draw(3,20)
                else:
                    cards[i].fill()
                cards[i].outline((124,138,61),7)
        else:
            wait-=1
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                x,y=event.pos
                for i in range(num_cards):
                    if cards[i].collidepoint(x,y):
                        if i+1==click:
                            cards[i].n_color((85,175,100))
                            points+=1
                        else:
                            cards[i].n_color((140,34,51))
                            points-=1
                        cards[i].fill()
                        cards[i].outline((124,138,61),7)

                        counter_2.set_text(str(points), 45)
                        counter_2.draw(3,20)

            if event.type == timer_event:
                start_time -= 1
                stopwatch.set_text(str(start_time),45)
                stopwatch.draw(3,20)
                
                if start_time==0:
                    timer_event=0

                    game_play=False

                    if game_play==False:
                        loose=Label(0,0,500,500,(55,4,112))
                        loose.set_text('Время вышло. Ты проиграл!',35,(210,95,95))

                        loose.draw(100,220)
                
                if points >=5:
                    timer_event=0

                    game_play=False

                    if game_play==False:
                        win=Label(0,0,500,500,(223,162,162))
                        win.set_text('Ты выиграл!',35,(32,91,91))
                        win.draw(100,270)
    else:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

    pygame.display.update()

    clock.tick(FPS)