import urllib.request
import json

with open("APIkey.txt") as Keyfile:
    KEY = Keyfile.readline().strip()
    print(KEY)


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
    print(url)
    for j in range(attempts):
        try:
            fp = urllib.request.urlopen(url)
            break
        except Exception as e:
            print("Exception in gethtml:", e)
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()
    # print(mystr)

    return mystr


def getSummoner(name):
    url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/%s?api_key=%s" % (name,KEY)
    return json.loads(gethtml(url))


def getAccountID(name):
    return getSummoner(name)["accountId"]


def getMatchIDs(AccountID): # 0 is the most recent
    url = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/%s?api_key=%s" % (AccountID,KEY)
    temp = json.loads(gethtml(url))
    return temp["matches"]


def getMatch(MatchID):
    url = "https://na1.api.riotgames.com/lol/match/v4/matches/%s?api_key=%s" % (MatchID,KEY)
    return json.loads(gethtml(url))


def getPlayerNames(Match):
    identities = Match["participantIdentities"]
    names = [el["player"]["summonerName"] for el in identities]
    return names


def getParticipantIndex(Match, AccountID):
    playerindex = None
    for p in range(10):
        if Match["participantIdentities"][p]["player"]["accountId"] == AccountID:
            playerindex = p
    # print(playerindex,Match["participantIdentities"][playerindex]["player"]["summonerName"])
    if playerindex is None:
        print("player %s not in match" % AccountID)
        return -1
    else:
        return playerindex


def playerWin(Match, AccountID):
    return Match["participants"][getParticipantIndex(Match, AccountID)]["stats"]["win"]


# gethtml("https://www.google.com")

# exploreDict(getSummoner("Rockwave22"))
# myid = getAccountID("Rockwave22")
# print(getAccountID("bravewy"))
# myid = "k385ZSP0MGtPayTkIMk79H-UFqsS9nh9QaOBlzGb64IJNVYdLhmRukWO" # bravewy
# myid = "Kr0ydb0LN8UkJh1MAQn7lopUGPsBm942aIKGalFh0owNHDDKgG_lrVb-" # rockwave22
# print("id: " + myid)
# exploreDict(getMatch(getMatchIDs(myid)[0]["gameId"]))
# print(playerWin(getMatch(getMatchIDs(myid)[0]["gameId"]),myid))
