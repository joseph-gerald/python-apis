from bs4 import BeautifulSoup
import cf_proxy

class Game:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats

class Player:
    def __init__(self, html_content):
        self.soup = BeautifulSoup(html_content, 'html.parser')
        
        self.rank = None
        self.hours_played = None
        self.profile_picture_url = None
        self.games = []
        
        self.extract_data()
        
    def extract_data(self):
        rank_element = self.soup.find('p', class_='profile-rank')
        self.rank = rank_element.text.strip() if rank_element else None
        
        hours_played_element = self.soup.find('div', class_='profile-time').h1
        hours_played_text = hours_played_element.text.strip()
        self.hours_played = hours_played_text.split()[0] if hours_played_text else None
        
        profile_picture_element = self.soup.find('img', class_='avatar')
        self.profile_picture_url = profile_picture_element['src'] if profile_picture_element else None
        
        game_cards = self.soup.find_all('div', class_='profile-game-card')
        for game_card in game_cards:
            game_name = game_card.find('div', class_='title').h1.text.strip()
            game_stats_element = game_card.find('ul')
            game_stats_data = {}
            for li in game_stats_element.find_all('li'):
                key = li.find('div', class_='key').text.strip()
                val = li.find('div', class_='val').text.strip()
                game_stats_data[key] = val
            game = Game(game_name, game_stats_data)
            self.games.append(game)
    
    def display_data(self):
        print('Rank:', self.rank)
        print('Hours Played:', self.hours_played)
        print('Profile Picture URL:', self.profile_picture_url)
        print('Games:')
        for game in self.games:
            print('  Game:', game.name)
            print('  Stats:', game.stats)
            print('---')

class BlocksMC():
    def __init__(self, username, hash):
        self.username = username
        self.hash = hash

    def getPlayer(self, username):
        html = cf_proxy.get(f"https://blocksmc.com/player/{username}", headers={
            "Cookie": f"username6={self.username};usernamehash6={self.hash}"
        }).text

        return Player(html)