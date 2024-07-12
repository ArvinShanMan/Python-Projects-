import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 400, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (100, 150, 255)
FONT_SIZE = 40

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Calculator")

font = pygame.font.Font(None, FONT_SIZE)
small_font = pygame.font.Font(None, FONT_SIZE - 10)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def is_mouse_over_button(pos, button_rect):
    x, y = pos
    bx, by, bw, bh = button_rect
    return bx <= x <= bx + bw and by <= y <= by + bh

def run_calculator():
    running = True
    expression = ''
    result = ''
    
    while running:
        screen.fill(WHITE)
        
        calculator_rect = pygame.Rect(50, 100, 300, 400)
        pygame.draw.rect(screen, GRAY, calculator_rect)
        
        button_positions = [
            (50, 100, '7'), (170, 100, '8'), (290, 100, '9'),
            (50, 200, '4'), (170, 200, '5'), (290, 200, '6'),
            (50, 300, '1'), (170, 300, '2'), (290, 300, '3'),
            (50, 400, '0'), (170, 400, '.'), (290, 400, 'C'),
            (50, 500, '+'), (170, 500, '-'), (290, 500, '*'),
            (50, 600, '/'), (170, 600, '=')
        ]
        
        for (bx, by, button_text) in button_positions:
            button_rect = pygame.Rect(bx, by, 100, 80)
            pygame.draw.rect(screen, BLUE if button_text in ('=', '+', '-', '*', '/') else GRAY, button_rect)
            draw_text(button_text, font, BLACK, screen, bx + 50, by + 40)
        
        draw_text(expression, font, BLACK, screen, WIDTH // 2, 50)
        draw_text(result, font, BLACK, screen, WIDTH // 2, 80)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                for (bx, by, button_text) in button_positions:
                    button_rect = pygame.Rect(bx, by, 100, 80)
                    if is_mouse_over_button(mouse_pos, button_rect):
                        if button_text == '=':
                            try:
                                result = str(eval(expression))
                            except:
                                result = 'Error'
                        elif button_text == 'C':
                            expression = ''
                            result = ''
                        else:
                            expression += button_text
        
if __name__ == '__main__':
    run_calculator()

