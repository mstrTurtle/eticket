'''
一个工作流引擎。
'''

from dataclasses import dataclass

@dataclass
class Node:
    fields=None

@dataclass
class Transition:
    desc=None # 描述，包括verb和跳转之后的状态。
    action=None # 该转移将要触发的动作。

@dataclass
class Workflow:
    nodes = None
    transitions = None
    name = None # 动听的名字，如“维修工单”，“采购工单”


class WorkflowEngine:
    def __init__(self, workflow) -> None:
        self.workflow = workflow
        self.context = None
        
    def setInit(self):
        pass

    def currentNode(self):
        pass

    def availableTransitions(self):
        pass

    def setContext(self): # 记得把context序列化进db。
        pass

    def getContext(self): # 记得要返回一个拷贝，不让外部乱改。
        pass
    

def makeEnginesFromDb(): # Engine工厂，从DB描述的状态机来创建真的状态机。
    pass


def makeExampleEngine():
    pass

class FakeEngine:
    STATE_BLANK=0
    STATE_FILLED=1
    STATE_APPROVED=2
    STATE_DONE=3
    STATE_CLOSED=99
    
    def setInit(self):
        pass

    def currentNode(self):
        pass

    def availableTransitions(self):
        pass

    def setContext(self): # 记得把context序列化进db。
        pass

    def getContext(self): # 记得要返回一个拷贝，不让外部乱改。
        pass