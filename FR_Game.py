import pygame
pygame.init()

win = pygame.display.set_mode((600, 600))

pygame.display.set_caption("Freya Ridings Kite")

walkRight = pygame.image.load('JP_1.png')
walkLeft = pygame.image.load('JP_1.png')
bg = pygame.image.load('bg.png')
char = pygame.image.load('JP_1.png')

clock = pygame.time.Clock()

class player:

    def __init__(self, name, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.right = False
        self.left = False
        self.walkCount = 0
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft, (self.x, self.y))
                #win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                #self.walkCount += 1
            elif self.right:
                win.blit(walkLeft, (self.x, self.y))
                #win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                #self.walkCount +=1
        else:
            if self.right:
                win.blit(walkLeft, (self.x, self.y))
                #win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft, (self.x, self.y))
                #win.blit(walkLeft[0], (self.x, self.y))

def redrawGameWindow():
    pygame.display.update()
    win.blit(bg, (0,0))
    man.draw(win)
    pygame.display.update()


#mainloop
man = player('man', 300, 410, 64, 64)
run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
    if keys[pygame.K_RIGHT] and man.x < 600 - man.width - man.vel:
        man.x += man.vel
    if not(man.isJump):
        if keys[pygame.K_UP] and man.y > man.vel:
            man.y -= man.vel
        if keys[pygame.K_DOWN] and man.y < 600 - man.height - man.vel:
            man.y += man.vel
    if not(man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.25 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
    redrawGameWindow()


pygame.QUIT()