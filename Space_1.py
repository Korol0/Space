from pygame import*

WIDTH, HEIGHT = 800, 600
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Space Shooter")

clock = time.Clock()

backround = transform.scale(image.load("101328650.jpg"), (WIDTH, HEIGHT))

while True:
    window.blit(backround, (0, 0))

    display.update()
    clock.tick(60)
