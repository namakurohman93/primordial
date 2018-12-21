import json
from sys import argv
from time import time
from extracted_data import gameworld_actions


def get_type_default(param):
    if type(param) is int:
        return 0
    elif type(param) is float:
        return 0.0
    elif type(param) is bool:
        return False
    elif type(param) is str:
        try:
            # Catch ints masquerading as strings
            int(param)
            if '.' in param:
                # Catch floats masquerading as strings
                return 0.0
            else:
                return 0
        except ValueError:
            # Not an int or a float
            return ''


def conform(data):
    if not isinstance(data, (list, dict)):
        return get_type_default(data)
    elif isinstance(data, list):
        _data = data.copy()
        tmp = []
        for item in data:
            tmp += [conform(item)]
        return tmp
    elif isinstance(data, dict):
        _data = data.copy()
        for key, value in data.items():
            _data[key] = conform(value)
        return _data


def convert_to_dict(entries):
    """
    Extracts request text strings from a .har file, loads them as json and conforms them to the
    structure definition that we require to work with it further
    """

    _post_data = []
    post_data = []
    premium_feature = []
    result = {}

    for entry in entries:
        # Exract json loadable text string, load into a dict and stack into post_data
        try:
            _post_data += [json.loads(entry['request']['postData']['text'])]
        except (KeyError, json.decoder.JSONDecodeError):
            # Not all requests are going to have postData
            pass

    # Separate premiumFeature controller from other controllers as it contains a different
    # data structure so we need to deal with it differently. In particular, we want premiumFeature
    # controller action bookFeature data sets
    premium_feature = [x for x in _post_data if 'action' in x.keys() and x['action'] == 'bookFeature']
    post_data = [x for x in _post_data if 'controller' in x.keys() and x['controller'] != 'premiumFeature']

    # Grab controllers
    for item in post_data:
        controller = item['controller']
        result[controller] = {}

    # Grab actions
    for item in post_data:
        controller = item['controller']
        action = item['action']
        try:
            result[controller][action] = conform(item['params'])
        except KeyError:
            pass

    # NOTE: There are no unique params as far as we're aware right now
    # # Grab unique params
    # for item in post_data:
    #     controller = item['controller']
    #     action = item['action']
    #     params = item['params']
    #
    #     for param in params.keys():
    #         # Deal with singletons
    #         if isinstance(params[param], (int, float, str, bool)):
    #             if param not in data[controller][action].keys():
    #                 data[controller][action][param] = conform(params[param])
    #         # Deal with lists and dicts
    #         elif isinstance(params[param], (list, dict)):
    #             if param not in data[controller][action].keys():
    #                 data[controller][action][param] = conform(params[param])

    # Process premiumFeature
    if premium_feature:
        result['premiumFeature'] = {}

        # Grab 2nd level actions (featureName) and conform the controller to the default controller
        # format
        for item in premium_feature:
            action = item['params']['featureName']
            result['premiumFeature'][action] = conform(item['params']['params'])

    return result


def compare(new_data):
    existing_data = gameworld_actions.actions
    result = {}

    # Check for new controllers
    for controller, value in new_data.items():
        if controller not in existing_data.keys():
            print(f'New controller found:\t{controller}')
            # Copy the whole controller dictionary over
            result[controller] = value

    for controller, value in new_data.items():
        # Avoid double-dipping newly detected controllers, otherwise will throw KeyError since
        # new controllers were saved in result but existing_data remains not updated
        if controller in existing_data.keys():
            for action in value.keys():
                # print(f'\t{controller.upper()} {action}')
                if action not in existing_data[controller].keys():
                    print(f'New {controller} action found:\t{action}')
                    try:
                        result[controller][action] = new_data[controller][action]
                    # Controller does not exist in result
                    except KeyError:
                        result[controller] = {}
                        result[controller][action] = new_data[controller][action]

    return result


if __name__ == '__main__':
    try:
        har_file = argv[1]

    except IndexError:
        print('Usage: python action_extractor.py <har_file.har>')
        raise

    with open(har_file, 'r') as f:
        har_data = f.read()
        json_har_data = json.loads(har_data)
        entries = json_har_data['log']['entries']
        result = convert_to_dict(entries)
        compared_result = compare(result)

        if compared_result:
            with open(f'results_{int(time())}.json', 'w') as f:
                f.write(json.dumps(compared_result, indent=4))
        else:
            print(f'No new data found')
