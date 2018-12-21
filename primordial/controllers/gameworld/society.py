from ..controller import Controller


class Society(Controller):
    def __init__(self, post_handler):
        actions = {
            "getSharedInformations": {
                "params": {
                    "villageId": 0
                }
            },
            "create": {
                "params": {
                    "name": "",
                    "attitude": 0,
                    "target": 0,
                    "targetId": 0,
                    "sharedInformations": {
                        "reports": False,
                        "nextAttacks": False,
                        "villageDetails": False
                    },
                    "joinCondition": 0,
                    "conditionValue": 0
                }
            },
            "invite": {
                "params": {
                    "groupId": 0,
                    "groupType": 0,
                    "playerName": [
                        ""
                    ],
                    "customText": ""
                }
            },
            "declineInvitation": {
                "params": {
                    "id": 0
                }
            },
            "changeDescription": {
                "params": {
                    "groupId": 0,
                    "description": 0
                }
            },
            "close": {
                "params": {
                    "groupId": 0,
                    "groupType": 0
                }
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='society', actions=actions)
