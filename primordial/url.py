import enum


class URL(enum.Enum):
    MellonURL = 'https://mellon-t5.traviangames.com/'
    LobbyAPI = 'https://lobby.kingdoms.com/api/'
    GameworldAPI = 'https://{}.kingdoms.com/api/'

    @property
    def authentication_login(self):
        return f'{self.value}authentication/login'

    @property
    def login_ajax(self):
        return f'{self.authentication_login}/ajax/form-validate'

    @property
    def login(self):
        return f'{self.value}login.php'

    @property
    def index(self):
        return f'{self.value}index.php'

    @property
    def join_gameworld(self):
        return f'{self.value}game-world/join/gameWorldId/' + '{}'

    @property
    def join_as_guest(self):
        return f'{self.value}game-world/join-as-guest/avatarId/' + '{}'

    def __str__(self):
        return self.value
