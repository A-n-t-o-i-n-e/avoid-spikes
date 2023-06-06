import pyxel
from random import randint

class App:
    def __init__(self):
        self.DEFAULT_FPS = 30
        pyxel.init(128, 128, title="Avoid Pikes", fps=self.DEFAULT_FPS)
        pyxel.load("4.pyxres")
        self.reset_game()
        pyxel.run(self.update, self.draw)
        
    def reset_game(self):
        self.x = 5
        self.y = 62
        self.x2 = 5
        self.y2 = 62
        self.arrival = 123
        self.score1 = 0
        self.score2 = 0
        self.n_pic = 0
        self.v = 1
        self.menu = True
        self.mult = False
        self.frame_count = 0  # Compteur de frames
        self.timer = 30  # Timer en secondes
        
        self.coords = self.generate_coordinates(self.n_pic)
        
    def generate_coordinates(self, n):
        coords = []
        while len(coords) < n:
            x = randint(15, 118)
            y = randint(-10, 130)
            if [x, y] not in coords:
                coords.append([x, y])
        return coords
        
    def update(self):
        if pyxel.btn(pyxel.KEY_R):
            self.reset_game()
            
        self.update_player1()
        self.update_player2()
        
        self.check_collision(self.x, self.y, 1)
        self.check_collision(self.x2, self.y2, 2)
        
        self.update_timer()
        
        self.frame_count += 1  # Incrémenter le compteur de frames
        
    def update_player1(self):
        if pyxel.btn(pyxel.KEY_G):
            self.menu = True
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= self.v
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += self.v
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= self.v
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += self.v
            
        if self.x > self.arrival:
            self.reset_player1()
            self.score1 += 1
            self.timer = 30
            if self.mult:
                self.n_pic += 10
            pyxel.play(0, 0)
            self.coords = self.generate_coordinates(self.n_pic)
            
        if self.y > 128 or self.y < 0:
            self.reset_player1()
            
    def update_player2(self):
        if pyxel.btn(pyxel.KEY_G):
            self.menu = True
        if pyxel.btn(pyxel.KEY_Q):
            self.x2 -= self.v
        if pyxel.btn(pyxel.KEY_D):
            self.x2 += self.v
        if pyxel.btn(pyxel.KEY_Z):
            self.y2 -= self.v
        if pyxel.btn(pyxel.KEY_S):
            self.y2 += self.v
            
        if self.x2 > self.arrival:
            self.reset_player2()
            self.score2 += 1
            pyxel.play(0, 0)
            self.timer = 30
            if self.mult:
                self.n_pic += 10
            self.coords = self.generate_coordinates(self.n_pic)
            
        if self.y2 > 128 or self.y2 < 0:
            self.reset_player2()
            
    def reset_player1(self):
        self.x = 5
        self.y = 62
        
    def reset_player2(self):
        self.x2 = 5
        self.y2 = 62

    def get_colors(self, a, b):
        colors = []
        for i in range(a, a+5):
            for j in range(b, b+5):
                color = pyxel.pget(i, j)
                colors.append(color)
        return colors

    def check_collision(self, x, y, player):
        for coord in self.coords:
            if 0 in self.get_colors(self.x,self.y):
                self.reset_player1()
            if 0 in self.get_colors(self.x2,self.y2):
                self.reset_player2()
                
    def update_timer(self):
        self.timer -= 1 / self.DEFAULT_FPS 
        if self.timer <= 0: 
            self.timer = 30
            
            if self.mult:
                self.n_pic += 10
            
            self.coords = self.generate_coordinates(self.n_pic)
        
    def draw(self):
        pyxel.cls(10)
        pyxel.blt(self.x, self.y, 0, 8, 0, 5, 5, 5)
        pyxel.blt(self.x2, self.y2, 0, 8, 8, 5, 5, 5)
        for coord in self.coords:
            pyxel.blt(coord[0], coord[1], 0, 0, 0, 3, 3, 5)
        if self.menu:
            pyxel.rect(10, 10, 108, 108, 11)
            pyxel.text(43, 15, "DIFFICULTÉ", 0)
            pyxel.text(43, 30, "1 = FACILE", 0)
            pyxel.text(43, 45, "2 = NORMAL", 0)
            pyxel.text(43, 60, "3 = DIFFICILE", 0)
            pyxel.text(43, 75, "4 = PROGRESSIF", 0)
            pyxel.text(43, 90, "R = RÉINITIALISER", 0)
            pyxel.text(43, 105, "G = MENU", 0)
            if pyxel.btn(pyxel.KEY_1):
                self.menu = False
                self.mult = False
                self.n_pic = 60
            elif pyxel.btn(pyxel.KEY_2):
                self.menu = False
                self.mult = False
                self.n_pic = 100
            elif pyxel.btn(pyxel.KEY_3):
                self.menu = False
                self.n_pic = 160
                self.mult = False
            if pyxel.btn(pyxel.KEY_4):
                self.mult = True
                self.n_pic = 0
                self.menu = False
            self.coords = self.generate_coordinates(self.n_pic)
        else:
            pass
        pyxel.text(3, 2, str(self.score1), 12)
        pyxel.text(3, 9, str(self.score2), 8)
        pyxel.text(3, 16, str(self.n_pic), 7)
        pyxel.text(110, 2, str(round(self.timer, 1)), 7)
            

App()
