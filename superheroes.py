import requests
from pprint import pprint

class Hero:
    def __init__(self, name):
        self.name = name
    
    def intelligence(self):
        url = f"https://superheroapi.com/api/2619421814940190/search/{str.lower(self.name)}"
        response = requests.get(url=url)
        intelligence = response.json()["results"][0]["powerstats"]["intelligence"]
        return intelligence
    def who_is_smarter(self, *heroes):
        hero_dict = {}
        hero_dict[self.name] = int(self.intelligence())
        for hero in heroes:
            if isinstance(hero, Hero): 
                hero_dict[hero.name] = int(hero.intelligence())
        return f"{max(hero_dict, key=hero_dict.get)} is the smartest!"

    
    

if __name__ == "__main__":
    hulk = Hero("Hulk")
    captain = Hero("Captain America")
    thanos = Hero("Thanos")

    print(hulk.who_is_smarter(captain, thanos))