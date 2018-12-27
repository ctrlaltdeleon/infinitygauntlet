# @author       acfromspace
# @filename     riot-api-playground.py
# @description  Riot Games API playground
# @notes        Riot Games API Reference: https://developer.riotgames.com/api-methods/

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
    URL = "https://" + region + "api.riotgames.com/lol/league/v4/positions/by-summoner/" + \
        ID + "/entry?api_key=" + APIKey
    # Goes to the URL and retrieves the .json file
    response = requests.get(URL)

    return response.json()


def main():
    print("*************************")
    print("Riot Games API Playground")
    print("*************************\n")

    # Ask the user for 3 things, their region, summoner name, and API Key.

    region = input('Choose a region (Type "na1" for North America): ')
    summonerName = input("Summoner name: ")
    APIKey = input('Copy and paste your API Key here: ')

    # Run the function to
    summonerV4Payload = requestSummonerV4(region, summonerName, APIKey)
    # ID = str(summonerV4Payload["id"])
    # leagueV4Payload = requestLeagueV4(region, ID, APIKey)

    # Output
    print("\n*************************")
    print("Conclusion")
    print("*************************\n")
    print("Name: " + str(summonerV4Payload["name"]))
    print("Level: " + str(summonerV4Payload["summonerLevel"]))
    # print(str(leagueV4Payload))


if __name__ == "__main__":
    main()
