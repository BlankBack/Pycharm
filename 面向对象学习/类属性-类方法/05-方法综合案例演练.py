class Game(object):

    #历史最高分
    top_score = 0

    def __init__(self, player_name):
        #游戏人姓名
        self.player_name = player_name

    #静态方法
    @staticmethod
    def show_help():
        print("显示游戏信息")

    #类方法
    @classmethod
    def show_top_score(cls):
        print("当前游戏最高分为：%d " % cls.top_score)

    #实例方法
    def start_game(self):
        print("%s 游戏开始：" % self.player_name)

Game.show_help()
Game.show_top_score()

game = Game("zl")
game.start_game()

