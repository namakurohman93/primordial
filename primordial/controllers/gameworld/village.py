from ..controller import Controller


class Village(Controller):
    def __init__(self, post_handler):
        actions = {
            "clickSpecial": {
                "params": {
                    "id": 0
                }
            },
            "toggleAllowTributeCollection": {
                "params": {
                    "villageId": 0
                }
            },
            "getVillagesWithInfluenceOnOasisForPlayer": {
                "params": {
                    "oasisId": 0,
                    "playerId": 0
                }
            },
            "getKingdomVillageAttacks": {
                "params": {}
            },
            "getProductionDetails": {
                "params": {
                    "villageId": 0
                }
            },
            "useOasis": {
                "params": {
                    "oasisId": 0,
                    "villageId": 0
                }
            },
            "clearOasis": {
                "params": {
                    "oasisId": 0,
                    "villageId": 0
                }
            },
            "updateName": {
                "params": {
                    "villageId": 0,
                    "villageName": ""
                }
            },
            "checkUnitProduction": {
                "params": {
                    "villageId": 0
                }
            },
            "getTreasuriesCapacity": {
                "params": {
                    "villageId": 0
                }
            },
            "getVictoryPointsAndInfluenceBonus": {
                "params": {
                    "villageId": 0
                }
            }
        },

        Controller.__init__(self, post_handler=post_handler, controller='village', actions=actions)
