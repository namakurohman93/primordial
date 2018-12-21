from ..controller import Controller


class Hero(Controller):
    def __init__(self, post_handler):
        actions = {
            "getValuePoints": {
                "params": {}
            },
            "addAttributePoints": {
                "params": {
                    "fightStrengthPoints": 0,
                    "attBonusPoints": 0,
                    "defBonusPoints": 0,
                    "resBonusPoints": 0,
                    "resBonusType": 0
                }
            },
            "mergeItem": {
                "params": {
                    "id": 0,
                    "amount": 0,
                    "villageId": 0
                }
            },
            "saveFace": {
                "params": {
                    "face": {
                        "mouth": 0,
                        "beard": 0,
                        "hair": 0,
                        "eye": 0,
                        "eyebrow": 0,
                        "ear": 0,
                        "nose": 0
                    },
                    "gender": 0,
                    "hairColor": 0,
                    "playerId": 0,
                    "fetchedFromLobby": 0
                }
            },
            "getLastInventoryView": {
                "params": {}
            },
            "getTreasureSellPrice": {
                "params": {}
            },
            "getDurationToClosestVillageWithInfluence": {
                "params": {
                    "villageId": 0
                }
            },
            "useItem": {
                "params": {
                    "id": 0,
                    "amount": 0,
                    "villageId": 0
                }
            },
            "setLastInventoryView": {
                "params": {}
            },
            "getResourceForResourceChest": {
                "params": {
                    "percent": 0,
                    "type": 0
                }
            },
            "upgradeItem": {
                "params": {
                    "upgradeItemId": 0,
                    "targetItemId": 0
                }
            },
            "revive": {
                "params": {
                    "villageId": 0
                }
            },
            "confirmHeroLevelUp": {
                "params": {}
            },
            "switchItems": {
                "params": {
                    "id1": 0,
                    "id2": 0
                }
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='hero', actions=actions)
