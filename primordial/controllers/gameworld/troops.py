from ..controller import Controller


class Troops(Controller):
    def __init__(self, post_handler):
        actions = {
            "getMarkers": {
                "params": {}
            },
            "setMarker": {
                "params": {
                    "troopId": 0,
                    "marker": 0
                }
            },
            "abortTroopMovement": {
                "params": {
                    "troopId": 0
                }
            },
            "checkTarget": {
                "params": {
                    "destVillageName": "",
                    "destVillageId": 0,
                    "villageId": 0,
                    "movementType": 0,
                    "redeployHero": False,
                    "heroPresent": False,
                    "selectedUnits": {
                        "1": 0,
                        "2": 0,
                        "3": 0,
                        "4": 0,
                        "5": 0,
                        "6": 0,
                        "7": 0,
                        "8": 0,
                        "9": 0,
                        "10": 0,
                        "11": 0
                    }
                }
            },
            "send": {
                "params": {
                    "destVillageId": 0,
                    "villageId": 0,
                    "movementType": 0,
                    "redeployHero": False,
                    "units": {
                        "1": 0,
                        "2": 0,
                        "3": 0,
                        "4": 0,
                        "5": 0,
                        "6": 0,
                        "7": 0,
                        "8": 0,
                        "9": 0,
                        "10": 0,
                        "11": 0
                    },
                    "spyMission": ""
                }
            },
            "startPartialFarmListRaid": {
                "params": {
                    "listId": 0,
                    "entryIds": [
                        0,
                        0
                    ],
                    "villageId": 0
                }
            },
            "startFarmListRaid": {
                "params": {
                    "listIds": [
                        0
                    ],
                    "villageId": 0
                }
            },
            "fightSimulate": {
                "params": {
                    "attackType": 0,
                    "attackerTribe": 0,
                    "attackerUnits": {
                        "2": 0,
                        "4": 0,
                        "5": 0
                    },
                    "defenderTribe": [
                        0
                    ],
                    "defenderUnits": [
                        {
                            "1": 0,
                            "2": 0,
                            "3": 0,
                            "4": 0,
                            "5": 0,
                            "6": 0,
                            "7": 0,
                            "8": 0,
                            "9": 0,
                            "10": 0,
                            "11": 0
                        }
                    ],
                    "heroOffBonus": [
                        0,
                        0
                    ],
                    "heroDefBonus": [
                        0,
                        0
                    ],
                    "heroItemType": [
                        0,
                        0
                    ],
                    "heroFightStrength": [
                        0,
                        0
                    ],
                    "attackerResearch": {
                        "1": 0,
                        "2": 0,
                        "3": 0,
                        "4": 0,
                        "5": 0,
                        "6": 0,
                        "7": 0,
                        "8": 0,
                        "9": 0
                    },
                    "defenderResearch": [
                        {
                            "1": 0,
                            "2": 0,
                            "3": 0,
                            "4": 0,
                            "5": 0,
                            "6": 0,
                            "7": 0,
                            "8": 0,
                            "9": 0
                        }
                    ],
                    "attPopulation": 0,
                    "defPopulation": 0,
                    "catapultTargetLevel": 0,
                    "catapultTargetLevel2": 0,
                    "masonLevel": 0,
                    "wallLevel": 0,
                    "palaceLevel": 0,
                    "moatLevel": 0,
                    "natarBonus": 0,
                    "heroMounted": [
                        0,
                        0
                    ]
                }
            },
            "moveTroopsHome": {
                "params": {
                    "troopId": 0,
                    "units": {
                        "1": 0,
                        "2": 0,
                        "3": 0,
                        "4": 0,
                        "5": 0,
                        "6": 0,
                        "7": 0,
                        "8": 0,
                        "9": 0,
                        "10": 0,
                        "11": 0
                    }
                }
            },
            "disband": {
                "params": {
                    "troopId": 0
                }
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='troops', actions=actions)
