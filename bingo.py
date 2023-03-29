import numpy as np
import pandas as pd
import random
import time

class Bingo():
    def __init__(self):
        self.songs = ['42', '7-11', 'above the waves', 'abraxas', 'aceetobee', 'air song', 'and the ladies were the rest of the night', 'another plan of attack', 'anthem', 'aquatic ape', 'astronaut', 'astronomy domine', 'barfly', 'basis for a day', 'bazaar escape', 'bernstein and chasnoff', 'bombs', 'boom shanker', 'catalyst', 'caterpillar', 'caves of the east', 'chemical warfare brigade', 'clocks', 'commercial amen', 'confrontation', 'crickets', 'crystal ball', 'cyclone', 'dance of the sugar plum fairy', 'digital buddha', 'down to the bottom', 'eulogy', 'everybody needs somebody to love', 'evolve', 'feeling twisted', 'flash mob', 'floes', 'floodlights', 'freeze', 'frog legs', 'grass is green', 'haleakala crater', 'helicopters', 'high speed racer', 'highwire', 'home again', 'hope', 'hot air balloon', 'house dog party favor', "humuhumunukunukuapua'a", 'i remember when', 'i-man', 'jack straw', 'jamillia', 'jigsaw earth', 'kamaole sands', 'king of the world', 'kitchen mitts', 'knights of cydonia', 'konkrete', 'lake shore drive', 'liquid handcuffs', 'little betty boop', 'little lai', 'little shimmy in a conga line', 'loose change', 'lunar pursuit', 'm.e.m.p.h.i.s.', 'm1', 'm80', 'magellan', 'magellan reprise', 'meditation', 'mindless dribble', 'minions', 'miracles', 'mirrors', 'morph dusseldorf', 'moshi fameus', 'mr. don', "mulberry's dream", 'munchkin invasion', 'my lady survives', 'naeba', 'neck romancer', 'new song', 'news from nowhere', 'nughuffer', 'o fortuna', 'on time', 'onamae wa', 'once the fiddler paid', 'one chance to save the world', 'orch theme', 'papercut', 'park ave.', 'pat and dex', "pilin' it high", 'pimp blue rikkis', 'plan b', 'portal to an empty head', 'pygmy twylyte', 'radiator', 'rainbow song', 'resurrection', 'rivers', 'rock candy', 'rock your dance', 'rockafella', 'run like hell', 'running into the night', 'sabre dance', 'save the robots', 'shadow', "she's gone", 'shelby rose', 'shem-rah boo', 'shocked!', "sister judy's soul shack", 'songs of joy', 'sound one', 'space train', 'spacebirdmatingcall', 'spaga', "spaga's last stand", 'spectacle', 'spraypaint', 'spy', 'step inside', 'stone', 'story of the world', 'strobelights and martinis', 'svenghali', 'sweating bullets', 'tamarin alley', 'tempest', 'the big happy', 'the bridge', 'the champions', 'the city', 'the deal', "the devil's waltz", 'the great abyss', 'the overture', 'the safety dance', 'the thieving magpie', 'the truth', 'the tunnel', 'the very moon', 'the wormhole', 'therapy', 'three wishes', 'times square', 'to be continued', 'tourists (rocket ship)', 'tricycle', 'triumph', 'trooper mccue', "trucker's choice", 'twisted in the road', 'uber glue', 'vassillios', 'vibes', 'voices insane', 'we like to party', 'wet', "who's in charge?", 'why we dance', 'widgets', 'widow in the rain', 'wizards in winter', 'world is spinning', 'you and i']
        # pd.read_csv('./songs.csv')['0'].tolist()
        self.boards = {
            'player1':pd.DataFrame([
                ['tourists (rocket ship)', "spaga's last stand", 'why we dance', 'twisted in the road', 'another plan of attack'],
                ['anthem', 'spraypaint', 'jigsaw earth', 'kitchen mitts', 'the overture'],
                ['therapy', 'mindless dribble', 'times square', 'abraxas', '7-11'],
                ['crystal ball', 'litte lai', 'little betty boop', 'triumph', "mulberry's dream"],
                ['running into the night', 'shem-rah boo', 'voices insane', 'naeba', '42']
            ]),
            'player2':pd.DataFrame([
                ['shocked!', 'hot air balloon', 'spaga', "mulberry's dream", 'why we dance'],
                ['clocks', 'aceetobee', 'freeze', 'anthem', '42'],
                ['the wormhole', 'twisted in the road', "spaga's last stand", 'naeba', 'tourists (rocket ship)'],
                ['magellan', 'abraxas', "who's in charge?", 'little betty boop', 'miracles'],
                ['times square', 'lunar pursuit', 'therapy', 'shem-rah boo', 'spraypaint']
            ]),
        }
        self.winners = []
        self.rank = pd.DataFrame(columns=None)

    def next_song(self):
        song = random.choice(self.songs)
        self.songs.remove(song)
        return song
    
    def update_boards(self, song):
        for player in self.boards:
            if song in self.boards[player].values:
                self.boards[player] = self.boards[player].replace(song, 'X')

    def count_hits(self):
        for player in self.boards:
            board = self.boards[player]

            # Rows
            board_t = board.transpose()
            row_rank = []
            for row in board_t:
                row = board_t[row].tolist()
                row_rank.append(row)
            row_df = pd.DataFrame(row_rank)
            row_df['count'] = [i.count('X') for i in row_rank]
            row_df['player'] = player
            row_df = row_df.set_index('player')
            self.rank = pd.concat([self.rank, row_df])

            # Column
            col_rank = []
            for column in board:
                column = board[column].tolist()
                col_rank.append(column)
            col_df = pd.DataFrame(col_rank)
            col_df['count'] = [i.count('X') for i in col_rank]
            col_df['player'] = player
            col_df = col_df.set_index('player')
            self.rank = pd.concat([self.rank, col_df])

            # Diagonal 1
            dia1 = np.diagonal(board)
            dia1_df = pd.DataFrame(dia1)
            dia1_df['count'] = [i.count('X') for i in dia1]
            dia1_df['player'] = player
            dia1_df = dia1_df.set_index('player')
            self.rank = pd.concat([self.rank, dia1_df])

            # Diagonal 2
            dia2 = np.fliplr(board).diagonal()
            dia2_df = pd.DataFrame(dia2)
            dia2_df['count'] = [i.count('X') for i in dia2]
            dia2_df['player'] = player
            dia2_df = dia2_df.set_index('player')
            self.rank = pd.concat([self.rank, dia2_df])

        self.rank = self.rank.sort_values(by=['count', 'player'], ascending=False)
        print(self.rank[['count']].head(5))

    def check_winner(self):
        self.winners = self.rank[self.rank['count'] == 5].index.unique()            

def main():
    b = Bingo()

    while len(b.winners) == 0:
        song = b.next_song()
        print(song)
        b.update_boards(song)
        b.count_hits()
        b.check_winner()
        print()
        # time.sleep(.25)

    print('BINGO! The winner(s):', *b.winners.values)
    for winner in b.boards.keys():
        print(winner)
        print(b.boards[winner])
        print()

if __name__ == '__main__':
    main()
