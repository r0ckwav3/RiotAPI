from RiotAPI import *
import json

# print(getPlayerNames(getMatch(getMatches(myid)[0]["gameId"])))
lanewins = {}
lanelosses = {}

player = "spoicymemes"

f = open("StoredData/%sMatchData.txt" % player)
targetid = getAccountID(player)

for line in f:
    match = json.loads(line.strip())
    myParticipantID = getParticipantIndex(match, targetid)
    # myTeam = match["participants"][myParticipantID]["teamId"]
    didIwin = match["participants"][myParticipantID]["stats"]["win"]
    lane = match["participants"][myParticipantID]["timeline"]["lane"]
    if lane not in lanewins:
        lanewins[lane] = 0
        lanelosses[lane] = 0
    if didIwin:
        lanewins[lane]+=1
    else:
        lanelosses[lane]+=1

f.close()

for key in lanewins:
    print(key,lanewins[key],lanelosses[key])
