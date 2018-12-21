from ..controller import Controller


class Ranking(Controller):
    def __init__(self, post_handler):
        actions = {
            "getKingdomVictoryPointsWithTreasures": {
                "params": {
                    "start": 0,
                    "end": 0
                }
            },
            "getKingdomStats": {
                "params": {
                    "kingdomId": 0
                }
            },
            "getRanking": {
                "params": {
                    "start": 0,
                    "end": 0,
                    "rankingType": "",
                    "rankingSubtype": ""
                }
            },
            "getRankingAveragePoints": {
                "params": {
                    "rankingType": "",
                    "rankingSubType": ""
                }
            },
            "getRankAndCount": {
                "params": {
                    "id": 0,
                    "rankingType": "",
                    "rankingSubtype": ""
                }
            },
            "getWorldStats": {
                "params": {}
            },
            "getKingdomInternalRanking": {
                "params": {}
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='ranking', actions=actions)
