import numpy as np
import pygame as pg
#import time

BLACK=(0,0,0)
WHITE=(255,255,255)
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (1, -1), (1, 1), (1, 0), (0, 1)]
pixel_size=8

class GoL():

    def __init__(self, window_width=None, window_height=None, seed=None):
        self.window_width = window_width
        self.window_height = window_height
        if seed==None:  
            if self.window_width==None:
                if self.window_height!=None or self.window_height!=0:
                    self.rows = self.window_height//pixel_size
                else:
                    self.rows = 100
            else:
                self.rows = self.window_width//pixel_size
            if self.window_height==None:
                if self.window_width!=None and self.window_width!=0:
                    self.columns = self.window_width//pixel_size
                else:
                    self.columns = 100
            else:
                self.columns = self.window_height//pixel_size

            seed_pg = np.random.randint(1001, size=(self.rows, self.columns))

            for row in range(self.rows):
                for column in range(self.columns):
                    if seed_pg[row][column]>=900 and row>=25 and row<75 and column>=25 and column<75:
                        seed_pg[row][column] = 1
                    else:
                        seed_pg[row][column] = 0

        self.seed = seed_pg

    def time_tick(self):
        seed_new = np.zeros([self.rows, self.columns], dtype=np.uint8)  
        for row in range(self.rows):
                for column in range(self.columns):
                    neighbours = 0
					for directions in DIRECTIONS:
						new_node = np.array([row, column]) + np.array(directions)
						if 0<=new_node[0]<rows and 0<=new_node[1]<columns:
							if seed[new_node[0]][new_node[1]] == 1:
								neighbours += 1
                    if ((neighbours==3 or neighbours==2) and self.seed[row][column] == 1) or (neighbours==3 and self.seed[row][column] == 0):
                        seed_new[row][column] = 1
        return seed_new



    def run_gol(self):

        pg.init()
		
		# window setup
        self.screen = pg.display.set_mode((self.window_width, self.window_height))
        pg.display.set_caption("Conway's Game of Life by S.S.Silva")
        # icon = pg.image.load('img\pendulum.png')
        # pg.display.set_icon(icon)
        clock = pg.time.Clock()

        

        #fieldC = sum(len(x) for x in self.seed)

        

        self.screen.fill((0,0,0))
        for row in range(self.rows):
            for column in range(self.columns):
                color = BLACK
                if self.seed[row][column] == 1:
                    color = WHITE
                pg.draw.rect(self.screen,
                                color,
                                [pixel_size * column,
                                pixel_size * row,
                                pixel_size,
                                pixel_size])
        #img = pg.surfarray.make_surface(self.seed)
        #self.win.blit(img, (0,0))
        #pg.display.update()
        clock.tick(60)
        pg.display.flip()

        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            
            self.seed= self.time_tick()
            self.screen.fill((0,0,0))
            #time.sleep(0.5)
            

            for row in range(self.rows):
                for column in range(self.columns):
                    color = BLACK
                    if self.seed[row][column] == 1:
                        color = WHITE
                    pg.draw.rect(self.screen,
                                    color,
                                    [pixel_size * column,
                                    pixel_size * row,
                                    pixel_size,
                                    pixel_size])
            clock.tick(60)
            pg.display.flip()
    pg.quit()



if __name__ == "__main__":
    w_width = 800
    w_height = 800
    seed1 = None

    game = GoL(w_width, w_height, seed1)

    game.run_gol()
    
