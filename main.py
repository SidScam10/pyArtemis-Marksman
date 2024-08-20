import pygame, sys
import random
import time

pygame.init()
score = 0
size = 1280, 720
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Aim Trainer")
clock = pygame.time.Clock()

white = (255, 255, 255)
red = (225, 0, 0)
black = (0, 0, 0)

font = pygame.font.SysFont("comicsans", 30)
target = pygame.image.load("square_target.png")
target = pygame.transform.scale(target, (90, 90))
resetsound=pygame.mixer.Sound('Reset_sound.wav')
hitsound=pygame.mixer.Sound('pp7_silenced.wav')
misssound=pygame.mixer.Sound('miss.wav')
music=pygame.mixer.music.load('BG_music.mpga')
pygame.mixer.music.play(-1)

sum = 0
avg = 0.0
miss = 0
curtime = 0
btpushtime = 0
prevtime = 0
x = random.randint(0, 1190)
y = random.randint(17, 630)
c = 0

run = True
while run:
    screen.fill(black)
    for event in pygame.event.get():
        mx, my = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mx >= x and my >= y and mx <= x + 90 and my <= y + 90:
                hitsound.play()
                x = random.randint(0, 1170)
                y = random.randint(17, 576)
                score += 1
                btpushtime = pygame.time.get_ticks()
                sum = sum + btpushtime - prevtime
            elif mx >= 1200 and my >= 690 and mx <= 1265 and my <= 706:
                resetsound.play()
                score = 0
                miss = 0
                btpushtime = pygame.time.get_ticks()
                sum = 0
                avg = 0.0
                x = random.randint(0, 1190)
                y = random.randint(17, 630)
            else:
                misssound.play()
                miss += 1
        prevtime = btpushtime
        curtime = pygame.time.get_ticks()
        if score != 0 and c == 0:
            avg = sum // score
        stop = font.render("Avg. Reaction Time: " + str(avg) + "ms", 1, white)
        lives = font.render("Lives: " + str((3 - miss)), 1, red)
        if mx >= 1200 and my >= 690 and mx <= 1265 and my <= 706:
            Reset = font.render("RESET", 1, red)
        else:
            Reset = font.render("RESET", 1, white)
        scoretext = font.render("Score:" + str(score), 1, red)
        screen.blit(scoretext, (1190, 5))
        screen.blit(stop, (5, 700))
        screen.blit(Reset, (1200, 690))
        screen.blit(target, (x, y))
        screen.blit(lives, (5, 5))
        if miss == 3:
            if score == 0:
                avg = 0
            else:
                avg = sum // score
            print("-----------------------------Result-----------------------------")
            print("Lives Lost=3")
            print("Score=", score)
            print("Average Reaction Time:", avg, "ms")
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if score != 0:
                    avg = sum // score
                print(
                    "-----------------------------Result-----------------------------"
                )
                print("Lives Lost=", miss, sep="")
                print("Score=", score)
                print("Average Reaction Time:", avg, "ms")
                run = False
        elif event.type == pygame.QUIT:
            if score != 0:
                avg = sum // score
            print("-----------------------------Result-----------------------------")
            print("Lives Lost=", miss, sep="")
            print("Score=", score)
            print("Average Reaction Time:", avg, "ms")
            run = False
        pygame.display.update()
    clock.tick(60)
if avg == 0.0:
    print("Try Again")
elif avg <= 200 and avg > 0:
    print("Grade=S")
    print("GOD")
elif avg <= 350 and avg > 200:
    print("Grade=A+")
    print("GREAT")
elif avg <= 600 and avg > 350:
    print("Grade=A")
    print("GOOD")
elif avg <= 700 and avg > 600:
    print("Grade=B")
    print("AVERAGE")
elif avg <= 950 and avg > 700:
    print("Grade=C")
    print("BAD")
elif avg <= 1150 and avg > 950:
    print("Grade=D")
    print("REALLY BAD")
else:
    print("Grade=F")
    print("GIT GUD")
print("-----------------------------Result-----------------------------")
pygame.quit()
