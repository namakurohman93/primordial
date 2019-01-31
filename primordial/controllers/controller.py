class ActionNotImplemented(Exception):
    """ Action not implemented """


class MissingParameter(Exception):
    """ Missing required parameter """


class Controller:
    def __init__(self, post_handler, controller, actions):
        self._post = post_handler
        self.controller = controller
        self.actions = actions

    def __getattr__(self, name):
        try:
            return self._fabricate_function(name)
        except KeyError:
            raise ActionNotImplemented(name)

    def __dir__(self):
        return [action for action in self.actions.keys()]

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, name):
        self.__dict__.update(name)

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

            response = self._post(controller=self.controller, action=action_name, params=params)
            return response

        # Allows us to check/return the required parameters of a fabricated function
        action.params = self.actions[action_name]['params']

        return action
