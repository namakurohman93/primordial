from ..controller import Controller


class Error(Controller):
    def __init__(self, post_handler):
        actions = {
            "logJavascriptError": {
                "params": {
                    "playerId": 0,
                    "error": ""
                }
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='error', actions=actions)
