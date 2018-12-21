from ..controller import Controller


class Sitter(Controller):
    def __init__(self, post_handler):
        actions = {
            "add": {
                "params": {
                    "avatarIdentifier": 0,
                    "consumersId": "",
                    "avatarName": "",
                    "email": ""
                }
            },
            "setPermissions": {
                "params": {
                    "avatarIdentifier": 0,
                    "sitterAccountIdentifier": 0,
                    "permissions": {
                        "1": False,
                        "2": False,
                        "3": False,
                        "4": False
                    }
                }
            },
            "remove": {
                "params": {
                    "avatarIdentifier": 0,
                    "sitterAccountIdentifier": 0
                }
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='sitter', actions=actions)
