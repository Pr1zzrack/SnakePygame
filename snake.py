import pygame
import random


class SnakeGame:
    def __init__(self):
        pygame.init()
        
        self.dis_width = 1000
        self.dis_height = 600
        self.dis = pygame.display.set_mode((self.dis_width, self.dis_height))
        pygame.display.set_caption('Змейка')
        
        self.clock = pygame.time.Clock()
        self.snake_block = 10
        self.snake_speed = 15
        
        self.font_style = pygame.font.SysFont("bahnschrift", 25)
        self.score_font = pygame.font.SysFont("comicsansms", 35)

        self.game_over = False
        self.game_close = False

        self.x1 = self.dis_width / 2
        self.y1 = self.dis_height / 2

        self.x1_change = 0
        self.y1_change = 0

        self.snake_list = []
        self.length_of_snake = 1

        self.foodx = round(random.randrange(0, self.dis_width - self.snake_block) / 10.0) * 10.0
        self.foody = round(random.randrange(0, self.dis_height - self.snake_block) / 10.0) * 10.0

    def our_snake(self):
        for x in self.snake_list:
            pygame.draw.rect(self.dis, (0, 128, 0), [x[0], x[1], self.snake_block, self.snake_block])

    def message(self, msg, color):
        mesg = self.font_style.render(msg, True, color)
        self.dis.blit(mesg, [self.dis_width / 6, self.dis_height / 3])

    def reset_game(self):
        self.game_over = False
        self.game_close = False

        self.x1 = self.dis_width / 2
        self.y1 = self.dis_height / 2

        self.x1_change = 0
        self.y1_change = 0

        self.snake_list = []
        self.length_of_snake = 1

        self.foodx = round(random.randrange(0, self.dis_width - self.snake_block) / 10.0) * 10.0
        self.foody = round(random.randrange(0, self.dis_height - self.snake_block) / 10.0) * 10.0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x1_change = -self.snake_block
                    self.y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    self.x1_change = self.snake_block
                    self.y1_change = 0
                elif event.key == pygame.K_UP:
                    self.y1_change = -self.snake_block
                    self.x1_change = 0
                elif event.key == pygame.K_DOWN:
                    self.y1_change = self.snake_block
                    self.x1_change = 0

    def update_snake(self):
        self.x1 += self.x1_change
        self.y1 += self.y1_change

        if self.x1 >= self.dis_width or self.x1 < 0 or self.y1 >= self.dis_height or self.y1 < 0:
            self.game_close = True

        snake_head = [self.x1, self.y1]
        self.snake_list.append(snake_head)

        if len(self.snake_list) > self.length_of_snake:
            del self.snake_list[0]

        for x in self.snake_list[:-1]:
            if x == snake_head:
                self.game_close = True

    def check_food_collision(self):
        if self.x1 == self.foodx and self.y1 == self.foody:
            self.foodx = round(random.randrange(0, self.dis_width - self.snake_block) / 10.0) * 10.0
            self.foody = round(random.randrange(0, self.dis_height - self.snake_block) / 10.0) * 10.0
            self.length_of_snake += 1

    def game_loop(self):
        while not self.game_over:
            while self.game_close:
                self.dis.fill((128, 128, 128))
                self.message("Вы проиграли! Нажмите Q для выхода или C для повторной игры", (139, 0, 0))
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            self.game_over = True
                            self.game_close = False
                        if event.key == pygame.K_c:
                            self.reset_game()

            self.handle_events()

            self.update_snake()

            self.dis.fill((128, 128, 128))
            pygame.draw.rect(self.dis, (255, 0, 0), [self.foodx, self.foody, self.snake_block, self.snake_block])

            self.our_snake()
            pygame.display.update()

            self.check_food_collision()

            self.clock.tick(self.snake_speed)

        pygame.quit()
        quit()

if __name__ == "__main__":
    game = SnakeGame()
    game.game_loop()