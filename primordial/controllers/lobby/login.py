from ..controller import Controller


class Login(Controller):
    def __init__(self, post_handler):
        actions = {
            "logout": {
                "params": {}
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='login', actions=actions)
