from ..controller import Controller


class Gameworld(Controller):
    def __init__(self, post_handler):
        actions = {
            "getPossibleNewGameworlds": {
                "params": {}
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='gameworld', actions=actions)
