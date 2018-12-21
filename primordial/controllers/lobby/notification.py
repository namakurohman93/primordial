from ..controller import Controller


class Notification(Controller):
    def __init__(self, post_handler):
        actions = {
            "markAsRead": {
                "params": {
                    "id": 0
                }
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='notification', actions=actions)
