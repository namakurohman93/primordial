from ..controller import Controller


class Dual(Controller):
    def __init__(self, post_handler):
        actions = {
            "add": {
                "params": {
                    "avatarIdentifier": 0,
                    "consumersId": "",
                    "avatarName": "",
                    "email": ""
                }
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='dual', actions=actions)
