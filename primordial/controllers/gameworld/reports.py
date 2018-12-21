from ..controller import Controller


class Reports(Controller):
    def __init__(self, post_handler):
        actions = {
            "getLastReports": {
                "params": {
                    "collection": "",
                    "start": 0,
                    "count": 0,
                    "filters": [],
                    "alsoGetTotalNumber": False
                }
            },
            "getFullReport": {
                "params": {
                    "id": "",
                    "collection": "",
                    "securityCode": ""
                }
            },
            "markAsFavorite": {
                "params": {
                    "id": "",
                    "collection": "",
                    "securityCode": ""
                }
            },
            "shareReport": {
                "params": {
                    "id": "",
                    "shareWith": "",
                    "shareParam": 0,
                    "shareMessage": "",
                    "collection": ""
                }
            },
            "removeAsFavorite": {
                "params": {
                    "bodyId": ""
                }
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='reports', actions=actions)
