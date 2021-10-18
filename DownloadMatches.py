from RiotAPI import *
import time
playername = input("what player: ")
chosenid = getAccountID(playername)
path = "StoredData/%sMatchData.txt" % playername
f = open(path, mode="w")

# Get the total number of games this player has played.
tempresponse = gethtml("https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/%s?endIndex=0&beginIndex=0&api_key=%s" % (chosenid, KEY))
totalGames = json.loads(tempresponse)["totalGames"]
print("This player has played "+str(totalGames)+" games total.")

# matches = getMatchIDs(chosenid)
ranges = [(i*50, (i+1)*50) for i in range(totalGames//50)]
# if totalGames is a multiple of 50, this will be length 0, which is fine
ranges.append(((totalGames//50)*50, totalGames))

for beginIndex, endIndex in ranges:
    time.sleep(120)
    matches = json.loads(gethtml("https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/%s?endIndex=%s&beginIndex=%s&api_key=%s" % (chosenid, str(endIndex), str(beginIndex), KEY)))["matches"]
    for j in range(len(matches)):
        print(j+beginIndex)
        url = "https://na1.api.riotgames.com/lol/match/v4/matches/%s?api_key=%s" % (matches[j]["gameId"], KEY)
        matchdata = gethtml(url)
        f.write(matchdata+"\n")

f.close()
