import sys
from st2common.runners.base_action import Action

class MyAction(Action):
    
    def run(self, a,b,c):
        thislist = []
        thislist.append(a)
        thislist.append(b)
        thislist.append(c)
        print(thislist)
        return(True)
