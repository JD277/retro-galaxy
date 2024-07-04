for event in pygame.event.get():
        if event.type == pygame.KEYDOWN :
            condition = True
        if event.type == pygame.QUIT:
            running = False