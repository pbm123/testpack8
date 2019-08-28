import sys
from st2common.runners.base_action import Action

class MyAction(Action):
    
    def run(self,num1):
        requests
        response
        response = requests.get("http://api.open-notify.org/iss-now.json")
        print(response.status_code)
        return(True)
