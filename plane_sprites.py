import random
import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
me = ["./images/me1.png", "./images/me2.png"]


class GameSprites(pygame.sprite.Sprite):

    def __init__(self, start_x=0, start_y=0, image_name="./images/background.png", speed=1):

        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        self.speed = speed

    def update(self):

        self.rect.y += self.speed


class BackGroundSprites(GameSprites):
    """创建背景类"""

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height


class Enemy(GameSprites):
    """敌机精灵"""

    def __init__(self):

        # 1、调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__(image_name="./images/enemy1.png")

        # 2、指定敌机初始速度
        self.speed = random.randint(1, 3)

        # 3、指定敌机初始位置

        # y的初始值
        self.rect.bottom = 0
        # x的初始值
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):

        # 1、调用父类方法，保持垂直方向的飞行
        super().update()
        # 2、判断飞机是否飞出屏幕，如果飞出屏幕，需要从精灵组中删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # print("敌机飞出屏幕需要从精灵组中删除...")
            # kill方法可以将精灵从所有精灵组中移除，精灵就会被自动销毁
            self.kill()

    def __del__(self):

        # print("敌机被销毁了，位置：%s" % self.rect)
        pass


class Hero(GameSprites):
    """英雄类"""
    def __init__(self):

        # 1、调用父类方法，设置speed & image
        super().__init__(image_name=me[0], speed=0)
        # 2、设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 创建子弹类
        self.bullets = pygame.sprite.Group()

        self.photo_num = 0

    def update(self):

        # 英雄水平移动
        self.rect.x += self.speed
        # 图片的更新
        self.image = pygame.image.load(me[self.photo_num])
        self.photo_num += 1
        if self.photo_num == 2:
            self.photo_num = 0
        # 判断英雄是否越界
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > SCREEN_RECT.width - self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width

    def fire(self):
        """英雄发射子弹"""
        print("开火！！！")
        for i in range(3):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
        # bullet.start_y = SCREEN_RECT.bottom

            self.bullets.add(bullet)


class Bullet(GameSprites):
    """子弹精灵类"""
    def __init__(self):
        # 调用父类方法，设置子弹图片，设置初始速度
        super().__init__(image_name="./images/bullet1.png", speed=-2)

    def update(self):
        # 调用父类方法，让子弹垂直飞行
        super().update()
        # 如果子弹飞出了屏幕，消除子弹来释放内存
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        # print("子弹被消灭了。。。")
        pass
