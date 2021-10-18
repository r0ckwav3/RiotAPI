from RiotAPI import *
import json

friends = ["SpoicyMemes","bravewy","Buotua"]

# print(getPlayerNames(getMatch(getMatches(myid)[0]["gameId"])))
playerWins = {}
playerGames = {}
f = open("StoredData/rockwave22MatchData.txt")

for line in f:
    match = json.loads(line.strip())
    # TODO: make sure this is a regular match
    myParticipantID = getParticipantIndex(match, myid)
    myTeam = match["participants"][myParticipantID]["teamId"]
    didIwin = match["participants"][myParticipantID]["stats"]["win"]
    friendsingame = []
    for i in range(10):
        if match["participants"][i]["teamId"] == myTeam: # will count me, so keep an eye out for that
            teammatename = match["participantIdentities"][i]["player"]["summonerName"]
            if teammatename in friends:
                friendsingame.append(teammatename)
    friendsingame = tuple(sorted(friendsingame))
    playerGames[friendsingame] = playerGames.get(friendsingame,0)+1
    if didIwin:
        playerWins[friendsingame] = playerWins.get(friendsingame,0)+1

f.close()

tosort = []
for p in playerGames.keys():
    tosort.append((playerGames[p],p,playerWins.get(p,0)/playerGames[p]))
tosort.sort()
for item in tosort:
    print(item)
