import pygame
import math
import random

# Spēles loga uzstādīšana.
pygame.init()
WIDTH, HEIGHT = 1000, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Karātavas")

# -----------------------------------------
#            Globālie mainīgie
# -----------------------------------------
# Bilžu ielādēšana.
bildes = []
for i in range(12):
    bilde = pygame.image.load("cilveks"+str(i) + ".png")
    bildes.append(bilde)

# Pogu izveidošana.
RADIUSS = 25
ATSTARPE = 15
burti = ['A','Ā','B','C','Č','D','E','Ē','F','G','Ģ','H','I','Ī','J','K','Ķ','L','Ļ','M','N','Ņ','O','P','R','S','Š','T','U','Ū','V','Z','Ž']
burti_poz = []
startsx = round((WIDTH - (RADIUSS * 2 + ATSTARPE) * 11) / 2)
startsy = 400
for i in range(33):
    x = startsx + ATSTARPE * 2 + ((RADIUSS * 2 + ATSTARPE) * (i % 11))
    y = startsy + ((i // 11) * (ATSTARPE + RADIUSS * 2))
    burti_poz.append([x, y, burti[i], True])

# Fonti
BURTU_FONTS = pygame.font.SysFont("segoe", 40)
VARDU_FONTS = pygame.font.SysFont("segoe", 60)
VIRSRAKSTU_FONTS = pygame.font.SysFont("segoe", 70)
MAZAIS_FONTS = pygame.font.SysFont("segoe", 30)

# Spēles mainīgie.
statuss = 0
minejumi = []
REZULTATS = 0
MINEJUMI_ATLIKUSI = 11
RAUNDS  = 1

# Krāsas
MELNS = 0, 0, 0
BALTS = 255, 255, 255

file = open("rezultats.txt", "r", encoding="utf-8")
AUGSTS_REZULTATS = file.read()

# -----------------------------------------
#               Funkcijas
# -----------------------------------------

# Augstākais rezultāts
def AUGSTS_REZULTATS(jauns_augstakais):
    global AUGSTS_REZULTATS
    file = open("rezultats.txt", "r", encoding="utf-8")
    AUGSTS_REZULTATS = file.read()
    if int(AUGSTS_REZULTATS) < REZULTATS:
        file = open("rezultats.txt", "w")
        file.write(str(jauns_augstakais))

def nejauss_vards():
    file = open("vardusaraksts.txt", "r", encoding="utf-8")
    rindas = file.readlines()
    vardusaraksts = []
    for i in rindas:
        i = i.strip("\n").upper()
        vardusaraksts.append(i)
    i = random.choice(vardusaraksts)
    return i


vards = nejauss_vards()


def zimet():
    win.fill(BALTS)
    # Teksti
    teksts4 = MAZAIS_FONTS.render(f"Raunds: {RAUNDS}", 1, MELNS)
    win.blit(teksts4, (750, 5))
    teksts2 = MAZAIS_FONTS.render(f"Rezultāts: {REZULTATS}", 1, MELNS)
    win.blit(teksts2, (750, 30))
    teksts3 = MAZAIS_FONTS.render(f"Dzīvības: {MINEJUMI_ATLIKUSI}", 1, MELNS)
    win.blit(teksts3, (70, 20))
    teksts = VIRSRAKSTU_FONTS.render("Karātavas", 1, MELNS)
    win.blit(teksts, (WIDTH/2 - teksts.get_width()/2, 10))
    attelotais_vards = ""
    for burts in vards:
        if burts in minejumi:
            attelotais_vards += burts + " "
        else:
            attelotais_vards += "_ "
    teksts = VARDU_FONTS.render(attelotais_vards, 1, MELNS)
    win.blit(teksts, (400, 200))
    # Pogas
    for burts in burti_poz:
        x, y, brt, redzams = burts
        if redzams:
            pygame.draw.circle(win, MELNS, (x, y), RADIUSS, 3)
            teksts = BURTU_FONTS.render(brt, 1, MELNS)
            win.blit(teksts, (x - teksts.get_width()/2, y - teksts.get_height()/2))

    win.blit(bildes[statuss], (150, 100))
    pygame.display.update()


def attelots_zinojums(zinojums):
    global vards
    win.fill(BALTS)
    teksts = VARDU_FONTS.render(zinojums, 1, MELNS)
    win.blit(teksts, (WIDTH / 2 - teksts.get_width() / 2, HEIGHT / 2 - teksts.get_height() / 2))
    if statuss == 11:
        answer = vards
        vards = VARDU_FONTS.render(f"Atbilde bija {answer}", 1, MELNS)
        win.blit(vards, (WIDTH / 2 - vards.get_width() / 2, 400))
    pygame.display.update()
    pygame.time.delay(3000)


def spelet_velreiz():
    win.fill(BALTS)
    teksts2 = MAZAIS_FONTS.render(f"Rezultāts: {REZULTATS}", 1, MELNS)
    win.blit(teksts2, (WIDTH / 2 - teksts2.get_width() / 2, 30))
    teksts = VARDU_FONTS.render("Vai Tu vēlies turpināt?(j/n)", 1, MELNS)
    win.blit(teksts, (WIDTH / 2 - teksts.get_width() / 2, HEIGHT / 2 - teksts.get_height() / 2))
    pygame.display.update()


def restart():
    global vards
    global statuss
    global minejumi
    global burti
    global MINEJUMI_ATLIKUSI
    global RAUNDS
    RAUNDS += 1
    RADIUSS = 25
    ATSTARPE = 15
    burti = ['A','Ā','B','C','Č','D','E','Ē','F','G','Ģ','H','I','Ī','J','K','Ķ','L','Ļ','M','N','Ņ','O','P','R','S','Š','T','U','Ū','V','Z','Ž']
    burti_poz = []
    startsx = round((WIDTH - (RADIUSS * 2 + ATSTARPE) * 13) / 2)
    startsy = 400
    for i in range(33):
        x = startsx + ATSTARPE * 2 + ((RADIUSS * 2 + ATSTARPE) * (i % 13))
        y = startsy + ((i // 13) * (ATSTARPE + RADIUSS * 2))
        burti_poz.append([x, y, burti[i], True])
    for burts in burti_poz:
        x, y, brt, redzams = burts
        if redzams:
            pygame.draw.circle(win, MELNS, (x, y), RADIUSS, 3)
            teksts = BURTU_FONTS.render(brt, 1, MELNS)
            win.blit(teksts, (x - teksts.get_width()/2, y - teksts.get_height()/2))
    MINEJUMI_ATLIKUSI = 11
    minejumi = []
    statuss = 0
    vards = nejauss_vards()
    AUGSTS_REZULTATS(REZULTATS)
    zimet()


def nosp_taust():
    global spelet
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                restart()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    AUGSTS_REZULTATS(REZULTATS)
                    spelet = False
    if pygame.time.delay(5000):
        pygame.quit()
      


def main():
    global statuss
    global spelet
    global REZULTATS
    global MINEJUMI_ATLIKUSI
    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in burti_poz:
                    x, y, brt, redzams = letter
                    if redzams:
                        dis = math.sqrt((x-m_x)**2 + (y-m_y)**2)
                        if dis < RADIUSS:
                            letter[3] = False
                            minejumi.append(brt)
                            if brt not in vards:
                                statuss += 1
                                MINEJUMI_ATLIKUSI -= 1

        zimet()

        uzvara = True
        for burts in vards:
            if burts not in minejumi:
                uzvara = False
                break
        if uzvara:
            REZULTATS += 1
            pygame.time.delay(1000)
            attelots_zinojums("Tu uzvarēji!")
            spelet_velreiz()
            pygame.time.delay(5000)
            nosp_taust()
            break

        if statuss == 11:
            pygame.time.delay(1000)
            attelots_zinojums("Tu zaudēji!")
            spelet_velreiz()
            pygame.time.delay(3000)
            nosp_taust()
            break


spelet = True
while spelet:
    main()
else:
    pygame.quit()
