import pygame

class Settings(object):
    """设置常用的属性"""

    def __init__(self):
        self.bgImage = pygame.image.load('img/background.png')  # 背景图

        self.bgImageWidth = self.bgImage.get_rect()[2]  # 背景图宽
        self.bgImageHeight = self.bgImage.get_rect()[3]  # 背景图高
        self.start = pygame.image.load("img/start.png")
        self.pause = pygame.image.load("img/pause.png")
        self.gameover = pygame.image.load("img/gameover.png")
        self.heroImages = ["img/hero.gif",
                           "img/hero1.png", "img/hero2.png"]  # 英雄机图片
        self.airImage = pygame.image.load("img/enemy0.png")  # airplane的图片
        self.beeImage = pygame.image.load("img/bee.png")  # bee的图片
        self.heroBullet = pygame.image.load("img/bullet.png")  # 英雄机的子弹


飞行物类
import abc


class FlyingObject(object):
    """飞行物类，基类"""

    def __init__(self, screen, x, y, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = image.get_rect()[2]
        self.height = image.get_rect()[3]
        self.image = image

    @abc.abstractmethod
    def outOfBounds(self):
        """检查是否越界"""
        pass

    @abc.abstractmethod
    def step(self):
        """飞行物移动一步"""
        pass

    def shootBy(self, bullet):
        """检查当前飞行物是否被子弹bullet（x，y）击中"""
        x1 = self.x
        x2 = self.x + self.width
        y1 = self.y
        y2 = self.y + self.height
        x = bullet.x
        y = bullet.y
        return x > x1 and x < x2 and y > y1 and y < y2

    def blitme(self):
        """打印飞行物"""
        self.screen.blit(self.image, (self.x, self.y))


英雄机
from flyingObject import FlyingObject
from bullet import Bullet
import pygame


class Hero(FlyingObject):
    """英雄机"""
    index = 2  # 标志位

    def __init__(self, screen, images):

        # self.screen = screen

        self.images = images  # 英雄级图片数组,为Surface实例
        image = pygame.image.load(images[0])
        x = screen.get_rect().centerx
        y = screen.get_rect().bottom
        super(Hero, self).__init__(screen, x, y, image)
        self.life = 3  # 生命值为3
        self.doubleFire = 0  # 初始火力值为0

    def isDoubleFire(self):
        """获取双倍火力"""
        return self.doubleFire

    def setDoubleFire(self):
        """设置双倍火力"""
        self.doubleFire = 40

    def addDoubleFire(self):
        """增加火力值"""
        self.doubleFire += 100

    def clearDoubleFire(self):
        """清空火力值"""
        self.doubleFire = 0

    def addLife(self):
        """增命"""
        self.life += 1

    def sublife(self):
        """减命"""
        self.life -= 1

    def getLife(self):
        """获取生命值"""
        return self.life

    def reLife(self):
        self.life = 3
        self.clearDoubleFire()

    def outOfBounds(self):
        return False

    def step(self):
        """动态显示飞机"""
        if (len(self.images) > 0):
            Hero.index += 1
            Hero.index %= len(self.images)
            self.image = pygame.image.load(self.images[int(Hero.index)])  # 切换图片

    def move(self, x, y):
        self.x = x - self.width / 2
        self.y = y - self.height / 2

    def shoot(self, image):
        """英雄机射击"""
        xStep = int(self.width / 4 - 5)
        yStep = 20
        if self.doubleFire >= 100:
            heroBullet = [Bullet(self.screen, image, self.x + 1 * xStep, self.y - yStep),
                          Bullet(self.screen, image, self.x + 2 * xStep, self.y - yStep),
                          Bullet(self.screen, image, self.x + 3 * xStep, self.y - yStep)]
            self.doubleFire -= 3
            return heroBullet
        elif self.doubleFire < 100 and self.doubleFire > 0:
            heroBullet = [Bullet(self.screen, image, self.x + 1 * xStep, self.y - yStep),
                          Bullet(self.screen, image, self.x + 3 * xStep, self.y - yStep)]
            self.doubleFire -= 2
            return heroBullet
        else:
            heroBullet = [Bullet(self.screen, image, self.x + 2 * xStep, self.y - yStep)]
            return heroBullet

    def hit(self, other):
        """英雄机和其他飞机"""
        x1 = other.x - self.width / 2
        x2 = other.x + self.width / 2 + other.width
        y1 = other.y - self.height / 2
        y2 = other.y + self.height / 2 + other.height
        x = self.x + self.width / 2
        y = self.y + self.height
        return x > x1 and x < x2 and y > y1 and y < y2


enemys
import abc


class Enemy(object):
    """敌人，敌人有分数"""

    @abc.abstractmethod
    def getScore(self):
        """获得分数"""
        pass


award
import abc


class Award(object):
    """奖励"""
    DOUBLE_FIRE = 0
    LIFE = 1

    @abc.abstractmethod
    def getType(self):
        """获得奖励类型"""
        pass


if __name__ == '__main__':
    print(Award.DOUBLE_FIRE)
airplane
import random
from flyingObject import FlyingObject
from enemy import Enemy


class Airplane(FlyingObject, Enemy):
    """普通敌机"""

    def __init__(self, screen, image):
        x = random.randint(0, screen.get_rect()[2] - 50)
        y = -40
        super(Airplane, self).__init__(screen, x, y, image)

    def getScore(self):
        """获得的分数"""
        return 5

    def outOfBounds(self):
        """是否越界"""

        return self.y < 715

    def step(self):
        """移动"""
        self.y += 3  # 移动步数


Bee
import random
from flyingObject import FlyingObject
from award import Award


class Bee(FlyingObject, Award):

    def __init__(self, screen, image):
        x = random.randint(0, screen.get_rect()[2] - 60)
        y = -50
        super(Bee, self).__init__(screen, x, y, image)
        self.awardType = random.randint(0, 1)
        self.index = True

    def outOfBounds(self):
        """是否越界"""
        return self.y < 715

    def step(self):
        """移动"""
        if self.x + self.width > 480:
            self.index = False
        if self.index == True:
            self.x += 3
        else:
            self.x -= 3
        self.y += 3  # 移动步数

    def getType(self):
        return self.awardType

