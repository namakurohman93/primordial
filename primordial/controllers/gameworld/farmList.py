from ..controller import Controller


class FarmList(Controller):
    def __init__(self, post_handler):
        actions = {
            "toggleEntry": {
                "params": {
                    "villageId": 0,
                    "listId": 0
                }
            },
            "getAttackInfo": {
                "params": {
                    "currentVillageId": 0,
                    "farmlistIds": [
                        0
                    ]
                }
            },
            "editTroops": {
                "params": {
                    "entryIds": [
                        0,
                        0
                    ],
                    "units": {
                        "1": 0,
                        "2": 0,
                        "3": 0,
                        "4": 0,
                        "5": 0,
                        "6": 0
                    }
                }
            },
            "createList": {
                "params": {
                    "name": ""
                }
            },
            "copyEntry": {
                "params": {
                    "villageId": 0,
                    "newListId": 0,
                    "entryId": 0
                }
            },
            "deleteList": {
                "params": {
                    "listId": 0
                }
            },
            "deleteEntry": {
                "params": {
                    "entryId": 0
                }
            },
            "checkTarget": {
                "params": {
                    "villageId": 0
                }
            },
            "addEntry": {
                "params": {
                    "villageId": 0,
                    "listId": 0
                }
            },
            "editList": {
                "params": {
                    "name": "",
                    "listId": 0
                }
            },
            "changeListOrder": {
                "params": {
                    "listIds": [
                        0,
                        0
                    ]
                }
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='farmList', actions=actions)
