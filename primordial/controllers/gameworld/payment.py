from ..controller import Controller


class Payment(Controller):
    def __init__(self, post_handler):
        actions = {
            "getPaymentShopUrl": {
                "params": {
                    "shopVersion": 0
                }
            },
            "getSmallestPackage": {
                "params": {
                    "featurePrice": 0
                }
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='payment', actions=actions)
