# primordial

Travian 5 API Client Framework

## Table of Contents

* [Installation](#Installation)
	* [Building from zip](#Building-from-zip)
* [Usage](#Usage)
	* [Import](#Import)
	* [Create a lobby object](#Create-a-lobby-object)
	* [Authenticate](#Authenticate)
	* [Connect to a gameworld](#Connect-to-a-gameworld)
	* [Explore](#Explore)
* [Controllers](#Controllers)
	* [Lobby Controllers](#Lobby-Controllers)
	* [Gameworld Controllers](#Gameworld-Controllers)
* [Developer Notes](#Developer-Notes)
	* [Missing Controllers](#Missing-Controllers)
	* [Missing Actions](#Missing-Actions)
	* [Param Types](#Param-Types)
	* [Cache Controller](#Cache-Controller)


## Installation

### Building from zip
```sh
python setup.py sdist --formats=zip
cd dist
pip install primordial-x.x.x.zip
```

## Usage

### Import
```py
from primordial.lobby import Lobby
```

### Create a lobby object
> **Note:** For a guide on how to use proxies see http://docs.python-requests.org/en/master/user/advanced/#proxies

```py
lobby = Lobby(proxies={})
```

### Authenticate
```py
lobby.authenticate(email=' ', password=' ')
```

### Connect to a gameworld
```py
gameworld = lobby.connect_to_gameworld(gameworld_id=0, gameworld_name=' ')
```

### Explore
> **Note:** For a complete list of controllers and their actions, see the Table of Contents

```py
dir(gameworld.building)
gameworld.building.upgrade.params
response = gameworld.building.upgrade(params={'villageId': 0, 'locationId': 0, 'buildingType': 0})
```
```py
dir(gameworld.reports)
gameworld.reports.getLastReports.params
response = gameworld.reports.getLastReports(params={'collection': ' ', 'start': 0, 'count': 0, 'filter': [], 'alsoGetTotalNumber': False})
```



# Controllers

## Lobby Controllers

|Controller    |Actions                                 |
|--------------|----------------------------------------|
|login         |logout                                  |
|cache         |get                                     |
|player        |abortDeletion                           |
|              |switchCountry                           |
|              |saveName                                |
|              |getAll                                  |
|              |getAvatarData                           |
|              |getPrestigeOnWorlds                     |
|              |getAccountDetails                       |
|              |deleteAvatar                            |
|gameworld     |getPossibleNewGameworlds                |
|sitter        |remove                                  |
|              |add                                     |
|              |setPermissions                          |
|dual          |add                                     |
|notification  |markAsRead                              |
|achievements  |update                                  |


## Gameworld Controllers

|Controller    |Actions                                 |
|--------------|----------------------------------------|
|player        |reportPlayer                            |
|              |getAll                                  |
|              |getReferralDirection                    |
|              |chooseTribe                             |
|              |checkKingRegistrationRule               |
|              |getSystemMessage                        |
|              |getAchievementNotifications             |
|              |changeTimeType                          |
|              |ping                                    |
|              |deleteAllNotifications                  |
|              |getOpenChatWindows                      |
|              |deleteNotification                      |
|              |getCardgameResult                       |
|              |getMidnight                             |
|              |selectCards                             |
|              |getInvitationRefLink                    |
|              |getPlayerInfo                           |
|              |setOpenChatWindows                      |
|              |changeSettings                          |
|              |addNote                                 |
|              |changeNote                              |
|              |removeNote                              |
|              |getActivityStreams                      |
|              |getPrestigeConditions                   |
|              |getRobberVillagesAmount                 |
|              |resetActivityStream                     |
|              |triggerInGameHelpNotice                 |
|              |changeVacationState                     |
|              |requestVerification                     |
|              |verifyAction                            |
|              |abortDeletion                           |
|              |requestExternalLogin                    |
|              |updatePlayerProfileContent              |
|              |editProfile                             |
|              |getInvitationsList                      |
|              |sendInvitation                          |
|              |reportConversation                      |
|              |reportConversationFinalize              |
|              |getPlayerInfluence                      |
|              |inviteToKingdom                         |
|farmList      |changeListOrder                         |
|              |toggleEntry                             |
|              |getAttackInfo                           |
|              |editTroops                              |
|              |createList                              |
|              |copyEntry                               |
|              |deleteList                              |
|              |deleteEntry                             |
|              |checkTarget                             |
|              |addEntry                                |
|              |editList                                |
|logger        |logMessage                              |
|troops        |disband                                 |
|              |getMarkers                              |
|              |setMarker                               |
|              |abortTroopMovement                      |
|              |checkTarget                             |
|              |send                                    |
|              |startPartialFarmListRaid                |
|              |startFarmListRaid                       |
|              |fightSimulate                           |
|              |moveTroopsHome                          |
|village       |getVictoryPointsAndInfluenceBonus       |
|              |clickSpecial                            |
|              |toggleAllowTributeCollection            |
|              |getVillagesWithInfluenceOnOasisForPlayer|
|              |getKingdomVillageAttacks                |
|              |getProductionDetails                    |
|              |useOasis                                |
|              |clearOasis                              |
|              |updateName                              |
|              |checkUnitProduction                     |
|              |getTreasuriesCapacity                   |
|cache         |get                                     |
|quest         |resetDailyQuest                         |
|              |getPuzzle                               |
|              |solvePuzzle                             |
|              |dialogAction                            |
|              |checkRewardCollectible                  |
|              |collectReward                           |
|error         |logJavascriptError                      |
|auctions      |sellItem                                |
|              |getRunningAuctionAmount                 |
|              |getRunningAuctionPage                   |
|              |placeBid                                |
|              |getSellerPayout                         |
|hero          |switchItems                             |
|              |getValuePoints                          |
|              |addAttributePoints                      |
|              |mergeItem                               |
|              |saveFace                                |
|              |getLastInventoryView                    |
|              |getTreasureSellPrice                    |
|              |getDurationToClosestVillageWithInfluence|
|              |useItem                                 |
|              |setLastInventoryView                    |
|              |getResourceForResourceChest             |
|              |upgradeItem                             |
|              |revive                                  |
|              |confirmHeroLevelUp                      |
|building      |getCpData                               |
|              |getCelebrationList                      |
|              |startCelebration                        |
|              |getBuildingList                         |
|              |getTrapperInfos                         |
|              |buildTraps                              |
|              |upgrade                                 |
|              |getRecruitList                          |
|              |recruitUnits                            |
|              |useMasterBuilder                        |
|              |getOasisList                            |
|              |getCulturePointBalance                  |
|              |reserveResources                        |
|              |cancel                                  |
|              |researchUnit                            |
|              |shiftMasterBuilder                      |
|              |destroy                                 |
|              |getTreasuryTransformations              |
|              |transformTreasury                       |
|trade         |acceptOffer                             |
|              |changeTradeRouteStatus                  |
|              |deleteTradeRoute                        |
|              |checkTarget                             |
|              |createOffer                             |
|              |cancelOffer                             |
|              |getOfferList                            |
|ranking       |getKingdomInternalRanking               |
|              |getKingdomVictoryPointsWithTreasures    |
|              |getKingdomStats                         |
|              |getRanking                              |
|              |getRankingAveragePoints                 |
|              |getRankAndCount                         |
|              |getWorldStats                           |
|kingdom       |cancelKingdom                           |
|              |cancelGovernor                          |
|              |acceptInvitation                        |
|              |getTop3NearbyKings                      |
|              |startCoronationCeremony                 |
|              |changeTag                               |
|              |promoteToDuke                           |
|              |changeDescription                       |
|              |declineInvitation                       |
|              |getFightStrengthRanks                   |
|              |getNews                                 |
|              |changeInternalDescription               |
|              |getDukeCandidate                        |
|map           |getKingdomInfluenceStatistics           |
|              |getHeatmapMaximums                      |
|              |getByRegionIds                          |
|              |editMapMarkers                          |
|              |fieldMarkerMinimize                     |
|              |fieldMarkerClose                        |
|              |fieldMarkerDelete                       |
|reports       |removeAsFavorite                        |
|              |getLastReports                          |
|              |getFullReport                           |
|              |markAsFavorite                          |
|              |shareReport                             |
|society       |close                                   |
|              |getSharedInformations                   |
|              |create                                  |
|              |invite                                  |
|              |declineInvitation                       |
|              |changeDescription                       |
|premiumFeature|cropProductionBonus                     |
|              |saveAutoExtendFlags                     |
|              |treasureResourcesInstant                |
|              |cardgameSingle                          |
|              |cardgame4of5                            |
|              |starterPackage                          |
|              |buildingMasterSlot                      |
|              |exchangeOffice                          |
|              |NPCTrader                               |
|              |finishNow                               |
|              |plusAccount                             |
|              |productionBonus                         |
|payment       |getSmallestPackage                      |
|              |getPaymentShopUrl                       |
|kingdomTreaty |cancel                                  |
|              |offer                                   |
|              |deny                                    |
|login         |logout                                  |


# Developer Notes

## Missing Controllers
> There are 3 controllers that have not yet been implemented
> * cheat
> * cheatsheat
> * adb
>
> These do not contain any actions that can be used by a non MH client

## Missing Actions
> Some controllers are missing some actions
>
> Please see dev/README.md

## Param Types

> Each action contains a dict of params
>
> Each param has been set to a default for the respective type, i.e int=0, bool=False
>
> Ensure that the param types of your queries match those types
>
> Majority of params of type dict or list can have an arbitrary amount of nested params

## Cache Controller

> The cache controller contains only one action: get
>
> The sole param of get is 'names' of type list
>
> The 'names' list may contain an arbitrary amount of values
>
> A list of unique possible values for the 'names' param can be found in dev/cache_params.py
>
> Please note that where a value contains an int, it should be treated as an id and replaced where relevant
