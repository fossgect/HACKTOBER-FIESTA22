# Pygame implementation of 2048 Game
# Created by Shone Stalin

# The aim is to reach the number 2048

# How to play the game:
#   ->  Use the arrow keys to merge the numbers 
#   ->  Can merge in al directions, i.e. up,down,left,right


import pygame
import random
import numpy as np

def Game2048():
  BG_COLORS = {
    0: (250, 250, 250),
    2: (238, 228, 218),
    4: (238, 225, 201),
    8: (243, 178, 122),
    16: (246, 150, 100),
    32: (247, 124, 95),
    64: (247, 95, 59),
    128: (237, 208, 115),
    256: (237, 204, 98),
    512: (237, 201, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
  }

  class Game2048:
      def __init__(self) -> None:
          self.N = 4
          self.cellSize = 100
          self.gap = 5
          self.windowBgColor = (187, 173, 160)
          self.blockSize = self.cellSize + self.gap * 2

          self.windowWidth = self.blockSize * 4
          self.windowHeight = self.windowWidth

          pygame.init()

          self.window = pygame.display.set_mode((self.windowWidth, self.windowHeight))
          self.myFont = pygame.font.SysFont("Comic Sans MS", 30)
          pygame.display.set_caption("2048")

          self.boardStatus = np.zeros((self.N, self.N))
          self.addNewNumber() # add new number to board

      
      def addNewNumber(self):
          freePos = zip(*np.where(self.boardStatus == 0))
          freePos = list(freePos)

          for pos in random.sample(freePos, k=1):
              self.boardStatus[pos] = 2

      def drawBoard(self):
          self.window.fill(self.windowBgColor)

          for r in range(self.N):
              rectY = self.blockSize * r + self.gap
              for c in range(self.N):
                  rectX = self.blockSize * c + self.gap
                  cellValue = int(self.boardStatus[r][c])

                  pygame.draw.rect(
                      self.window,
                      BG_COLORS[cellValue],
                      pygame.Rect(rectX, rectY, self.cellSize, self.cellSize)
                  )

                  if cellValue != 0:
                      textSurface = self.myFont.render(f"{cellValue}", True, (0, 0, 0))
                      textRect = textSurface.get_rect(center=(rectX + self.blockSize/2, rectY + self.blockSize/2))
                      self.window.blit(textSurface, textRect)

      def compressNumber(self, data):
          result = [0]
          data = [x for x in data if x != 0]
          for element in data:
              if element == result[len(result) - 1]:
                  result[len(result) - 1] *= 2
                  result.append(0)
              else:
                  result.append(element)
          
          result = [x for x in result if x != 0]
          return result

      def move(self, dir):
          for idx in range(self.N):

              if dir in "UD":
                  data = self.boardStatus[:, idx]
              else:
                  data = self.boardStatus[idx, :]

              flip = False
              if dir in "RD":
                  flip = True
                  data = data[::-1]

              data = self.compressNumber(data)
              data = data + (self.N - len(data)) * [0]

              if flip:
                  data = data[::-1]

              if dir in "UD":
                  self.boardStatus[:, idx] = data
              else:
                  self.boardStatus[idx, :] = data

      def isGameOver(self):
          boardStatusBackup = self.boardStatus.copy()
          for dir in "UDLR":
              self.move(dir)

              if (self.boardStatus == boardStatusBackup).all() == False:
                  self.boardStatus = boardStatusBackup
                  return False
          return True

      def play(self):
          running = True
          while running:
              self.drawBoard()
              pygame.display.update()

              for event in pygame.event.get():
                  oldBoardStatus = self.boardStatus.copy()

                  if event.type == pygame.QUIT:
                      running = False
                  elif event.type == pygame.KEYDOWN:
                      if event.key == pygame.K_UP:
                          self.move("U")
                      elif event.key == pygame.K_DOWN:
                          self.move("D")
                      elif event.key == pygame.K_LEFT:
                          self.move("L")
                      elif event.key == pygame.K_RIGHT:
                          self.move("R")
                      elif event.key == pygame.K_ESCAPE:
                          running = False

                      if self.isGameOver():
                          print("Game Over !!")
                          return

                      if (self.boardStatus == oldBoardStatus).all() == False:
                          self.addNewNumber()


  game = Game2048()
  game.play()

if __name__ == "__main__":
  Game2048()
