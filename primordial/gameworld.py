import json
import time
from urllib import parse
from .controllers.gameworld import (
    player, farmList, logger, troops, village, cache, quest, error, auctions, hero, building,
    trade, ranking, kingdom, map, reports, society, premiumFeature, payment, kingdomTreaty, login
)


class Gameworld():
    api_root = 'https://%s.kingdoms.com/api/?'

    def __init__(self, client, msid):
        self.client = client
        self.msid = msid
        self.session_key = ''
        self.api_root = ''  # Will vary based on gameworld name

        # Controllers
        self.player = player.Player(post_handler=self.post)
        self.farmList = farmList.FarmList(post_handler=self.post)
        self.logger = logger.Logger(post_handler=self.post)
        self.troops = troops.Troops(post_handler=self.post)
        self.village = village.Village(post_handler=self.post)
        self.cache = cache.Cache(post_handler=self.post)
        self.quest = quest.Quest(post_handler=self.post)
        self.error = error.Error(post_handler=self.post)
        self.auctions = auctions.Auctions(post_handler=self.post)
        self.hero = hero.Hero(post_handler=self.post)
        self.building = building.Building(post_handler=self.post)
        self.trade = trade.Trade(post_handler=self.post)
        self.ranking = ranking.Ranking(post_handler=self.post)
        self.kingdom = kingdom.Kingdom(post_handler=self.post)
        self.map = map.Map(post_handler=self.post)
        self.reports = reports.Reports(post_handler=self.post)
        self.society = society.Society(post_handler=self.post)
        self.premiumFeature = premiumFeature.PremiumFeature(post_handler=self.post)
        self.payment = payment.Payment(post_handler=self.post)
        self.kingdomTreaty = kingdomTreaty.KingdomTreaty(post_handler=self.post)
        self.login = login.Login(post_handler=self.post)

    def is_authenticated(self):
        """ Checks whether user is authenticated with the gameworld """

        if 'error' in self.payment.getPaymentShopUrl():
            return False
        else:
            return True

    def authenticate(self, gameworld_id, gameworld_name):
        """ Authenticates with the gameworld """

        mellon_root_url = 'https://mellon-t5.traviangames.com'

        # STEP 1
        response = self.client.get(
            f'{mellon_root_url}/game-world/join/gameWorldId/{gameworld_id}?msid={self.msid}&msname=msid')
        # Fish out 32 char long token
        token = response.text[response.text.find('token=')+6: response.text.find('token=')+38]

        # STEP 3
        response = self.client.get(
            f'https://{gameworld_name.lower()}.kingdoms.com/api/login.php?token={token}&msid={self.msid}&msname=msid')

        encoded_session_key = self.client.session.cookies.get('t5SessionKey', domain=f'{gameworld_name}.kingdoms.com')
        decoded_session_key = parse.unquote(encoded_session_key)
        self.session_key = json.loads(decoded_session_key)['key']

        self.api_root = Gameworld.api_root % gameworld_name.lower()

    def post(self, controller, action, params={}):
        payload = {
            'action': action,
            'controller': controller,
            'params': params,
            'session': self.session_key
            }

        # Create non-float timestamp like 154526134228
        timestamp = int('{:.2f}'.format(time.time()).replace('.', ''))
        url = f'{self.api_root}c={controller}&a={action}&t{timestamp}'

        response = self.client.post(url=url, data=json.dumps(payload))
        return response.json()
