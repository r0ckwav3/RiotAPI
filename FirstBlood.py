from RiotAPI import *
import json

# print(getPlayerNames(getMatch(getMatches(myid)[0]["gameId"])))
fbwins = 0
fblosses = 0

player = "rockwave22"

f = open("StoredData/%sMatchData.txt" % player)

for line in f:
    match = json.loads(line.strip())

    for player in match["info"]["participants"]:
        if player["firstBloodKill"]:
            if player["win"]:
                fbwins += 1
            else:
                fblosses += 1

f.close()

print("fbwins: %d, fblosses: %d" % (fbwins, fblosses))
