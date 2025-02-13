import pygame
import sys

#GENERIC BUTTON
class Button:
	def __init__(self, image, position, text_input, font, base_color, hovering_color):
		self.image: pygame.Surface = image
		self.x: int = position[0]
		self.y: int = position[1]
		self.font = font
		self.base_color = base_color
		self.hovering_color = hovering_color
		self.text_input = text_input
		self.text: pygame.Surface = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect: pygame.Rect = self.image.get_rect(center=(self.x, self.y))
		self.text_rect: pygame.Rect = self.text.get_rect(center=(self.x, self.y))

	def update(self, screen):
		if (self.image is not None):
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def check_for_input(self, position):
		if ((position[0] in range(self.rect.left, self.rect.right)) and (position[1] in range(self.rect.top, self.rect.bottom))):
			return (True)
		return (False)
	
	def change_color(self, position):
		if ((position[0] in range(self.rect.left, self.rect.right)) and (position[1] in range(self.rect.top, self.rect.bottom))):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

	def callback(self, screen):
		...