from engine import Board, Player1, Player2
import pygame
import sys

s = [900, 800]

pygame.init()
screen = pygame.display.set_mode(s, 0, 32)
pygame.display.set_caption("Connect 4 by NIP")

big = pygame.font.SysFont("Garamond MS", 60)
med = pygame.font.SysFont("Garamond MS", 25)

def startscreen():
    head = big.render("Connect 4", True, (0, 0, 0))
    foot = med.render("Click to play", True, (0, 0, 0))
    
    while True:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                return

        pygame.draw.line(screen, (0, 255, 0), (570, 0), (570, 800), 10)
        pygame.draw.line(screen, (255, 0, 0), (0, 600), (900, 600), 40)
        pygame.draw.line(screen, (0, 255, 0), (700, 0), (700, 800), 200)
        pygame.draw.line(screen, (0, 255, 0), (270, 0), (370, 800), 70)
        pygame.draw.line(screen, (255, 0, 0), (0, 270), (900, 170), 40)

        for y in range(3):
            pygame.draw.line(screen, (255, 0, 0), (0, y*20 + 100), (900, y*20 + 100), 4)

        screen.blit(head, head.get_rect(center=[s[0]/2, s[1]/2 - 50]))
        screen.blit(foot, foot.get_rect(center=[s[0]/2, s[1]/2 + 20]))

        pygame.display.flip()

def endscreen(message, Board):
    pygame.display.set_caption("Game Over! Result: %s" % message)
    head = big.render(message, True, (255, 0, 0) if message[0].lower() == "r" else ((0, 255, 0) if message[0].lower() == "g" else (0, 0, 0)))
    foot = med.render("Click to play again!", True, (0, 0, 0))

    b = pygame.Surface(s)
    Board.draw(b)
    b.set_alpha(40)

    while True:
        screen.fill((0, 0, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                return

        pygame.draw.rect(screen, (255, 255, 255), ((50, 50), [i-100 for i in s]), 0)
        screen.blit(head, head.get_rect(center=[s[0]/2, s[1]/2 - 50]))
        screen.blit(foot, foot.get_rect(center=[s[0]/2, s[1]/2 + 20]))
        screen.blit(b, (0, 0))

        pygame.display.flip()

def main():
    startscreen()
    P1 = Player1()
    P2 = Player2()

    while True:
        board = Board(P1, P2, s)
        pygame.display.set_caption("Connect 4 by NIP |||| Red: %s |||| Green: %s" % (P1.wins, P2.wins))

        while True:
            board.events()
            board.draw(screen)
            
            pygame.draw.circle(screen, (255, 0, 0) if board.turn else (0, 255, 0), pygame.mouse.get_pos(), 10, 0)
            pygame.draw.circle(screen, (255, 0, 0) if board.turn else (0, 255, 0), pygame.mouse.get_pos(), 30, 2)

            if board.check():
                break

            pygame.display.flip()

        if board.check() == 1:
            if not board.turn:
                P1.wins += 1
            else:
                P2.wins += 1

        endscreen(("Red Wins!" if not board.turn else "Green Wins!") if board.check() == 1 else "Draw", board)
            
if __name__ == "__main__":
    main()
