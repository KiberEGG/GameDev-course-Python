import pygame
import math
import random

def draw(screen: pygame.Surface):
    font = pygame.font.Font('C://WINDOWS//Fonts//segoeuil.ttf', 36)
    text = font.render('Lesson 3. Snowman', True, (12, 34, 56))
    text_x = w // 2 - text.get_width() // 2
    text_y = h // 8 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))
    BLUE = ( 10, 50, 100)
    pygame.draw.circle(screen, BLUE, (800, 200) , 50 , 5)
    pygame.draw.circle(screen, BLUE, (800, 330) , 80 , 5)
    pygame.draw.line(screen, BLUE, (760, 260) , (700 , 310), 5)
    pygame.draw.line(screen, BLUE, (840, 260) , (900, 310), 5)
    pygame.draw.circle(screen, BLUE, (825, 180) , 3 ,0)   
    pygame.draw.circle(screen, BLUE, (775, 180) , 3 ,0)   
    pygame.draw.arc(screen, BLUE,(775, 180, 50, 50), math.pi, 2*math.pi, 3)
    pygame.draw.circle(screen, pygame.Color("orange"), (800, 300) , 3 ,0)
    pygame.draw.circle(screen, pygame.Color("orange"), (800, 350) , 3 ,0)
    pygame.draw.circle(screen, pygame.Color("orange"), (800, 400) , 3 ,0)
    pygame.draw.polygon(screen,pygame.Color("orange"),[(800, 180) , (795, 185) , (805, 185)])
    
    
    
    
    
    
    
if __name__ == '__main__':
    pygame.init()
    size = w, h = 1600, 600
    screen = pygame.display.set_mode(size)
    color = pygame.Color(25, 60, 10)
    hsv = color.hsva
    color.hsva = (hsv[0], hsv[1], hsv[2] + 20, hsv[3])
    screen.fill(color)

    draw(screen)

    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()