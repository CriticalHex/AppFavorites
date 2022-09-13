import pygame
import random

class App:
    def __init__(self,x,y):
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.pos = (x,y)
        self.clicked = 0
        
    def draw(self,loc=None):
        if loc is None:
            pygame.draw.circle(screen, self.color, self.pos, 50)
            return
        pygame.draw.circle(screen, self.color, loc, 50)
        
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Favorite Apps")
MousePos = (0,0)

apps = list()
for i in range(4):
    for j in range(4):
        apps.append(App((j*110) + 225,(i*110) + 225))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LCTRL]:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            MousePos = pygame.mouse.get_pos()
            for a in apps:
                if MousePos[0] <= a.pos[0] + 50 and MousePos[1] <= a.pos[1] + 50 and MousePos[0] >= a.pos[0] - 50 and MousePos[1] >= a.pos[1] - 50:
                    a.clicked += 1
    
    apps.sort(key=lambda app: app.clicked,reverse=True)
    
    screen.fill((0,0,0))
    
    for a in apps:
        a.draw()
    
    for i in range(3):
        apps[i].draw(((i * 150) + 250,75))
        
    pygame.draw.line(screen, (255,255,255), (0,150), (800,150))
    
    pygame.display.flip()
    
pygame.quit()