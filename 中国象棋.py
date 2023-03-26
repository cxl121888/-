# -import pygame
from Chessman import *

pygame.init()
....
screen = pygame.display.set_mode((WIDTH, HEIGHT))
....
board = Chessboard()
selected = None
running = True
while running:
for event in pygame.event.get():
...
if event.type == MOUSEBUTTONDOWN:
x, y = event.pos
piece = board.get_piece(x, y)
if piece and piece.color == turn:
selected = piece
...
board.draw(screen)
if selected:
selected.highlight(screen)
pygame.display.update()
pygame.quit()

Chessboard.py
class Chessboard:
def init(self):
# 初始化棋盘及棋子
...
def get_piece(self, x, y):
# 根据位置返回棋子,若无棋子返回 None
...
def draw(self, screen):
# 绘制棋盘和棋子
...

Chessman.py
class Chessman:
def init(self, color):
self.color = color # 棋子颜色,红方或黑方
def highlight(self, screen):
# 高亮选中的棋子
...
def can_move(self, board, x, y):
# 检查棋子是否可以移动到指定位置,返回 True/False
...

General.py 等继承 Chessman
class General(Chessman):
def can_move(self, board, x, y):
# overrides父类的方法,实现将的走法判断
...
