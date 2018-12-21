actions = {
    "player": {
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
    },
    "farmList": {
        "toggleEntry": {
            "params": {
                "villageId": 0,
                "listId": 0
            }
        },
        "getAttackInfo": {
            "params": {
                "currentVillageId": 0,
                "farmlistIds": [
                    0
                ]
            }
        },
        "editTroops": {
            "params": {
                "entryIds": [
                    0,
                    0
                ],
                "units": {
                    "1": 0,
                    "2": 0,
                    "3": 0,
                    "4": 0,
                    "5": 0,
                    "6": 0
                }
            }
        },
        "createList": {
            "params": {
                "name": ""
            }
        },
        "copyEntry": {
            "params": {
                "villageId": 0,
                "newListId": 0,
                "entryId": 0
            }
        },
        "deleteList": {
            "params": {
                "listId": 0
            }
        },
        "deleteEntry": {
            "params": {
                "entryId": 0
            }
        },
        "checkTarget": {
            "params": {
                "villageId": 0
            }
        },
        "addEntry": {
            "params": {
                "villageId": 0,
                "listId": 0
            }
        },
        "editList": {
            "params": {
                "name": "",
                "listId": 0
            }
        },
        "changeListOrder": {
            "params": {
                "listIds": [
                    0,
                    0
                ]
            }
        }
    },
    "logger": {
        "logMessage": {
            "params": {
                "message": "",
                "prefix": "",
                "logType": "",
                "details": ""
            }
        }
    },
    "troops": {
        "getMarkers": {
            "params": {}
        },
        "setMarker": {
            "params": {
                "troopId": 0,
                "marker": 0
            }
        },
        "abortTroopMovement": {
            "params": {
                "troopId": 0
            }
        },
        "checkTarget": {
            "params": {
                "destVillageName": "",
                "destVillageId": 0,
                "villageId": 0,
                "movementType": 0,
                "redeployHero": False,
                "heroPresent": False,
                "selectedUnits": {
                    "1": 0,
                    "2": 0,
                    "3": 0,
                    "4": 0,
                    "5": 0,
                    "6": 0,
                    "7": 0,
                    "8": 0,
                    "9": 0,
                    "10": 0,
                    "11": 0
                }
            }
        },
        "send": {
            "params": {
                "destVillageId": 0,
                "villageId": 0,
                "movementType": 0,
                "redeployHero": False,
                "units": {
                    "1": 0,
                    "2": 0,
                    "3": 0,
                    "4": 0,
                    "5": 0,
                    "6": 0,
                    "7": 0,
                    "8": 0,
                    "9": 0,
                    "10": 0,
                    "11": 0
                },
                "spyMission": ""
            }
        },
        "startPartialFarmListRaid": {
            "params": {
                "listId": 0,
                "entryIds": [
                    0,
                    0
                ],
                "villageId": 0
            }
        },
        "startFarmListRaid": {
            "params": {
                "listIds": [
                    0
                ],
                "villageId": 0
            }
        },
        "fightSimulate": {
            "params": {
                "attackType": 0,
                "attackerTribe": 0,
                "attackerUnits": {
                    "2": 0,
                    "4": 0,
                    "5": 0
                },
                "defenderTribe": [
                    0
                ],
                "defenderUnits": [
                    {
                        "1": 0,
                        "2": 0,
                        "3": 0,
                        "4": 0,
                        "5": 0,
                        "6": 0,
                        "7": 0,
                        "8": 0,
                        "9": 0,
                        "10": 0,
                        "11": 0
                    }
                ],
                "heroOffBonus": [
                    0,
                    0
                ],
                "heroDefBonus": [
                    0,
                    0
                ],
                "heroItemType": [
                    0,
                    0
                ],
                "heroFightStrength": [
                    0,
                    0
                ],
                "attackerResearch": {
                    "1": 0,
                    "2": 0,
                    "3": 0,
                    "4": 0,
                    "5": 0,
                    "6": 0,
                    "7": 0,
                    "8": 0,
                    "9": 0
                },
                "defenderResearch": [
                    {
                        "1": 0,
                        "2": 0,
                        "3": 0,
                        "4": 0,
                        "5": 0,
                        "6": 0,
                        "7": 0,
                        "8": 0,
                        "9": 0
                    }
                ],
                "attPopulation": 0,
                "defPopulation": 0,
                "catapultTargetLevel": 0,
                "catapultTargetLevel2": 0,
                "masonLevel": 0,
                "wallLevel": 0,
                "palaceLevel": 0,
                "moatLevel": 0,
                "natarBonus": 0,
                "heroMounted": [
                    0,
                    0
                ]
            }
        },
        "moveTroopsHome": {
            "params": {
                "troopId": 0,
                "units": {
                    "1": 0,
                    "2": 0,
                    "3": 0,
                    "4": 0,
                    "5": 0,
                    "6": 0,
                    "7": 0,
                    "8": 0,
                    "9": 0,
                    "10": 0,
                    "11": 0
                }
            }
        },
        "disband": {
            "params": {
                "troopId": 0
            }
        }
    },
    "village": {
        "clickSpecial": {
            "params": {
                "id": 0
            }
        },
        "toggleAllowTributeCollection": {
            "params": {
                "villageId": 0
            }
        },
        "getVillagesWithInfluenceOnOasisForPlayer": {
            "params": {
                "oasisId": 0,
                "playerId": 0
            }
        },
        "getKingdomVillageAttacks": {
            "params": {}
        },
        "getProductionDetails": {
            "params": {
                "villageId": 0
            }
        },
        "useOasis": {
            "params": {
                "oasisId": 0,
                "villageId": 0
            }
        },
        "clearOasis": {
            "params": {
                "oasisId": 0,
                "villageId": 0
            }
        },
        "updateName": {
            "params": {
                "villageId": 0,
                "villageName": ""
            }
        },
        "checkUnitProduction": {
            "params": {
                "villageId": 0
            }
        },
        "getTreasuriesCapacity": {
            "params": {
                "villageId": 0
            }
        },
        "getVictoryPointsAndInfluenceBonus": {
            "params": {
                "villageId": 0
            }
        }
    },
    "cache": {
        "get": {
            "params": {
                "names": [
                    ""
                ]
            }
        }
    },
    "quest": {
        "getPuzzle": {
            "params": {}
        },
        "solvePuzzle": {
            "params": {
                "moves": [
                    [],
                    [],
                    [],
                    [],
                    [],
                    [],
                    []
                ]
            }
        },
        "dialogAction": {
            "params": {
                "questId": 0,
                "dialogId": 0,
                "command": ""
            }
        },
        "checkRewardCollectible": {
            "params": {
                "questId": 0,
                "villageId": 0
            }
        },
        "collectReward": {
            "params": {
                "questId": 0,
                "villageId": 0
            }
        },
        "resetDailyQuest": {
            "params": {
                "questId": 0
            }
        }
    },
    "error": {
        "logJavascriptError": {
            "params": {
                "playerId": 0,
                "error": ""
            }
        }
    },
    "auctions": {
        "getRunningAuctionAmount": {
            "params": {
                "filterItemType": 0,
                "filterSlot": 0,
                "page": 0
            }
        },
        "getRunningAuctionPage": {
            "params": {
                "filterItemType": 0,
                "filterSlot": 0,
                "page": 0
            }
        },
        "placeBid": {
            "params": {
                "auctionId": 0,
                "bidAmount": 0
            }
        },
        "getSellerPayout": {
            "params": {
                "itemId": 0,
                "amount": 0
            }
        },
        "sellItem": {
            "params": {
                "itemId": 0,
                "amount": 0
            }
        }
    },
    "hero": {
        "getValuePoints": {
            "params": {}
        },
        "addAttributePoints": {
            "params": {
                "fightStrengthPoints": 0,
                "attBonusPoints": 0,
                "defBonusPoints": 0,
                "resBonusPoints": 0,
                "resBonusType": 0
            }
        },
        "mergeItem": {
            "params": {
                "id": 0,
                "amount": 0,
                "villageId": 0
            }
        },
        "saveFace": {
            "params": {
                "face": {
                    "mouth": 0,
                    "beard": 0,
                    "hair": 0,
                    "eye": 0,
                    "eyebrow": 0,
                    "ear": 0,
                    "nose": 0
                },
                "gender": 0,
                "hairColor": 0,
                "playerId": 0,
                "fetchedFromLobby": 0
            }
        },
        "getLastInventoryView": {
            "params": {}
        },
        "getTreasureSellPrice": {
            "params": {}
        },
        "getDurationToClosestVillageWithInfluence": {
            "params": {
                "villageId": 0
            }
        },
        "useItem": {
            "params": {
                "id": 0,
                "amount": 0,
                "villageId": 0
            }
        },
        "setLastInventoryView": {
            "params": {}
        },
        "getResourceForResourceChest": {
            "params": {
                "percent": 0,
                "type": 0
            }
        },
        "upgradeItem": {
            "params": {
                "upgradeItemId": 0,
                "targetItemId": 0
            }
        },
        "revive": {
            "params": {
                "villageId": 0
            }
        },
        "confirmHeroLevelUp": {
            "params": {}
        },
        "switchItems": {
            "params": {
                "id1": 0,
                "id2": 0
            }
        }
    },
    "building": {
        "getCelebrationList": {
            "params": {
                "villageId": 0,
                "locationId": 0
            }
        },
        "startCelebration": {
            "params": {
                "villageId": 0,
                "type": 0
            }
        },
        "getBuildingList": {
            "params": {
                "villageId": 0,
                "locationId": 0
            }
        },
        "getTrapperInfos": {
            "params": {
                "villageId": 0,
                "locationId": 0
            }
        },
        "buildTraps": {
            "params": {
                "villageId": 0,
                "locationId": 0,
                "amount": 0
            }
        },
        "upgrade": {
            "params": {
                "villageId": 0,
                "locationId": 0,
                "buildingType": 0
            }
        },
        "getRecruitList": {
            "params": {
                "villageId": 0,
                "locationId": 0
            }
        },
        "recruitUnits": {
            "params": {
                "villageId": 0,
                "locationId": 0,
                "units": {
                    "1": 0
                }
            }
        },
        "useMasterBuilder": {
            "params": {
                "villageId": 0,
                "locationId": 0,
                "buildingType": 0,
                "reserveResources": False
            }
        },
        "getOasisList": {
            "params": {
                "villageId": 0
            }
        },
        "getCulturePointBalance": {
            "params": {
                "villageId": 0
            }
        },
        "reserveResources": {
            "params": {
                "villageId": 0,
                "entryId": 0
            }
        },
        "cancel": {
            "params": {
                "villageId": 0,
                "eventId": 0
            }
        },
        "researchUnit": {
            "params": {
                "villageId": 0,
                "locationId": 0,
                "buildingType": 0,
                "unitType": 0
            }
        },
        "shiftMasterBuilder": {
            "params": {
                "villageId": 0,
                "from": 0,
                "to": 0
            }
        },
        "destroy": {
            "params": {
                "villageId": 0,
                "locationId": 0
            }
        },
        "getTreasuryTransformations": {
            "params": {}
        },
        "transformTreasury": {
            "params": {
                "villageId": 0,
                "locationId": 0
            }
        },
        "getCpData": {
            "params": {
                "villageId": 0
            }
        }
    },
    "trade": {
        "changeTradeRouteStatus": {
            "params": {
                "id": 0,
                "status": 0
            }
        },
        "deleteTradeRoute": {
            "params": {
                "id": 0
            }
        },
        "checkTarget": {
            "params": {
                "sourceVillageId": 0,
                "destVillageId": 0,
                "destVillageName": ""
            }
        },
        "createOffer": {
            "params": {
                "villageId": 0,
                "offeredResource": 0,
                "offeredAmount": 0,
                "searchedResource": 0,
                "searchedAmount": 0,
                "kingdomOnly": False
            }
        },
        "cancelOffer": {
            "params": {
                "offerId": 0
            }
        },
        "getOfferList": {
            "params": {
                "villageId": 0,
                "search": 0,
                "offer": 0,
                "rate": 0,
                "start": 0,
                "count": 0
            }
        },
        "acceptOffer": {
            "params": {
                "offerId": 0,
                "villageId": 0
            }
        }
    },
    "ranking": {
        "getKingdomVictoryPointsWithTreasures": {
            "params": {
                "start": 0,
                "end": 0
            }
        },
        "getKingdomStats": {
            "params": {
                "kingdomId": 0
            }
        },
        "getRanking": {
            "params": {
                "start": 0,
                "end": 0,
                "rankingType": "",
                "rankingSubtype": ""
            }
        },
        "getRankingAveragePoints": {
            "params": {
                "rankingType": "",
                "rankingSubType": ""
            }
        },
        "getRankAndCount": {
            "params": {
                "id": 0,
                "rankingType": "",
                "rankingSubtype": ""
            }
        },
        "getWorldStats": {
            "params": {}
        },
        "getKingdomInternalRanking": {
            "params": {}
        }
    },
    "kingdom": {
        "cancelGovernor": {
            "params": {
                "governorPlayerId": 0
            }
        },
        "acceptInvitation": {
            "params": {
                "id": 0
            }
        },
        "getTop3NearbyKings": {
            "params": {
                "villageId": 0
            }
        },
        "startCoronationCeremony": {
            "params": {
                "villageId": 0,
                "tag": ""
            }
        },
        "changeTag": {
            "params": {
                "tag": ""
            }
        },
        "promoteToDuke": {
            "params": {
                "playerId": 0,
                "customText": ""
            }
        },
        "changeDescription": {
            "params": {
                "groupId": 0,
                "publicDescription": ""
            }
        },
        "declineInvitation": {
            "params": {
                "id": 0
            }
        },
        "getFightStrengthRanks": {
            "params": {}
        },
        "getNews": {
            "params": {
                "start": 0,
                "count": 0
            }
        },
        "changeInternalDescription": {
            "params": {
                "groupId": 0,
                "internalDescription": ""
            }
        },
        "getDukeCandidate": {
            "params": {
                "kingdomId": 0
            }
        },
        "cancelKingdom": {
            "params": {}
        }
    },
    "map": {
        "getHeatmapMaximums": {
            "params": {}
        },
        "getByRegionIds": {
            "params": {
                "regionIdCollection": {
                    "1": [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0
                    ],
                    "2": [],
                    "3": [],
                    "4": [],
                    "5": [],
                    "6": []
                }
            }
        },
        "editMapMarkers": {
            "params": {
                "markers": [
                    {
                        "owner": 0,
                        "type": 0,
                        "color": 0,
                        "editType": 0,
                        "ownerId": 0,
                        "targetId": 0
                    }
                ],
                "fieldMessage": {
                    "text": "",
                    "type": 0,
                    "duration": 0,
                    "cellId": 0,
                    "targetId": 0
                }
            }
        },
        "fieldMarkerMinimize": {
            "params": {
                "cellId": 0,
                "isGlobal": 0,
                "minimizeState": 0
            }
        },
        "fieldMarkerClose": {
            "params": {
                "id": 0,
                "isGlobal": 0
            }
        },
        "fieldMarkerDelete": {
            "params": {
                "id": 0,
                "isGlobal": 0
            }
        },
        "getKingdomInfluenceStatistics": {
            "params": {
                "kingId": 0
            }
        }
    },
    "reports": {
        "getLastReports": {
            "params": {
                "collection": "",
                "start": 0,
                "count": 0,
                "filters": [],
                "alsoGetTotalNumber": False
            }
        },
        "getFullReport": {
            "params": {
                "id": "",
                "collection": "",
                "securityCode": ""
            }
        },
        "markAsFavorite": {
            "params": {
                "id": "",
                "collection": "",
                "securityCode": ""
            }
        },
        "shareReport": {
            "params": {
                "id": "",
                "shareWith": "",
                "shareParam": 0,
                "shareMessage": "",
                "collection": ""
            }
        },
        "removeAsFavorite": {
            "params": {
                "bodyId": ""
            }
        }
    },
    "society": {
        "getSharedInformations": {
            "params": {
                "villageId": 0
            }
        },
        "create": {
            "params": {
                "name": "",
                "attitude": 0,
                "target": 0,
                "targetId": 0,
                "sharedInformations": {
                    "reports": False,
                    "nextAttacks": False,
                    "villageDetails": False
                },
                "joinCondition": 0,
                "conditionValue": 0
            }
        },
        "invite": {
            "params": {
                "groupId": 0,
                "groupType": 0,
                "playerName": [
                    ""
                ],
                "customText": ""
            }
        },
        "declineInvitation": {
            "params": {
                "id": 0
            }
        },
        "changeDescription": {
            "params": {
                "groupId": 0,
                "description": 0
            }
        },
        "close": {
            "params": {
                "groupId": 0,
                "groupType": 0
            }
        }
    },
    "premiumFeature": {
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
    },
    "payment": {
        "getPaymentShopUrl": {
            "params": {
                "shopVersion": 0
            }
        },
        "getSmallestPackage": {
            "params": {
                "featurePrice": 0
            }
        }
    },
    "kingdomTreaty": {
        "offer": {
            "params": {
                "kingdomId": 0,
                "type": 0
            }
        },
        "deny": {
            "params": {
                "id": 0
            }
        },
        "cancel": {
            "params": {
                "id": 0
            }
        }
    },
    "login": {
        "logout": {
            "params": {}
        }
    }
}
