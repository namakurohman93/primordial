actions = {
    "login": {
        "logout": {
            "params": {}
        }
    },
    "cache": {
        "get": {
            "params": {
                "names": [
                    "",
                    "",
                    "",
                    "",
                    ""
                ]
            }
        }
    },
    "player": {
        "switchCountry": {
            "params": {
                "country": ""
            }
        },
        "saveName": {
            "params": {
                "accountName": ""
            }
        },
        "getAll": {
            "params": {}
        },
        "getAvatarData": {
            "params": {}
        },
        "getPrestigeOnWorlds": {
            "params": {
                "type": ""
            }
        },
        "getAccountDetails": {
            "params": {}
        },
        "deleteAvatar": {
            "params": {
                "avatarIdentifier": 0
            }
        },
        "abortDeletion": {
            "params": {
                "avatarIdentifier": 0
            }
        }
    },
    "gameworld": {
        "getPossibleNewGameworlds": {
            "params": {}
        }
    },
    "sitter": {
        "add": {
            "params": {
                "avatarIdentifier": 0,
                "consumersId": "",
                "avatarName": "",
                "email": ""
            }
        },
        "setPermissions": {
            "params": {
                "avatarIdentifier": 0,
                "sitterAccountIdentifier": 0,
                "permissions": {
                    "1": False,
                    "2": False,
                    "3": False,
                    "4": False
                }
            }
        },
        "remove": {
            "params": {
                "avatarIdentifier": 0,
                "sitterAccountIdentifier": 0
            }
        }
    },
    "dual": {
        "add": {
            "params": {
                "avatarIdentifier": 0,
                "consumersId": "",
                "avatarName": "",
                "email": ""
            }
        }
    },
    "notification": {
        "markAsRead": {
            "params": {
                "id": 0
            }
        }
    },
    "achievements": {
        "update": {
            "params": {}
        }
    }
}
