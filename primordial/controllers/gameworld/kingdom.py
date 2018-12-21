from ..controller import Controller


class Kingdom(Controller):
    def __init__(self, post_handler):
        actions = {
            "cancelGovernor": {
                "params": {
                    "governorPlayerId": 0
                }
            },
            "acceptInvitation": {
                "params": {
                    "id": 0
                }
            },
            "getTop3NearbyKings": {
                "params": {
                    "villageId": 0
                }
            },
            "startCoronationCeremony": {
                "params": {
                    "villageId": 0,
                    "tag": ""
                }
            },
            "changeTag": {
                "params": {
                    "tag": ""
                }
            },
            "promoteToDuke": {
                "params": {
                    "playerId": 0,
                    "customText": ""
                }
            },
            "changeDescription": {
                "params": {
                    "groupId": 0,
                    "publicDescription": ""
                }
            },
            "declineInvitation": {
                "params": {
                    "id": 0
                }
            },
            "getFightStrengthRanks": {
                "params": {}
            },
            "getNews": {
                "params": {
                    "start": 0,
                    "count": 0
                }
            },
            "changeInternalDescription": {
                "params": {
                    "groupId": 0,
                    "internalDescription": ""
                }
            },
            "getDukeCandidate": {
                "params": {
                    "kingdomId": 0
                }
            },
            "cancelKingdom": {
                "params": {}
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='kingdom', actions=actions)
