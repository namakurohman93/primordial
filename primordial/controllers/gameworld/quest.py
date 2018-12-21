from ..controller import Controller


class Quest(Controller):
    def __init__(self, post_handler):
        actions = {
            "getPuzzle": {
                "params": {}
            },
            "solvePuzzle": {
                "params": {
                    "moves": [
                        [],
                        [],
                        [],
                        [],
                        [],
                        [],
                        []
                    ]
                }
            },
            "dialogAction": {
                "params": {
                    "questId": 0,
                    "dialogId": 0,
                    "command": ""
                }
            },
            "checkRewardCollectible": {
                "params": {
                    "questId": 0,
                    "villageId": 0
                }
            },
            "collectReward": {
                "params": {
                    "questId": 0,
                    "villageId": 0
                }
            },
            "resetDailyQuest": {
                "params": {
                    "questId": 0
                }
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='quest', actions=actions)
