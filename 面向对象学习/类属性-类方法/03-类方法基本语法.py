#类属性：：
class Tool(object):

    #使用赋值语句定义类属性，记录所有工具对象的数量：
    count = 0

    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量为 %d" % cls.count)

    def __init__(self, name):
        self.name = name

       #让类属性的值+1
        Tool.count += 1

t1 =Tool("斧头")
t2 = Tool("榔头")
Tool.show_tool_count()