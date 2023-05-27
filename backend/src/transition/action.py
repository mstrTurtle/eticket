'''
这是预设的“动作”，可以用来绑在transition上。

用反射机制来实现，所以这些类不用手动注册了。

每个动作依赖于隐式参数和显示参数。并且会更改自动机的一些状态，或者产生一些外部作用（如发送邮件，etc）
'''


class Reject:
    descrip = "驳回给发起人"
    def __init__(self,config) -> None:
        self.config=config

    def run(args): # 传入显示参数字典
        pass

class ReferUnicast:
    descrip = "指名道姓的点播"
    def __init__(self,config) -> None:
        self.config=config

    def run(args): # 传入显示参数字典
        pass

class PredefUnicast:
    descrip = "预设的点播"
    def __init__(self,config) -> None:
        self.config=config

    def run(args): # 传入显示参数字典
        pass

class PredefMulticast:
    descrip="预设的组播"
    def __init__(self,config) -> None:
        self.config=config

    def run(args): # 传入显示参数字典
        pass
