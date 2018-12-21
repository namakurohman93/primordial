from ..controller import Controller, MissingParameter


class PremiumFeature(Controller):
    def __init__(self, post_handler):
        actions = {
            "saveAutoExtendFlags": {
                "params": {
                    "autoExtendFlags": 0
                }
            },
            "treasureResourcesInstant": {
                "params": {
                    "troopId": 0
                }
            },
            "cardgameSingle": {
                "params": {
                    "selectedCard": 0
                }
            },
            "cardgame4of5": {
                "params": {}
            },
            "starterPackage": {
                "params": {}
            },
            "buildingMasterSlot": {
                "params": {}
            },
            "exchangeOffice": {
                "params": {
                    "amount": 0,
                    "type": ""
                }
            },
            "NPCTrader": {
                "params": {
                    "villageId": 0,
                    "distributeRes": {
                        "1": 0,
                        "2": 0,
                        "3": 0,
                        "4": 0
                    }
                }
            },
            "finishNow": {
                "params": {
                    "villageId": 0,
                    "queueType": 0,
                    "price": 0
                }
            },
            "plusAccount": {
                "params": {}
            },
            "productionBonus": {
                "params": {}
            },
            "cropProductionBonus": {
                "params": {}
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='premiumFeature', actions=actions)

    # Overriding Controller class _fabricate_function method due to inconsistencies of
    # premiumFeature controller payloads all having the same action name but different secondary
    # action names
    def _fabricate_function(self, action_name):
        """
        Fabricates a function so we can call dict elements in self.actions as if they were
        functions

        We take this approach due to the extensive amount of actions provided by the controllers
        we implement
        """

        def action(params={}):
            required_params = self.actions[action_name]['params']

            # Check that all params are supplied as required by the action
            for key in required_params.keys():
                try:
                    assert key in params.keys()
                except AssertionError:
                    raise MissingParameter(key)

            # Shift params and action 1 layer in, action becoming featureName
            if action_name is not 'saveAutoExtendFlags':
                real_action_name = 'bookFeature'
                real_params = {
                    "featureName": action_name,
                    "params": params
                }

                response = self._post(
                    controller=self.controller, action=real_action_name, params=real_params)
                return response

        # Allows us to check/return the required parameters of a fabricated function
        action.params = self.actions[action_name]['params']

        return action
