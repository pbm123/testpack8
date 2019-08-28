import sys
from st2common.runners.base_action import Action

class MyAction(Action):
    
    def run(self,sub1,marks1,sub2,marks2,sub3,marks3):
        thisdict = {}
        thisdict[sub1]=marks1
        thisdict[sub2]=marks2
        thisdict[sub3]=marks3
        for x in thisdict:
            print(x+(str)thisdict[x])
        return(True)
