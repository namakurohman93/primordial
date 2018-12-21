from ..controller import Controller


class Player(Controller):
    def __init__(self, post_handler):
        actions = {
            "getAll": {
                "params": {
                    "deviceDimension": ""
                }
            },
            "getReferralDirection": {
                "params": {}
            },
            "chooseTribe": {
                "params": {
                    "tribeId": 0
                }
            },
            "checkKingRegistrationRule": {
                "params": {}
            },
            "getSystemMessage": {
                "params": {}
            },
            "getAchievementNotifications": {
                "params": {}
            },
            "changeTimeType": {
                "params": {
                    "timeType": 0
                }
            },
            "ping": {
                "params": {
                    "cnt": 0,
                    "lastGlobalMessageTime": 0.0,
                    "lastId": 0
                }
            },
            "deleteAllNotifications": {
                "params": {}
            },
            "getOpenChatWindows": {
                "params": {}
            },
            "deleteNotification": {
                "params": {
                    "type": 0
                }
            },
            "getCardgameResult": {
                "params": {}
            },
            "getMidnight": {
                "params": {}
            },
            "selectCards": {
                "params": {
                    "selectedCards": [
                        False,
                        False,
                        False,
                        False,
                        False
                    ]
                }
            },
            "getInvitationRefLink": {
                "params": {}
            },
            "getPlayerInfo": {
                "params": {
                    "playerId": 0
                }
            },
            "setOpenChatWindows": {
                "params": {
                    "windows": []
                }
            },
            "changeSettings": {
                "params": {
                    "newSettings": {
                        "premiumConfirmation": 0,
                        "lang": "",
                        "onlineStatusFilter": 0,
                        "extendedSimulator": False,
                        "musicVolume": 0,
                        "soundVolume": 0,
                        "uiSoundVolume": 0,
                        "muteAll": False,
                        "timeType": 0,
                        "timeZone": 0,
                        "timeZoneString": "",
                        "timeZoneSwitcher": 0,
                        "timeFormat": 0,
                        "attacksFilter": 0,
                        "mapFilter": 0,
                        "enableTabNotifications": False,
                        "disableAnimations": False,
                        "enableHelpNotifications": False,
                        "enableWelcomeScreen": False,
                        "notpadsVisible": False
                    }
                }
            },
            "addNote": {
                "params": {
                    "x": 0,
                    "y": 0
                }
            },
            "changeNote": {
                "params": {
                    "newSettings": {
                        "id": 0,
                        "positionX": 0,
                        "positionY": 0,
                        "sizeX": 0,
                        "sizeY": 0,
                        "text": ""
                    }
                }
            },
            "removeNote": {
                "params": {
                    "id": 0
                }
            },
            "getActivityStreams": {
                "params": {}
            },
            "getPrestigeConditions": {
                "params": {}
            },
            "getRobberVillagesAmount": {
                "params": {
                    "kingdomId": 0
                }
            },
            "resetActivityStream": {
                "params": {}
            },
            "triggerInGameHelpNotice": {
                "params": {
                    "helpType": ""
                }
            },
            "changeVacationState": {
                "params": {}
            },
            "requestVerification": {
                "params": {
                    "requestAction": 0,
                    "url": ""
                }
            },
            "verifyAction": {
                "params": {
                    "token": ""
                }
            },
            "abortDeletion": {
                "params": {}
            },
            "requestExternalLogin": {
                "params": {
                    "publicSiteKey": 0
                }
            },
            "updatePlayerProfileContent": {
                "params": {}
            },
            "editProfile": {
                "params": {
                    "description": 0
                }
            },
            "getInvitationsList": {
                "params": {}
            },
            "sendInvitation": {
                "params": {
                    "friendName": "",
                    "email": "",
                    "ownName": "",
                    "message": ""
                }
            },
            "reportConversation": {
                "params": {
                    "roomId": ""
                }
            },
            "reportConversationFinalize": {
                "params": {
                    "roomId": ""
                }
            },
            "getPlayerInfluence": {
                "params": {
                    "villageId": 0
                }
            },
            "inviteToKingdom": {
                "params": {
                    "villageId": 0
                }
            },
            "reportPlayer": {
                "params": {
                    "roomId": "",
                    "playerId": 0,
                    "reason": 0
                }
            }
        }

        Controller.__init__(self, post_handler=post_handler, controller='player', actions=actions)
