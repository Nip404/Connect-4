import pygame
import sys

class Player1:
    def __init__(self):
        self.wins = 0
        self.colour = (255, 0, 0)
        self.inner_colour = (230, 0, 0)

class Player2:
    def __init__(self):
        self.wins = 0
        self.colour = (0, 255, 0)
        self.inner_colour = (0, 230, 0)

class Board:
    def __init__(self, p1, p2, s):
        self.board = [[None for i in range(7)] for i in range(6)]

        self.player1 = p1
        self.player2 = p2
        
        self.frame = [i-100 for i in s]
        self.coords = [[(150 + (p1*100), 150 + (p0*100)) for p1, item in enumerate(row)] for p0, row in enumerate(self.board)]
        self.rects = [[pygame.Rect(item[0] - 40, item[1] - 40, 80, 80) for item in row] for row in self.coords]

        self.turn = True

    def draw(self,surface):
        surface.fill((139, 93, 46))
        pygame.draw.rect(surface, (30, 144, 255), ((50, 50), self.frame), 0)

        for p0,i in enumerate(self.coords):
            for p1,j in enumerate(i):
                pygame.draw.circle(surface, (255, 255, 255) if self.board[p0][p1] is None else self.board[p0][p1].colour, j, 40, 0)
                pygame.draw.circle(surface, (255, 255, 255) if self.board[p0][p1] is None else self.board[p0][p1].inner_colour, j, 32, 0)

    def move(self, mouse):
        column = None
        
        for y, i in enumerate(self.rects):
            for x, j in enumerate(i):
                if pygame.Rect(mouse[0]-1, mouse[1]-1, 2, 2).colliderect(j):
                    if self.board[0][x] is not None:
                        return

                    y = len(self.board) - 1
                    while self.board[y][x] is not None and y:
                        y -= 1

                    self.board[y][x] = self.player1 if self.turn else self.player2
                    self.turn = not self.turn

    def check(self):
        for t in [self.board, [[self.board[y][x] for y in range(len(self.board))] for x in range(len(self.board[0]))]]:
            for row in t:
                for i in range(len(row) - 3):
                    if all(row[i] == e and row[i] is not None for e in row[i: i+4]):
                        return 1

        for y in range(len(self.board) - 3):
            for x in range(len(self.board[0]) - 3):
                if (self.board[y][x] is not None and self.board[y][x] == self.board[y+1][x+1] == self.board[y+2][x+2] == self.board[y+3][x+3]) or (self.board[len(self.board)-y-1][x] is not None and self.board[len(self.board)-y-1][x] == self.board[len(self.board)-y-2][x+1] == self.board[len(self.board)-y-3][x+2] == self.board[len(self.board)-y-4][x+3]):
                    return 1

        if all(all(self.board[y][x] is not None for x in range(len(self.board[0]))) for y in range(len(self.board))):
            return 2
                
    def events(self, **custom_events):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.move(pygame.mouse.get_pos())

            else:
                for user_evt in custom_events.keys():
                    if event.type == user_evt:
                        try:
                            custom_events[user_evt]()
                        except:
                            pass
