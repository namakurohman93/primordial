from ..controller import Controller


class Auctions(Controller):
    def __init__(self, post_handler):
        actions = {
            "getRunningAuctionAmount": {
                "params": {
                    "filterItemType": 0,
                    "filterSlot": 0,
                    "page": 0
                }
            },
            "getRunningAuctionPage": {
                "params": {
                    "filterItemType": 0,
                    "filterSlot": 0,
                    "page": 0
                }
            },
            "placeBid": {
                "params": {
                    "auctionId": 0,
                    "bidAmount": 0
                }
            },
            "getSellerPayout": {
                "params": {
                    "itemId": 0,
                    "amount": 0
                }
            },
            "sellItem": {
                "params": {
                    "itemId": 0,
                    "amount": 0
                }
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='auctions', actions=actions)
