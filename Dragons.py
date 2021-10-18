from RiotAPI import *
import json

# print(getPlayerNames(getMatch(getMatches(myid)[0]["gameId"])))
dragonkillwins = {i:0 for i in range(10)} # noone better kill 10 dragons
dragonkilllosses = {i:0 for i in range(10)}

player = "rockwave22"

f = open("StoredData/%sMatchData.txt" % player)
targetid = getAccountID(player)

for line in f:
    match = json.loads(line.strip())
    if match["gameMode"] == "CLASSIC": # because aram has no dragons
        for team in match["teams"]:
            if team["win"] == "Win":
                dragonkillwins[team["dragonKills"]] += 1
            else:
                dragonkilllosses[team["dragonKills"]] += 1

f.close()
for i in range(10):
    print("dragons: %d, wins: %d, losses: %d" % (i,dragonkillwins[i],dragonkilllosses[i]))
