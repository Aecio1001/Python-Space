# Importes de bibliotecas 
import sys, pygame

def run_game():
	#Inicializa o jogo e cria um objeto para a tela
	pygame.init()
	ia_settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# Define a cor do plano de fundo
	bg_color = (0, 230, 0)

	#Inicia o laço principal do jogo
	while True:

		#Observa eventos de teclado e de mouse
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		#Redesenha a tela a cada passagem pelo laço
		screen.fill(ai_settings.bg_color)

		#Deixa a tela mais recente visivel
		pygame.display.flip()

run_game()