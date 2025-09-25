import random
import time
import pygame
pygame.init()
ss = [1920,1080]
screen = pygame.display.set_mode((ss[0],ss[1]))
clock = pygame.time.Clock()
running = True
ti = 0
slider = pygame.rect.Rect(960-200,760,400,50)
f = (960-200,760,50,50)
lts = []
flts = []
k=0
simsp = 3*(f[0]-760)+10
rerand = pygame.rect.Rect(960-100,900,200,75)
def text(size,color,text,loc):
    font = pygame.font.SysFont('Arial', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (loc)
    screen.blit(text_surface, text_rect)
for i in range(1,121):
    k+=1
    lts.append(k)
    flts.append(k)
random.shuffle(lts)
flts.sort()
d = True
i=0
h=2
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((40,40,40))
    screen.fill((20,20,20),(1920-1560,0,1200,720))
    if d == True:
        if lts[i] > lts[i+1]:
            r = lts[i]
            lts[i] = lts[i+1]
            lts[i+1] = r
            del r
            continue
        for o in range(len(lts)):
            pygame.draw.rect(screen,(100,255,100),(1920-1560+o*10,720-lts[o]*5,10,lts[o]*5))
            if i == o:
                pygame.draw.rect(screen,(255,100,100),(1920-1560+o*10,720-lts[o]*5,10,lts[o]*5))
        i+=1
        ti+=1
        if i > len(lts)-h:
            h+=1
            i=0
        if flts == lts:
            i=0
            d = False
    #continue to render once done
    if d == False:
        for o in range(len(lts)):
                pygame.draw.rect(screen,(100,255,100),(1920-1560+o*10,720-lts[o]*5,10,lts[o]*5))
                if i == o:
                    pygame.draw.rect(screen,(255,100,100),(1920-1560+o*10,720-lts[o]*5,10,lts[o]*5))
    m = pygame.mouse.get_pressed(3)
    mp = pygame.mouse.get_pos()
    
    pygame.draw.rect(screen,(200,200,200),slider)
    pygame.draw.rect(screen,(150,150,170),rerand)

    if slider.collidepoint(mp[0]+24,mp[1]):
        pygame.draw.rect(screen,(255,255,255),slider)
        if m[0]:
            f = (mp[0]-25,760,50,50)
            if f[0] < 960-200:
                f = (960-200,760,50,50)
            simsp = 3*(f[0]-760)+10
            pygame.draw.rect(screen,(100,100,100),f)
    if rerand.collidepoint(mp[0],mp[1]):
        pygame.draw.rect(screen,(200,200,240),rerand)
        if m[0]:
            d = True
            i = 0
            h = 2
            ti = 0
            random.shuffle(lts)
    pygame.draw.rect(screen,(100,100,100),f)
    text(48,(255,255,255),f'FPS: {simsp}',(960,840))
    text(28,(255,255,255),f'Iterations: {ti}',(1920-1560+120,25))
    text(36,(255,255,255),'Re-Random',(960,935))
    pygame.display.flip()
    clock.tick(simsp)
pygame.quit()