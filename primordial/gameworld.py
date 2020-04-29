import re
import json
import time
import urllib.parse

from .url import URL
from .controllers.gameworld import map
from .controllers.gameworld import hero
from .controllers.gameworld import cache
from .controllers.gameworld import error
from .controllers.gameworld import login
from .controllers.gameworld import quest
from .controllers.gameworld import trade
from .controllers.gameworld import logger
from .controllers.gameworld import player
from .controllers.gameworld import troops
from .controllers.gameworld import kingdom
from .controllers.gameworld import payment
from .controllers.gameworld import ranking
from .controllers.gameworld import reports
from .controllers.gameworld import society
from .controllers.gameworld import village
from .controllers.gameworld import auctions
from .controllers.gameworld import building
from .controllers.gameworld import farmList
from .controllers.gameworld import kingdomTreaty
from .controllers.gameworld import premiumFeature


class Gameworld:
    def __init__(self, client, gameworld_name, gameworld_id=None, avatar_id=None):
        self.gameworld_api = f'{URL.GameworldAPI}'.format(gameworld_name.lower())
        self.gameworld_name = gameworld_name
        self.gameworld_id = gameworld_id
        self.avatar_id = avatar_id
        self.client = client
        # Controllers
        self.map = map.Map(post_handler=self.post)
        self.hero = hero.Hero(post_handler=self.post)
        self.cache = cache.Cache(post_handler=self.post)
        self.error = error.Error(post_handler=self.post)
        self.login = login.Login(post_handler=self.post)
        self.quest = quest.Quest(post_handler=self.post)
        self.trade = trade.Trade(post_handler=self.post)
        self.logger = logger.Logger(post_handler=self.post)
        self.player = player.Player(post_handler=self.post)
        self.troops = troops.Troops(post_handler=self.post)
        self.kingdom = kingdom.Kingdom(post_handler=self.post)
        self.payment = payment.Payment(post_handler=self.post)
        self.ranking = ranking.Ranking(post_handler=self.post)
        self.reports = reports.Reports(post_handler=self.post)
        self.society = society.Society(post_handler=self.post)
        self.village = village.Village(post_handler=self.post)
        self.auctions = auctions.Auctions(post_handler=self.post)
        self.building = building.Building(post_handler=self.post)
        self.farmList = farmList.FarmList(post_handler=self.post)
        self.kingdomTreaty = kingdomTreaty.KingdomTreaty(post_handler=self.post)
        self.premiumFeature = premiumFeature.PremiumFeature(post_handler=self.post)

    def is_authenticated(self):
        """ Checks whether user is authenticated with the gameworld """

        if 'error' in self.troops.getMarkers():
            return False
        else:
            return True

    def authenticate(self):
        """ Authenticates with the gameworld """

        if self.gameworld_id:
            r = self.client.get(
                url=URL.MellonURL.join_gameworld.format(self.gameworld_id),
                params={'msid': self.msid, 'msname': 'msid'},
            )

        if self.avatar_id:
            r = self.client.get(
                url=URL.MellonURL.join_as_guest.format(self.avatar_id),
                params={'msid': self.msid, 'msname': 'msid'},
            )

        token = re.search(r'token=([\w]*)&msid', r.text).group(1)

        self.client.get(
            url=URL.GameworldAPI.login.format(self.gameworld_name.lower()),
            params={'token': token, 'msid': self.msid, 'msname': 'msid'}
        )

    def post(self, controller, action, params={}):
        payload = {
            'action': action,
            'controller': controller,
            'params': params,
            'session': self.session,
        }

        url = '?'.join(
            [
                self.gameworld_api,
                urllib.parse.urlencode({
                    'controller': controller,
                    'action': action
                })
            ]
        )

        t = f'{time.time():.3f}'.replace('.', '')

        return self.client.post(url=url + f'&t{t}', json=payload).json()

    @property
    def msid(self):
        return self.client.cookies.get(
            name='msid',
            domain='.kingdoms.com',
        )

    @property
    def decoded_session(self):
        encoded_session = self.client.cookies.get(
            name='t5SessionKey',
            domain=self.gameworld_api[8:-5],
        )
        return json.loads(urllib.parse.unquote(encoded_session))

    @property
    def player_id(self):
        return self.decoded_session['id']

    @property
    def session(self):
        return self.decoded_session['key']
