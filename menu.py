import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import tictactoe
from objects import Button

#========= CONSTANTS ==========
MENU_BACKGROUND_COLOR = (54, 48, 39)
TITLE_COLOR = (66, 8, 140)
BASE_BUTTON_COLOR = (135, 135, 135)
HOVER_BUTTON_COLOR = (190, 190, 190)

#========= SCENE ==========
class Menu:
	def __init__(self, screen: pygame.Surface):
		self.screen: pygame.Surface = screen
		self.running: bool = True
		self.buttons: list[Button] = [ButtonTicTacToe((SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2))]

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

	def display(self):
		self.screen.fill(MENU_BACKGROUND_COLOR)
		for button in self.buttons:
			button.update(self.screen)
		title = pygame.font.SysFont("Arial", 100).render("Lil'Games", True, TITLE_COLOR)
		pygame.display.flip()

	def run(self):
		while (self.running):
			self.handle_events()
			self.display()

#========= ELEMENTS ==========
class ButtonTicTacToe(Button):
	def __init__(self, position):
		super().__init__(image = None,
				   position = position,
				   text_input = "TIC TAC TOE",
				   font = pygame.font.SysFont("Arial", 35),
				   base_color = BASE_BUTTON_COLOR,
				   hovering_color = HOVER_BUTTON_COLOR)

	def callback(self, screen):
		print("MAIN MENU : TIC TAC TOE pressed")
		scene = tictactoe.TicTacToe(screen)
		scene.run()