import pygame
import sys
from objects import Button
import menu
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

BACKGROUND_COLOR = (54, 48, 39)
BOARD_BACKGROUND_COLOR = (242, 242, 242)
BOARD_LINE_COLOR = (150, 150, 150)
BASE_BUTTON_COLOR = (135, 135, 135)
HOVER_BUTTON_COLOR = (190, 190, 190)
CROSS_COLOR = (255, 150, 150)
CIRCLE_COLOR = (150, 150, 255)
DRAW_COLOR = (150, 150, 150)

class TicTacToe:
	def __init__(self, screen):
		self.running: bool = True
		self.screen: pygame.Surface = screen
		self.clock = pygame.time.Clock()
		self.board = Board()
		self.buttons: list[Button] = [ButtonBackToMenu([50,25])]
		self.state: int = 0
		self.turn = 1

	def handle_events(self):
		mouse_position = pygame.mouse.get_pos()
		for button in self.buttons:
			button.change_color(mouse_position)
			button.update(self.screen)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				for button in self.buttons:
					if (button.check_for_input(mouse_position)):
						button.callback(self.screen)
				if (self.state == 0):
					if (self.board.handle_click(mouse_position, self.turn)):
						self.turn += 1
						self.state = self.board.check_position()
						if (self.state == 0 and self.turn == 10):
							self.state = 3

	def display(self):
		self.screen.fill(BACKGROUND_COLOR)
		for button in self.buttons:
			button.update(self.screen)
		self.board.display(self.screen)
		if (self.state == 1):
			victory = pygame.font.SysFont('Arial', 35).render('PLAYER 1 VICTORY !', True, CIRCLE_COLOR)
		if (self.state == 2):
			victory = pygame.font.SysFont('Arial', 35).render('PLAYER 2 VICTORY !', True, CROSS_COLOR)
		if self.state == 3:
			victory = pygame.font.SysFont('Arial', 35).render('IT\'S A DRAW !', True, DRAW_COLOR)
		if (self.state == 1 or self.state == 2 or self.state == 3):
			victory_rect = victory.get_rect()
			victory_rect.center = (SCREEN_WIDTH / 2, 50)
			self.screen.blit(victory, victory_rect)
		pygame.display.flip()

	def run(self):
		while (self.running):
			self.handle_events()
			self.display()

