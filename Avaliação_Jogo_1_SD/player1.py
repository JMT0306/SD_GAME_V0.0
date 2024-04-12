import pygame

class Player1(pygame.sprite.Sprite):
    def __init__(self, position, square_size, screen_width, screen_height):
        pygame.sprite.Sprite.__init__(self)
        # Carrega a imagem do jogador
        self.sheet = pygame.image.load('teste1.png')
        # Define a área  inicial
        self.sheet.set_clip(pygame.Rect(0, 0, 52, 76))
        # Cria a imagem do jogador a partir da área
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        # Obtém o retângulo da imagem
        self.rect = self.image.get_rect()
        # Define a posição inicial do jogador
        self.rect.topleft = position
        # Índice do frame atual
        self.frame = 0
        # Direção inicial do jogador
        self.direction = 'stand_down'
        # Tamanho do quadrado na grade
        self.square_size = square_size
        # Largura da ecrã
        self.screen_width = screen_width
        # Altura da ecrã
        self.screen_height = screen_height

    def update(self, direction):
        # Atualiza a direção do jogador
        if direction != self.direction:
            self.direction = direction

        # Move o jogador na direção especificada
        if direction == 'left':
            self.rect.x = max(0, self.rect.x - self.square_size)
        elif direction == 'right':
            self.rect.x = min(self.screen_width - self.rect.width, self.rect.x + self.square_size)
        elif direction == 'up':
            self.rect.y = max(0, self.rect.y - self.square_size)
        elif direction == 'down':
            self.rect.y = min(self.screen_height - self.rect.height, self.rect.y + self.square_size)

        # Garante que o jogador se mexa apenas de quadrado em quadrado
        self.rect.x = (self.rect.x // self.square_size) * self.square_size
        self.rect.y = (self.rect.y // self.square_size) * self.square_size

    def handle_event(self, event):
        # Manipula os eventos de teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.direction = 'left'
            elif event.key == pygame.K_RIGHT:
                self.direction = 'right'
            elif event.key == pygame.K_UP:
                self.direction = 'up'
            elif event.key == pygame.K_DOWN:
                self.direction = 'down'
        elif event.type == pygame.KEYUP:
            # faz o reset  da direção quando a tecla é solta
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
                self.direction = 'stand_down'
