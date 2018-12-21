from ..controller import Controller


class Cache(Controller):
    def __init__(self, post_handler):
        actions = {
            "get": {
                "params": {
                    "names": [
                        "",
                        "",
                        "",
                        "",
                        ""
                    ]
                }
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='cache', actions=actions)
