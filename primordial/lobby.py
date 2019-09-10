import re
import json
import urllib.parse

from .url import URL
from .gameworld import Gameworld
from .http_client import HttpClient
from .controllers.lobby import dual
from .controllers.lobby import cache
from .controllers.lobby import login
from .controllers.lobby import player
from .controllers.lobby import sitter
from .controllers.lobby import gameworld
from .controllers.lobby import achievements
from .controllers.lobby import notification


class Lobby:
    def __init__(self, client=HttpClient()):
        self.client = client
        # Controllers
        self.dual = dual.Dual(post_handler=self.post)
        self.cache = cache.Cache(post_handler=self.post)
        self.login = login.Login(post_handler=self.post)
        self.player = player.Player(post_handler=self.post)
        self.sitter = sitter.Sitter(post_handler=self.post)
        self.gameworld = gameworld.Gameworld(post_handler=self.post)
        self.achievements = achievements.Achievements(post_handler=self.post)
        self.notification = notification.Notification(post_handler=self.post)

    def is_authenticated(self):
        """ Checks whether user is authenticated with the lobby portal """

        if 'error' in self.gameworld.getPossibleNewGameworlds():
            return False
        else:
            return True

    def authenticate(self, email, password):
        """ Authenticates with the lobby portal """

        r = self.client.get(URL.MellonURL.authentication_login)
        msid = re.search(r'msid=([\w]*)&msname', r.text).group(1)

        r = self.client.post(
            url=URL.MellonURL.login_ajax,
            params={'msid': msid, 'msname': 'msid'},
            data={'email': email, 'password': password},
        )
        token = re.search(r'token=([\w]*)&msid', r.text).group(1)

        self.client.get(
            url=URL.LobbyAPI.login,
            params={'token': token, 'msid': msid, 'msname': 'msid'},
        )

        self.client.cookies.set(
            name='msid',
            value=msid,
            domain='.kingdoms.com',
        )

    def connect_to_gameworld(self, gameworld_name, gameworld_id=None, avatar_id=None):
        """ Authenticates and returns a gameworld object """

        gameworld = Gameworld(self.client)
        gameworld.authenticate(
            gameworld_name=gameworld_name,
            gameworld_id=gameworld_id,
            avatar_id=avatar_id,
        )
        return gameworld

    def post(self, controller, action, params={}):
        payload = {
            'action': action,
            'controller': controller,
            'params': params,
            'session': self.session,
        }
        return self.client.post(url=URL.LobbyAPI.index, json=payload).json()

    @property
    def session(self):
        encoded_session = self.client.cookies.get(
            name='gl5SessionKey',
            domain='lobby.kingdoms.com',
        )
        return json.loads(urllib.parse.unquote(encoded_session))['key']
