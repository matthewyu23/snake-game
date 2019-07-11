import pygame
import random
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 600))
done = False
allPositions = [[0, 0]]
direction = "right"
snakeLength = 1
candyPosition = [random.randint(0, 60), random.randint(0, 60)]



while not done: 

    pygame.display.set_caption('Snake') 

    for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                    done = True

    for x in range(60): #draws the grid
        for y in range(60): 
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x * 10, y * 10, 9, 9)) 

    
    for x in range(len(allPositions)): #draws the snake
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(allPositions[x][0], allPositions[x][1], 9, 9))

    if direction == "right": #changing directions
        allPositions.insert(0, [allPositions[0][0]+10, allPositions[0][1]])
    if direction == "left": 
        allPositions.insert(0, [allPositions[0][0]-10, allPositions[0][1]])
    if direction == "up": 
        allPositions.insert(0, [allPositions[0][0], allPositions[0][1]-10])
    if direction == "down": 
        allPositions.insert(0, [allPositions[0][0], allPositions[0][1]+10])

    pressed = pygame.key.get_pressed() #controling direction
    if pressed[pygame.K_UP] and direction != "down": direction = "up"
    if pressed[pygame.K_DOWN] and direction != "up": direction = "down"
    if pressed[pygame.K_LEFT] and direction != "right": direction = "left"
    if pressed[pygame.K_RIGHT] and direction != "left": direction = "right"

    while len(allPositions) > snakeLength: 
        allPositions.pop()
    
    for x in range(1, len(allPositions)):
        if allPositions[x] == allPositions[0]:
            pygame.time.delay(1000)
            allPositions[0] = [0,0]
            snakeLength = 1
            direction = "right"
    
    if allPositions[0][0] < -10 or allPositions[0][0] > 600 or allPositions[0][1] < -10 or allPositions[0][1] > 600: 
        pygame.time.delay(1000)
        allPositions[0] = [0,0]
        snakeLength = 1
        direction = "right"

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(candyPosition[0]*10, candyPosition[1]*10, 9, 9)) #draws candy

    if allPositions[0][0] == candyPosition[0] * 10 and allPositions[0][1] == candyPosition[1] * 10: 
        snakeLength = snakeLength + 1
        candyPosition = [random.randint(0, 60), random.randint(0, 60)]

    pygame.display.flip() 
    screen.fill((0, 0, 0))
    clock.tick(15)