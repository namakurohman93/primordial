from ..controller import Controller


class Map(Controller):
    def __init__(self, post_handler):
        actions = {
            "getHeatmapMaximums": {
                "params": {}
            },
            "getByRegionIds": {
                "params": {
                    "regionIdCollection": {
                        "1": [
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0
                        ],
                        "2": [],
                        "3": [],
                        "4": [],
                        "5": [],
                        "6": []
                    }
                }
            },
            "editMapMarkers": {
                "params": {
                    "markers": [
                        {
                            "owner": 0,
                            "type": 0,
                            "color": 0,
                            "editType": 0,
                            "ownerId": 0,
                            "targetId": 0
                        }
                    ],
                    "fieldMessage": {
                        "text": "",
                        "type": 0,
                        "duration": 0,
                        "cellId": 0,
                        "targetId": 0
                    }
                }
            },
            "fieldMarkerMinimize": {
                "params": {
                    "cellId": 0,
                    "isGlobal": 0,
                    "minimizeState": 0
                }
            },
            "fieldMarkerClose": {
                "params": {
                    "id": 0,
                    "isGlobal": 0
                }
            },
            "fieldMarkerDelete": {
                "params": {
                    "id": 0,
                    "isGlobal": 0
                }
            },
            "getKingdomInfluenceStatistics": {
                "params": {
                    "kingId": 0
                }
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='map', actions=actions)
