from ..controller import Controller


class Logger(Controller):
    def __init__(self, post_handler):
        actions = {
            "logMessage": {
                "params": {
                    "message": "",
                    "prefix": "",
                    "logType": "",
                    "details": ""
                }
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='logger', actions=actions)
