from ..controller import Controller


class Achievements(Controller):
    def __init__(self, post_handler):
        actions = {
            "update": {
                "params": {}
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='achievements', actions=actions)
