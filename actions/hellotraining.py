import sys
from st2common.runners.base_action import Action

class MyAction(Action):
    
    def run(self,num1):
        
        for x in range(num1):
            for y in range(x)
                print('*',end=" ")
            print("\n")
        return(True)
