from ..controller import Controller


class Building(Controller):
    def __init__(self, post_handler):
        actions = {
            "getCelebrationList": {
                "params": {
                    "villageId": 0,
                    "locationId": 0
                }
            },
            "startCelebration": {
                "params": {
                    "villageId": 0,
                    "type": 0
                }
            },
            "getBuildingList": {
                "params": {
                    "villageId": 0,
                    "locationId": 0
                }
            },
            "getTrapperInfos": {
                "params": {
                    "villageId": 0,
                    "locationId": 0
                }
            },
            "buildTraps": {
                "params": {
                    "villageId": 0,
                    "locationId": 0,
                    "amount": 0
                }
            },
            "upgrade": {
                "params": {
                    "villageId": 0,
                    "locationId": 0,
                    "buildingType": 0
                }
            },
            "getRecruitList": {
                "params": {
                    "villageId": 0,
                    "locationId": 0
                }
            },
            "recruitUnits": {
                "params": {
                    "villageId": 0,
                    "locationId": 0,
                    "units": {
                        "1": 0
                    }
                }
            },
            "useMasterBuilder": {
                "params": {
                    "villageId": 0,
                    "locationId": 0,
                    "buildingType": 0,
                    "reserveResources": False
                }
            },
            "getOasisList": {
                "params": {
                    "villageId": 0
                }
            },
            "getCulturePointBalance": {
                "params": {
                    "villageId": 0
                }
            },
            "reserveResources": {
                "params": {
                    "villageId": 0,
                    "entryId": 0
                }
            },
            "cancel": {
                "params": {
                    "villageId": 0,
                    "eventId": 0
                }
            },
            "researchUnit": {
                "params": {
                    "villageId": 0,
                    "locationId": 0,
                    "buildingType": 0,
                    "unitType": 0
                }
            },
            "shiftMasterBuilder": {
                "params": {
                    "villageId": 0,
                    "from": 0,
                    "to": 0
                }
            },
            "destroy": {
                "params": {
                    "villageId": 0,
                    "locationId": 0
                }
            },
            "getTreasuryTransformations": {
                "params": {}
            },
            "transformTreasury": {
                "params": {
                    "villageId": 0,
                    "locationId": 0
                }
            },
            "getCpData": {
                "params": {
                    "villageId": 0
                }
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='building', actions=actions)
