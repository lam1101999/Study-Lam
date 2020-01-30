import pygame,sys,os


def main():
    pygame.init()
    displayWidth = 800
    displayHeight = 800
    gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)

    pathCar = os.path.join(os.getcwd(),"Image\car1.png")
    carImage = pygame.image.load(pathCar).convert()
    pygame.display.set_caption("A Game")
    clock = pygame.time.Clock()
    crashed = False

    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            print(event)
        pygame.display.update()
        clock.tick(60)
        gameDisplay.blit(carImage,(50,50))
    pygame.quit()   
    quit()


if __name__ =='__main__':
 main()