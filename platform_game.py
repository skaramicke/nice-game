import random

class Platform:
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length

class Player:
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol

def draw_game_area(game_area, platforms, player):
    for y in range(len(game_area)):
        for x in range(len(game_area[y])):
            if any(platform.x <= x < platform.x + platform.length and platform.y == y for platform in platforms):
                print('#', end='')
            elif player.x == x and player.y == y:
                print(player.symbol, end='')
            else:
                print('.', end='')
        print()

def game_loop(game_area, platforms, player):
    draw_game_area(game_area, platforms, player)
    while True:
        move = input('Enter move (a, d, w, or s): ')
        valid_moves = ['a', 'd', 'w', 's']
        if move in valid_moves:
            if move == 'a':
                if player.x > 0 and not any(platform.x <= player.x - 1 < platform.x + platform.length and platform.y == player.y for platform in platforms):
                    player.x -= 1
            elif move == 'd':
                if player.x < len(game_area[0]) - 1 and not any(platform.x <= player.x + 1 < platform.x + platform.length and platform.y == player.y for platform in platforms):
                    player.x += 1
            elif move == 'w':
                if player.y > 0 and not any(platform.x <= player.x < platform.x + platform.length and platform.y == player.y - 1 for platform in platforms):
                    player.y -= 1
            elif move == 's':
                if player.y < len(game_area) - 1 and not any(platform.x <= player.x < platform.x + platform.length and platform.y == player.y + 1 for platform in platforms):
                    player.y += 1

        for line in game_area:
            print(line)
        print()

game_area = [['.' for _ in range(40)] for _ in range(20)]
platforms = [Platform(5, 10, 20), Platform(25, 5, 10)]
player = Player(3, 5, 'A')
game_loop(game_area, platforms, player)