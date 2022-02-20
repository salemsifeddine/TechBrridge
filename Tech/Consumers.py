from email import message
from time import sleep
from channels.generic.websocket import WebsocketConsumer
import json
from random import  randint
# from . import  hw_server ,  hw_sim
from . import hw_sim

class WSConsumer(WebsocketConsumer):
    
    def connect(self):
        self.accept()
        


        for i in range(10):
            # self.send(json.dumps({"message":randint(1,100)}))
            hw_sim.simulate()
            # print({"message":randint(1,100)})
            # hw_sim.send_data()
            sleep(1)
