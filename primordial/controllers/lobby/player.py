from ..controller import Controller


class Player(Controller):
    def __init__(self, post_handler):
        actions = {
            "switchCountry": {
                "params": {
                    "country": ""
                }
            },
            "saveName": {
                "params": {
                    "accountName": ""
                }
            },
            "getAll": {
                "params": {}
            },
            "getAvatarData": {
                "params": {}
            },
            "getPrestigeOnWorlds": {
                "params": {
                    "type": ""
                }
            },
            "getAccountDetails": {
                "params": {}
            },
            "deleteAvatar": {
                "params": {
                    "avatarIdentifier": 0
                }
            },
            "abortDeletion": {
                "params": {
                    "avatarIdentifier": 0
                }
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='player', actions=actions)
