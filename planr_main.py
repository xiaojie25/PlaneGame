import pygame
from plane_sprites import *

# 游戏的帧数
FRAME_PER_SEC = 120
# 创建敌机事件
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class PlaneGame(object):

    def __init__(self):
        print("游戏初始化。。。")

        # 1.创建屏幕对象
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 写窗口title
        pygame.display.set_caption("飞机大战")
        # 2.创建时钟对象
        self.clock = pygame.time.Clock()
        # 3.调用私有方法，精灵和精灵组的创建
        self.__create_sprites()
        # 4.设置敌机定时器事件—1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):

        background1 = BackGroundSprites()
        background2 = BackGroundSprites(0, -SCREEN_RECT.height)
        # background2.rect.y = -SCREEN_RECT.h
        self.background_group = pygame.sprite.Group(background1, background2)

        # 创建敌机精灵、精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄精灵、精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始了。。。")
        while True:
            # 1、设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2、事件监听
            self.__event_handler()
            # 3、碰撞检测
            self.__check_collide()
            # 5、刷新精灵
            self.__update_sprites()
            # 6、屏幕更新
            pygame.display.update()

    def __event_handler(self):
        """事件监听"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌机出现喽、、、")
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
        # 返回所有的按键元组,若某个键被按下，对应值为1
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT] == 1 or key_pressed[pygame.K_d] == 1:
            # print("向右移动。。。")
            self.hero.speed = 2
        elif key_pressed[pygame.K_LEFT] == 1 or key_pressed[pygame.K_a] == 1:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):
        """碰撞检测"""
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        """更新精灵"""
        self.background_group.update()
        self.background_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        """游戏结束，卸载所有模块，退出游戏"""
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()


