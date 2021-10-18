import urllib.request
import json

with open("APIkey.txt") as Keyfile:
    KEY = Keyfile.readline().strip()


def exploreDict(d):
    history = [d]
    flag = True
    while flag:
        if type(d) == list:
            print("There are %d entries in this list." % len(d))
            next = input("which element would you like to view: ")
            if next == "..":
                d = history.pop()
            else:
                history.append(d)
                d = d[int(next)]
        elif type(d) == dict:
            print("The keys to this dict are: " + ", ".join(d.keys()) + ".")
            next = input("which element would you like to view: ")
            if next == "..":
                d = history.pop()
            else:
                history.append(d)
                d = d[next]
        else:
            print(d)
            if input("quit? (y/n)") != "n":
                flag = False
            else:
                d = history.pop()


def gethtml(url, attempts=5):
    fp = None
    for j in range(attempts):
        try:
            fp = urllib.request.urlopen(url)
            break
        except Exception as e:
            print("Exception in gethtml:", e)

    if fp is None:
        print("Error when requesting URL:", url)

    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()
    # print(mystr)

    return mystr


def getSummoner(name):
    url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/%s?api_key=%s" % (name, KEY)
    return json.loads(gethtml(url))


def getAccountID(name):
    return getSummoner(name)["accountId"]


def getPUUID(name):
    return getSummoner(name)["puuid"]


def getMatchIDs(PUUID, start=0, count=20):  # 0 is the most recent
    url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/%s/ids?start=%s&count=%s&api_key=%s" % (PUUID, str(start), str(count), KEY)
    temp = json.loads(gethtml(url))
    return temp


def getMatch(MatchID):
    url = "https://americas.api.riotgames.com/lol/match/v5/matches/%s?api_key=%s" % (MatchID, KEY)
    return json.loads(gethtml(url))


def getPlayerNames(Match):
    participants = Match["info"]["participants"]
    names = [el["summonerName"] for el in participants]
    return names


def getParticipantIndex(Match, PUUID):
    print(Match["metadata"]["matchId"], len(Match["info"]["participants"]))
    playerindex = None
    for p in range(len(Match["info"]["participants"])):
        if Match["info"]["participants"][p]["puuid"] == PUUID:
            playerindex = p
    # print(playerindex,Match["participantIdentities"][playerindex]["player"]["summonerName"])
    if playerindex is None:
        print("player %s not in match" % PUUID)
        return -1
    else:
        return playerindex


def playerWin(Match, PUUID):
    return Match["info"]["participants"][getParticipantIndex(Match, PUUID)]["win"]
