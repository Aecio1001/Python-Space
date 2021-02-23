class Settings():
	'''Uma classe para armazenar todas as configurações do jogo.'''

	def __init__(self):
		'''Inicializa as configurações do jogo.'''
		# Configurações da tela
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (230, 230, 230)

		# Configurações da espaçonave
		self.ship_speed_factor = 1.5