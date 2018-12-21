from ..controller import Controller


class Trade(Controller):
    def __init__(self, post_handler):
        actions = {
            "changeTradeRouteStatus": {
                "params": {
                    "id": 0,
                    "status": 0
                }
            },
            "deleteTradeRoute": {
                "params": {
                    "id": 0
                }
            },
            "checkTarget": {
                "params": {
                    "sourceVillageId": 0,
                    "destVillageId": 0,
                    "destVillageName": ""
                }
            },
            "createOffer": {
                "params": {
                    "villageId": 0,
                    "offeredResource": 0,
                    "offeredAmount": 0,
                    "searchedResource": 0,
                    "searchedAmount": 0,
                    "kingdomOnly": False
                }
            },
            "cancelOffer": {
                "params": {
                    "offerId": 0
                }
            },
            "getOfferList": {
                "params": {
                    "villageId": 0,
                    "search": 0,
                    "offer": 0,
                    "rate": 0,
                    "start": 0,
                    "count": 0
                }
            },
            "acceptOffer": {
                "params": {
                    "offerId": 0,
                    "villageId": 0
                }
            },
            "sendResources": {
                "params": {
                    "destVillageId": 0,
                    "recurrences": 0,
                    "resources": [
                        0,
                        0,
                        0,
                        0
                    ],
                    "sourceVillageId": 0
                }
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='trade', actions=actions)
