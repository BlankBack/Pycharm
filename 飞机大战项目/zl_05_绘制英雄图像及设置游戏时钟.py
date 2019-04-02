import pygame

# 游戏的初始化
pygame.init()
#创建游戏的窗口 480*700
screen = pygame.display.set_mode((480,700))
# 绘制背景图像:
# 1> 加载图像数据
background = pygame.image.load("./images/background.png")
# 2> blit 绘制图像
screen.blit(background, (0, 0))

# 英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(155,500))

# 3> update 更新屏幕显示
# 可以在所有绘制工作完成后在统一调用 update方法，节省内容
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()




# 游戏循环 -> 意味着游戏的正式开始
i = 0

while True:
    # 可以指定循环体内部的代码执行的频率
    clock.tick(60)
    print(i)
    i += 1

pygame.quit()