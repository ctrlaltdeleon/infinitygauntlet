# @author       acfromspace
# @filename     riot-api-playground.py
# @description  Riot Games API playground.
# @notes        Riot Games API Reference: https://developer.riotgames.com/api-methods/
# @todo         Consider separating main() into more functions, considering if the player plays ranked.
#               Works on laptop, not on desktop, most likely due to specific Python linkage.

# "requests" library installed using "pip".
import requests


def request_summoner_v4(region, summoner_name, api_key):
    # SUMMONER-v4.
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + \
        summoner_name + "?api_key=" + api_key
    # Goes to the URL and retrieves the .json file.
    response = requests.get(URL)
    return response.json()


def request_league_v4(region, ID, api_key):
    # LEAGUE-v4.
    URL = "https://" + region + ".api.riotgames.com/lol/league/v4/positions/by-summoner/" + \
        ID + "?api_key=" + api_key
    # Goes to the URL and retrieves the .json file.
    response = requests.get(URL)
    return response.json()


def main():
    print("*************************")
    print("Riot Games API Playground")
    print("*************************\n")
    # Ask the user for 3 things, their region, summoner name, and API Key.
    region = input('Choose a region (Type "na1" for North America): ')
    summoner_name = input("Summoner name (Must be ranked): ")
    api_key = input('Copy and paste your API Key here: ')

    payload_summoner_v4 = request_summoner_v4(region, summoner_name, api_key)
    encrypted_summoner_id = str(payload_summoner_v4["id"])
    payload_league_v4 = request_league_v4(
        region, encrypted_summoner_id, api_key)

    print("\n*************************")
    print("Conclusion Stats")
    print("*************************\n")
    print("Name: " + str(payload_summoner_v4["name"]))
    print("Level: " + str(payload_summoner_v4["summonerLevel"]))
    print("League Name: " + str(payload_league_v4[0]["leagueName"]))
    print("Tier: " + str(payload_league_v4[0]["tier"]))
    print("Ranked Wins: " + str(payload_league_v4[0]["wins"]))
    print("Ranked Losses: " + str(payload_league_v4[0]["losses"]))
    print("League Points: " + str(payload_league_v4[0]["leaguePoints"]))


if __name__ == "__main__":
    main()