class Board:
	def __init__(self):
		self.board = [[' ', ' ', ' '],
					   [' ', ' ', ' '],
					   [' ', ' ', ' ']]

	def handle_click(self, position: tuple[int, int], turn) -> bool:
		if (100 <= position[0] < 333):
			col = 0
		elif (333 <= position[0] < 566):
			col = 1
		elif (566 <= position[0] <= 800):
			col = 2
		if (100 <= position[1] < 333):
			row = 0
		elif (333 <= position[1] < 566):
			row = 1
		elif (566 <= position[1] <= 800):
			row = 2
		else:
			return False
		if (self.board[row][col] == ' '):
			if (turn % 2):
				self.board[row][col] = 'O'
				return True
			else:
				self.board[row][col] = 'X'
				return True
		else:
			return False

	def check_position(self) -> int:
		if (self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2] and self.board[0][0] != " "):
			if (self.board[0][0] == "O"):
				return (1)
			else:
				return (2)
		elif (self.board[1][0] == self.board[1][1] and self.board[1][1] == self.board[1][2] and self.board[1][0] != " "):
			if (self.board[1][0] == "O"):
				return (1)
			else:
				return (2)
		elif (self.board[2][0] == self.board[2][1] and self.board[2][1] == self.board[2][2] and self.board[2][0] != " "):
			if (self.board[2][0] == "O"):
				return (1)
			else:
				return (2)
		elif (self.board[0][0] == self.board[1][0] and self.board[1][0] == self.board[2][0] and self.board[0][0] != " "):
			if (self.board[0][0] == "O"):
				return (1)
			else:
				return (2)
		elif (self.board[0][1] == self.board[1][1] and self.board[1][1] == self.board[2][1] and self.board[0][1] != " "):
			if (self.board[0][1] == "O"):
				return (1)
			else:
				return (2)
		elif (self.board[0][2] == self.board[1][2] and self.board[1][2] == self.board[2][2] and self.board[0][2] != " "):
			if (self.board[0][2] == "O"):
				return (1)
			else:
				return (2)
		elif (self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[2][2] != " "):
			if (self.board[0][0] == "O"):
				return (1)
			else:
				return (2)
		elif (self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[2][0] != " "):
			if (self.board[0][2] == "O"):
				return (1)
			else:
				return (2)
		else:
			return (0)

	def display(self, screen: pygame.Surface):
		pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, pygame.Rect(100, 100, SCREEN_WIDTH - 200, SCREEN_HEIGHT - 200))
		pygame.draw.rect(screen, BOARD_LINE_COLOR, pygame.Rect(100, 100 + ((SCREEN_HEIGHT - 200) / 3), (SCREEN_WIDTH - 200), 5))
		pygame.draw.rect(screen, BOARD_LINE_COLOR, pygame.Rect(100, 100 + ((SCREEN_HEIGHT - 200) / 3) * 2, (SCREEN_WIDTH - 200), 5))
		pygame.draw.rect(screen, BOARD_LINE_COLOR, pygame.Rect(100 + ((SCREEN_WIDTH - 200) / 3) , 100, 5,(SCREEN_HEIGHT - 200)))
		pygame.draw.rect(screen, BOARD_LINE_COLOR, pygame.Rect(100 + ((SCREEN_WIDTH - 200) / 3) * 2, 100, 5,(SCREEN_HEIGHT - 200)))
		i: int = 0
		for row in self.board:
			j: int = 0
			for col in row:
				if (i == 0 and j == 0):
					if (self.board[i][j] == "X"):
						pygame.draw.line(screen, CROSS_COLOR, (110,105), (323, 328), 10) ##############Line top
						pygame.draw.line(screen, CROSS_COLOR, (110,328), (323, 105), 10)
					elif (self.board[i][j] == "O"):
						pygame.draw.circle(screen, CIRCLE_COLOR, (216, 216), 111, 10)
				elif (i == 0 and j == 1):
					if (self.board[i][j] == "X"):
						pygame.draw.line(screen, CROSS_COLOR, (343,105), (556, 328), 10)
						pygame.draw.line(screen, CROSS_COLOR, (343,328), (556, 105), 10)
					elif (self.board[i][j] == "O"):
						pygame.draw.circle(screen, CIRCLE_COLOR, (450, 216), 111, 10)
				elif (i == 0 and j == 2):
					if (self.board[i][j] == "X"):
						pygame.draw.line(screen, CROSS_COLOR, (576,105), (790, 328), 10)
						pygame.draw.line(screen, CROSS_COLOR, (576,328), (790, 105), 10)
					elif (self.board[i][j] == "O"):
						pygame.draw.circle(screen, CIRCLE_COLOR, (683, 216), 111, 10)

				elif (i == 1 and j == 0):
					if (self.board[i][j] == "X"):
						pygame.draw.line(screen, CROSS_COLOR, (110,343), (323, 561), 10) ##############Line mid
						pygame.draw.line(screen, CROSS_COLOR, (110,561), (323, 343), 10)
					elif (self.board[i][j] == "O"):
						pygame.draw.circle(screen, CIRCLE_COLOR, (216, 450), 111, 10)
				elif (i == 1 and j == 1):
					if (self.board[i][j] == "X"):
						pygame.draw.line(screen, CROSS_COLOR, (348,343), (555, 561), 10)
						pygame.draw.line(screen, CROSS_COLOR, (348,561), (555, 343), 10)
					elif (self.board[i][j] == "O"):
						pygame.draw.circle(screen, CIRCLE_COLOR, (450, 450), 111, 10)
				elif (i == 1 and j == 2):
					if (self.board[i][j] == "X"):
						pygame.draw.line(screen, CROSS_COLOR, (581,343), (785, 561), 10)
						pygame.draw.line(screen, CROSS_COLOR, (581,561), (785, 343), 10)
					elif (self.board[i][j] == "O"):
						pygame.draw.circle(screen, CIRCLE_COLOR, (683, 450), 111, 10)

				elif (i == 2 and j == 0):
					if (self.board[i][j] == "X"):
						pygame.draw.line(screen, CROSS_COLOR, (110,575), (323, 795), 10) ###############Line bot
						pygame.draw.line(screen, CROSS_COLOR, (110,795), (323, 575), 10)
					elif (self.board[i][j] == "O"):
						pygame.draw.circle(screen, CIRCLE_COLOR, (216, 683), 111, 10)
				elif (i == 2 and j == 1):
					if (self.board[i][j] == "X"):
						pygame.draw.line(screen, CROSS_COLOR, (348,575), (555, 795), 10)
						pygame.draw.line(screen, CROSS_COLOR, (348,795), (555, 575), 10)
					elif (self.board[i][j] == "O"):
						pygame.draw.circle(screen, CIRCLE_COLOR, (450, 683), 111, 10)
				elif (i == 2 and j == 2):
					if (self.board[i][j] == "X"):
						pygame.draw.line(screen, CROSS_COLOR, (581,575), (785, 795), 10)
						pygame.draw.line(screen, CROSS_COLOR, (581,795), (785, 575), 10)
					elif (self.board[i][j] == "O"):
						pygame.draw.circle(screen, CIRCLE_COLOR, (683, 683), 111, 10)
				j = j + 1
			i = i + 1

class ButtonBackToMenu(Button):
	def __init__(self, position):
		super().__init__(image = None,
				   position = position,
				   text_input = "MENU",
				   font = pygame.font.SysFont("Arial", 25),
				   base_color = BASE_BUTTON_COLOR,
				   hovering_color = HOVER_BUTTON_COLOR)

	def callback(self, screen):
		print("TIC TAC TOE : MENU pressed")
		scene = menu.Menu(screen)
		scene.run()