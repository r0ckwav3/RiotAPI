## R0ckwav3's Python Riot API thing

You need a file called 'APIkey.txt' containing your API key for anything to work.

The most important files are:
* `RiotAPI.py`
    *  This includes all the QOL functions I coded up so that you don't need to manually touch anything like urllib or the API calls to get a player's ID.
* `DownloadMatches.py`
    *  This downloads all of a player's matches to a local file so that they are easier to work with. This takes a while, but circumvents the low amount of API calls that you can get on a test key.
