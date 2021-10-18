from RiotAPI import *
import time
playername = input("what player: ")
chosenid = getPUUID(playername)
path = "StoredData/%sMatchData.txt" % playername
f = open(path, mode="w")

# As far as I can tell, there's no equivalet way to get the number of matches
# in match-v5, but here's the old v4 code that would do that
# tempresponse = gethtml("https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/%s?endIndex=0&beginIndex=0&api_key=%s" % (chosenid, KEY))
# totalGames = json.loads(tempresponse)["totalGames"]
# print("This player has played "+str(totalGames)+" games total.")

matchchunksize = 64
currentmatch = 0

while matchchunksize != 0:
    time.sleep(120)
    try:
        matches = getMatchIDs(chosenid, start=currentmatch, count=matchchunksize)
    except Exception as e:
        matchchunksize = matchchunksize//2
        print("getMatchIDs failed, decreasing chunk size to", matchchunksize)
    else:
        for j in range(len(matches)):
            print(j+currentmatch)
            url = "https://americas.api.riotgames.com/lol/match/v5/matches/%s?api_key=%s" % (matches[j], KEY)
            try:
                matchdata = gethtml(url)
            except Exception as e:
                pass
            else:
                f.write(matchdata+"\n")
        currentmatch += matchchunksize

f.close()
