from RiotAPI import *
import json

# maximums and minimums of KDA
KDMax = 0
KDMaxID = []
KDMin = 0
KDMinID = []

player = "rockwave22"

f = open("StoredData/%sMatchData.txt" % player)
targetid = getPUUID(player)

for line in f:
    match = json.loads(line.strip())

    # urf and similar don't count
    if(match["info"]["gameMode"] == "CLASSIC"):
        targetindex = getParticipantIndex(match, targetid)
        kills = match["info"]["participants"][targetindex]["kills"]
        deaths = match["info"]["participants"][targetindex]["deaths"]
        assists = match["info"]["participants"][targetindex]["assists"]

        # I might tweak this to get a more intuitive "best" and "worst" game
        stat = kills-deaths

        if(stat > KDMax):
            KDMax = stat
            KDMaxID = []
        if(stat == KDMax):
            KDMaxID.append(match["metadata"]["matchId"])

        if(stat < KDMin):
            KDMin = stat
            KDMinID = []
        if(stat == KDMin):
            KDMinID.append(match["metadata"]["matchId"])

f.close()

print("Best stat:", KDMax, "in games", KDMaxID)
print(mobalyticsMatch(KDMaxID[0], player))
print("Worst stat:", KDMin, "in games", KDMinID)
print(mobalyticsMatch(KDMinID[0], player))
