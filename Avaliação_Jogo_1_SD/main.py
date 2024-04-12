import pygame
import random
from player1 import Player1
from player2 import Player2

pygame.init()

# Definições iniciais do ecrã
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Python/Sobrevivênvia no Limite")

# upload de imagens
background = pygame.image.load('ice.jpg').convert()
collectible_image = pygame.image.load('bag.png').convert_alpha()

# Relógio para controlo de frames
clock = pygame.time.Clock()

# Tamanho do quadrado na grid
square_size = 80

# Criação dos jogadores
player1 = Player1((150, 150), square_size, screen_width, screen_height)
player2 = Player2((300, 300), square_size, screen_width, screen_height)
# Pontuações iniciais
score_player1 = 0
score_player2 = 0

# timer
start_time = pygame.time.get_ticks()

# Lista de posições dos colecionáveis
collectible_positions = []


# Função para adicionar novos colecionáveis
def add_collectibles(num_collectibles):
    for _ in range(num_collectibles):
        # Posição central do quadrado
        square_center_x = random.randint(0, (screen_width // square_size) - 1) * square_size + (square_size // 2)
        square_center_y = random.randint(0, (screen_height // square_size) - 1) * square_size + (square_size // 2)
        collectible_positions.append((square_center_x - collectible_image.get_width() // 2,
                                      square_center_y - collectible_image.get_height() // 2))


# Posicionamento inicial dos colecionáveis
add_collectibles(5)

# Variável de controlo de fim de jogo
game_over = False

# Loop principal do jogo
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # Passa os eventos para ambos os jogadores
        player1.handle_event(event)
        player2.handle_event(event)

    # Atualizações dos jogadores
    player1.update(player1.direction)
    player2.update(player2.direction)

    # Verifica colisão com as malas
    for position in collectible_positions[:]:
        if player1.rect.colliderect(
                pygame.Rect(position[0], position[1], collectible_image.get_width(), collectible_image.get_height())):
            score_player1 += 1
            collectible_positions.remove(position)

        if player2.rect.colliderect(
                pygame.Rect(position[0], position[1], collectible_image.get_width(), collectible_image.get_height())):
            score_player2 += 1
            collectible_positions.remove(position)

    # Calcula o tempo decorrido
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000

    # Desenha o background
    screen.blit(background, (0, 0))

    # Desenha as grades
    for x in range(0, screen_width, square_size):  # Linhas verticais
        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, screen_height))
    for y in range(0, screen_height, square_size):  # Linhas horizontais
        pygame.draw.line(screen, (0, 0, 0), (0, y), (screen_width, y))

    # Desenha os colecionáveis
    for position in collectible_positions:
        screen.blit(collectible_image, position)

    # Desenha os jogadores
    screen.blit(player1.image, player1.rect)
    screen.blit(player2.image, player2.rect)

    # Desenha as pontuações dos jogadores
    font = pygame.font.Font(None, 36)
    score_text_player1 = font.render(f'Jogador 1 Pontuação: {score_player1}', True, (0, 0, 0))
    score_text_player2 = font.render(f'Jogador 2 Pontuação: {score_player2}', True, (0, 0, 0))
    screen.blit(score_text_player1, (10, 10))
    screen.blit(score_text_player2, (10, 50))

    # Desenha o tempo decorrido
    timer_text = font.render(f' {elapsed_time} s', True, (0, 0, 0))
    screen.blit(timer_text, (screen_width - timer_text.get_width() - 10, 10))

    # Adiciona novos colecionáveis
    if len(collectible_positions) < 5:
        add_collectibles(2)

    # Verifica condição de fim de jogo
    if elapsed_time >= 30:
        game_over = True

    # Atualiza o ecrã
    pygame.display.flip()
    clock.tick(10)  # frames

# Determina o vencedor
winner = "Jogador 1" if score_player1 > score_player2 else "Jogador 2" if score_player2 > score_player1 else "Empate"

# Exibe o vencedor na tela
font_winner = pygame.font.Font(None, 50)
winner_text = font_winner.render(f'Parabéns: {winner}', True, (0, 0, 0))
screen.blit(winner_text, (screen_width // 2 - 150, screen_height // 2 - 25))
pygame.display.flip()

# Espera-se uns segundos antes de encerrar(3 ssegundos)
pygame.time.delay(3000)

# Encerra o Pygame
pygame.quit()
