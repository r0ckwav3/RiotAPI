from RiotAPI import *
import json

# print(getPlayerNames(getMatch(getMatches(myid)[0]["gameId"])))
playerWins = {}
playerGames = {}
gamecutoff = 5 # change this to 5 or 10 for the real thing

player = "rockwave22"

f = open("StoredData/%sMatchData.txt" % player)
targetid = getAccountID(player)

for line in f:
    match = json.loads(line.strip())
    # TODO: make sure this is a regular match
    myParticipantID = getParticipantIndex(match, targetid)
    myTeam = match["participants"][myParticipantID]["teamId"]
    didIwin = match["participants"][myParticipantID]["stats"]["win"]
    for i in range(10):
        if match["participants"][i]["teamId"] == myTeam: # will count me, so keep an eye out for that
            teammatename = match["participantIdentities"][i]["player"]["summonerName"]
            playerGames[teammatename] = playerGames.get(teammatename,0)+1
            if didIwin:
                playerWins[teammatename] = playerWins.get(teammatename,0)+1

f.close()

tosort = []
for p in playerGames.keys():
    if playerGames[p]>gamecutoff:
        tosort.append((playerGames[p],p,playerWins.get(p,0)/playerGames[p]))
tosort.sort()
for item in tosort:
    print(item)
