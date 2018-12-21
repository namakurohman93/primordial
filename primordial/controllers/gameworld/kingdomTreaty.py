from ..controller import Controller


class KingdomTreaty(Controller):
    def __init__(self, post_handler):
        actions = {
            "offer": {
                "params": {
                    "kingdomId": 0,
                    "type": 0
                }
            },
            "deny": {
                "params": {
                    "id": 0
                }
            },
            "cancel": {
                "params": {
                    "id": 0
                }
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='kingdomTreaty', actions=actions)
