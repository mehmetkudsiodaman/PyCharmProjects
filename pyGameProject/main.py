import pygame as pg


pg.init()
screen = pg.display.set_mode((1000, 400))
running = True
counter = 0

X = screen.get_width() / 2
Y = screen.get_height() / 2

display_surface = pg.display.set_mode((X, Y))
pg.display.set_caption('Mouse counter')
font = pg.font.Font("Sendcat.ttf", 256)
text = font.render(str(counter), True, "Black", "White")
textRect = text.get_rect()

while running:
    display_surface.fill("White")
    display_surface.blit(text, textRect)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            counter += 1

    text = font.render(str(counter), True, "Black", "White")
    pg.display.update()
