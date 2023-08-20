import random as r
from collections import deque

class Game:
    def __init__(self):
        self.arr = deque()
        for _ in range(10):
            self.arr.append(["   " for _ in range(10)])
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.catcher = "|_|"
        self.catchZone = ["   " for _ in range(10)]
        self.score = 0
        self.pos = 0
        self.catchZone[self.pos] = self.catcher
        self.holdingNumber = -1
        self.findings = deque()

    def movement(self, inp):
        if (inp == "a" and self.catchZone[0] == self.catcher) or (inp == "d" and self.catchZone[-1] == self.catcher):
            pass 
        elif inp == "a": 
            self.catchZone[self.pos] = "   " 
            self.pos = max(0, self.pos - 1)
            self.catchZone[self.pos] = self.catcher 
        elif inp == "d": 
            self.catchZone[self.pos] = "   " 
            self.pos = min(9, self.pos + 1) 
            self.catchZone[self.pos] = self.catcher 
        elif inp == "p": 
            print("game quitting")
            return "ov","er"
        else:
            pass 
        return self.catchZone, self.pos 

    def display(self, letter):
        l = letter[1:-1] 
        if self.arr[-1][self.pos] != "   ": 
            self.catchZone[self.pos] = f"|{l}|" 
        for a in range(len(self.arr) - 1): 
            if a == 0: 
                print(self.arr[a], self.score, self.findings) 
            else: 
                print(self.arr[a]) 
        print(self.catchZone) 
        self.catchZone[self.pos] = "|_|" 

    def update(self, c, score):
        self.numbers = self.numbers[5:] 
        score += 1 
        self.numbers.append(c) 
        for i in range(4): 
            self.numbers.append(r.randint(1, c) + r.randint(1, c)) 
        return self.numbers, score 

    def run(self):
        for _ in range(1, 1000): 
            self.display(self.arr[-1][self.pos]) 
            self.arr.pop() 
            self.arr.appendleft(["   " for _ in range(10)]) 
            x = r.randint(0, 9) 
            self.arr[0][x] = f" {r.choice(self.numbers)} " 
            inp = input() 
            self.catchZone, self.pos = self.movement(inp) 

            if self.catchZone == "ov" and self.pos == "er": 
                break 

            if len(self.findings) < 2 and self.arr[-1][self.pos] != "   ": 
                self.findings.append(int(self.arr[-1][self.pos][1:-1])) 
                continue 

            if len(self.findings) == 2: 
                self.holdingNumber = self.findings[-1] + self.findings[-2] 
                self.findings.append(self.holdingNumber) 
                if self.holdingNumber > 10: 
                    self.numbers, self.score = self.update(self.findings[0] + self.findings[1], self.score) 
                continue 

            if len(self.findings) > 2 and self.arr[-1][self.pos] != "   " and int(self.arr[-1][self.pos][1:-1]) != self.findings[-1]: 
                print("You chose the wrong number fool GAME OVER") 
                break 

            print(self.arr[-1][self.pos]) 
            if self.arr[-1][self.pos] != "   " and int(self.arr[-1][self.pos][1:-1]) == self.findings[-1]: 
                a = self.findings[-1] 
                b = self.findings[-2] 
                c = a + b 
                self.findings.append(c) 
                self.numbers, self.score = self.update(c, self.score) 

        print(f"Your score is {self.score}") 
        print(f"Your numbers are {self.findings}")

if __name__ == "__main__":
    game = Game()
    game.run()
