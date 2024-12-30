import pygame 
import sys 
import random


# initializing the constructor 
pygame.init() 

# screen resolution 
res = (720,720) 

# sets value for number of clicks
clicks = 0
str(clicks)

# opens up a window 
screen = pygame.display.set_mode(res) 

# white color 
color = (255,255,255) 

# light shade of the button 
color_light = (170,170,170) 

# dark shade of the button 
color_dark = (100,100,100) 

# stores the width of the 
# screen into a variable 
width = screen.get_width() 

# stores the height of the 
# screen into a variable 
height = screen.get_height() 

# defining the numbers that will be
# replaced for the xy coordinates of the button
X_C = random.randint(1,10)
Y_C = random.randint(1,10)

# defining a font 
smallfont = pygame.font.SysFont('Corbel',35) 

# rendering a text written in 
# this font 
text = smallfont.render('click' , True , color) 

while True: 
	
	for ev in pygame.event.get(): 
		
		if ev.type == pygame.QUIT: 
			pygame.quit() 
			
		#checks if a mouse is clicked 
		if ev.type == pygame.MOUSEBUTTONDOWN: 
			
			#if the mouse is clicked on the 
			# button the game is terminated 
			if width/X_C <= mouse[0] <= width/X_C+140 and height/Y_C <= mouse[1] <= height/Y_C+40: 
				clicks = clicks+1
				str(clicks)
				print(clicks)
				
	# fills the screen with a color 
	screen.fill((60,25,60)) 
	
	# stores the (x,y) coordinates into 
	# the variable as a tuple 
	mouse = pygame.mouse.get_pos() 
	
	# if mouse is hovered on a button it 
	# changes to lighter shade 
	if width/X_C <= mouse[0] <= width/X_C+140 and height/Y_C <= mouse[1] <= height/Y_C+40: 
		pygame.draw.rect(screen,color_light,[width/X_C,height/Y_C,140,40]) 
		
	else: 
		pygame.draw.rect(screen,color_dark,[width/X_C,height/Y_C,140,40]) 
	
	# superimposing the text onto our button 
	screen.blit(text , (width/X_C+50,height/Y_C)) 
	
	# updates the frames of the game 
	pygame.display.update() 
