# @author       acfromspace
# @filename     riot-api-playground.py
# @description  Riot Games API playground
# @notes        Riot Games API Reference: https://developer.riotgames.com/api-methods/
# @todo         Consider separating main() into more functions, considering if the player plays ranked
#               Works on laptop, not on desktop, most likely due to specific Python linkage

# "requests" library installed using "pip"
import requests


def requestSummonerV4(region, summonerName, APIKey):
    # SUMMONER-V4
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + \
        summonerName + "?api_key=" + APIKey
    # Goes to the URL and retrieves the .json file
    response = requests.get(URL)

    return response.json()


def requestLeagueV4(region, ID, APIKey):
    # LEAGUE-V4
    URL = "https://" + region + ".api.riotgames.com/lol/league/v4/positions/by-summoner/" + \
        ID + "?api_key=" + APIKey
    # Goes to the URL and retrieves the .json file
    response = requests.get(URL)

    return response.json()


def main():
    print("*************************")
    print("Riot Games API Playground")
    print("*************************\n")

    # Ask the user for 3 things, their region, summoner name, and API Key.

    region = input('Choose a region (Type "na1" for North America): ')
    summonerName = input("Summoner name (Must be ranked): ")
    APIKey = input('Copy and paste your API Key here: ')

    # Run the function to
    summonerV4Payload = requestSummonerV4(region, summonerName, APIKey)
    encryptedSummonerID = str(summonerV4Payload["id"])
    leagueV4Payload = requestLeagueV4(region, encryptedSummonerID, APIKey)

    # Output
    print("\n*************************")
    print("Conclusion Stats")
    print("*************************\n")
    print("Name: " + str(summonerV4Payload["name"]))
    print("Level: " + str(summonerV4Payload["summonerLevel"]))
    print("League Name: " + str(leagueV4Payload[0]["leagueName"]))
    print("Tier: " + str(leagueV4Payload[0]["tier"]))
    print("Ranked Wins: " + str(leagueV4Payload[0]["wins"]))
    print("Ranked Losses: " + str(leagueV4Payload[0]["losses"]))
    print("League Points: " + str(leagueV4Payload[0]["leaguePoints"]))


if __name__ == "__main__":
    main()
