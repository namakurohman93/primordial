import json
from urllib import parse
from .http_client import HttpClient
from .gameworld import Gameworld
from .controllers.lobby import (
    achievements, cache, dual, gameworld, login, notification, player, sitter
)


class Lobby():
    api_root = 'https://lobby.kingdoms.com/api/index.php'

    def __init__(self, proxies=None):
        self.client = HttpClient(proxies=proxies)

        self.msid = ''
        self.session_key = ''

        self.achievements = achievements.Achievements(post_handler=self.post)
        self.cache = cache.Cache(post_handler=self.post)
        self.dual = dual.Dual(post_handler=self.post)
        self.gameworld = gameworld.Gameworld(post_handler=self.post)
        self.login = login.Login(post_handler=self.post)
        self.notification = notification.Notification(post_handler=self.post)
        self.player = player.Player(post_handler=self.post)
        self.sitter = sitter.Sitter(post_handler=self.post)

    def is_authenticated(self):
        """ Checks whether user is authenticated with the lobby portal """

        if 'error' in self.gameworld.getPossibleNewGameworlds():
            return False
        else:
            return True

    def authenticate(self, email, password):
        """ Authenticates with the lobby portal """

        mellon_root_url = 'https://mellon-t5.traviangames.com'

        # STEP 1
        response = self.client.get(f'{mellon_root_url}/authentication/login')
        # Fish out the 26 char long msid
        self.msid = response.text[response.text.find('msid=')+5: response.text.find('msid=')+31]

        # STEP 2
        credentials = {'email': email, 'password': password}
        response = self.client.post(
            url=f'{mellon_root_url}/authentication/login/ajax/form-validate?msid={self.msid}&msname=msid',
            data=credentials)

        # STEP 3
        # Fish out the 38 char long token
        token = response.text[response.text.find('token=')+6: response.text.find('token=')+38]
        response = self.client.get(
            f'https://lobby.kingdoms.com/api/login.php?token={token}&msid={self.msid}&msname=msid')

        encoded_session_key = self.client.session.cookies.get('gl5SessionKey', domain='.kingdoms.com')
        decoded_session_key = parse.unquote(encoded_session_key)
        self.session_key = json.loads(decoded_session_key)['key']

    def connect_to_gameworld(self, gameworld_id, gameworld_name):
        """ Authenticates and returns a gameworld object """

        gameworld = Gameworld(client=self.client, msid=self.msid)
        gameworld.authenticate(gameworld_id=gameworld_id, gameworld_name=gameworld_name)
        return gameworld

    def post(self, controller, action, params={}):
        params = {
            'action': action,
            'controller': controller,
            'params': params,
            'session': self.session_key
            }
        response = self.client.post(url=Lobby.api_root, data=json.dumps(params))
        return response.json()
