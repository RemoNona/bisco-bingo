import numpy as np
import pandas as pd
import streamlit as st
import random
import time

st.title('Bisco Bingo')

class Bingo():
    def __init__(self):
        self.songs = [' ', '7-11'] + pd.read_csv('./songs_full.csv')['0'].tolist()
        self.boards = {
            'Jeremy':pd.DataFrame([
                ['tourists (rocket ship)', "spaga's last stand", 'why we dance', 'twisted in the road', 'another plan of attack'],
                ['anthem', 'spraypaint', 'jigsaw earth', 'kitchen mitts', 'the overture'],
                ['therapy', 'mindless dribble', 'times square', 'abraxas', '7-11'],
                ['crystal ball', 'litte lai', 'little betty boop', 'triumph', "mulberry's dream"],
                ['running into the night', 'shem-rah boo', 'voices isongane', 'naeba', '42']
            ]),
            'player2':pd.DataFrame([
                ['shocked!', 'hot air balloon', 'spaga', "mulberry's dream", 'why we dance'],
                ['clocks', 'aceetobee', 'freeze', 'anthem', '42'],
                ['the wormhole', 'twisted in the road', "spaga's last stand", 'naeba', 'tourists (rocket ship)'],
                ['magellan', 'abraxas', "who's in charge?", 'little betty boop', 'miracles'],
                ['times square', 'lunar pursuit', 'therapy', 'shem-rah boo', 'spraypaint']
            ]),
            'player3':pd.DataFrame([
                ['pygmy twylyte', 'resurrection', 'tourists (rocket ship)', 'jigsaw earth', 'hope'],
                ['abraxas', 'the overture', 'i-man', 'helicopters', 'minions'],
                ['liquid handcuffs', 'running into the night', 'spraypaint', 'bazaar escape', 'anthem'],
                ['triumph', 'down to the bottom', 'shem-rah boo', 'strobelights and martinis', 'crystal ball'],
                ['highwire', 'mindless dribble', 'm1', 'catalyst', '7-11'],
            ]),
            'Jon':pd.DataFrame([
                ['little lai', 'running into the night', 'the great abyss', 'house dog party favor', 'voices insane'],
                ['uber glue', 'tourists (rocket ship)', '42', 'm1', 'home again'],
                ["mulberry's dream", 'catalyst', 'crystal ball', 'times square', 'twisted in the road'],
                ['sound one', 'morph dusseldorf', 'another plan of attack', 'lunar pursuit', 'chemical warfare brigade'],
                ['shem-rah boo', 'the very moon', 'helicopters', 'naeba', 'spraypaint']
            ]),
            'Evan':pd.DataFrame([
                ['evolve', 'mr. don', "humuhumunukunukuapua'a", 'little lai', "who's in charge?"],
                ['mindless dribble', 'aceetobee', 'jigsaw earth', 'spaga', 'crickets'],
                ["mulberry's dream", 'another plan of attack', 'helicopters', '42', 'run like hell'],
                ['the overture', '7-11', 'confrontation', 'house dog party favor', 'space train'],
                ['tourists (rocket ship)', 'once the fiddler paid', 'little betty boop', 'hope', 'twisted in the road']
            ]),
            'Tomer':pd.DataFrame([
                ['another plan of attack', 'rocket science', 'freeze', 'anthem', 'plan b'],
                ['m1', 'feeling twisted', 'morph dusseldorf', 'tourists (rocket ship)', 'uber glue'],
                ['vassillios', '42', 'strobelights and martinis', 'spaga', 'magellan'],
                ['hot air balloon', 'clocks', 'little shimmy in a conga line', 'twisted in the road', 'evolve'],
                ['why we dance', 'freebis slinky', 'monster', 'triumph', "spaga's last stand"],
            ]),
            'Raffi':pd.DataFrame([
                ['why we dance', 'the champions', 'nughuffer', 'little lai', 'world is spinning'],
                ['shem-rah boo', 'spraypaint', 'crystal ball', 'anthem', 'down to the bottom'],
                ['mr. don', 'minions', 'times square', 'aquatic ape', 'papercut'],
                ['pygmy twylyte', 'hope', 'aceetobee', 'abraxas', '7-11'],
                ['naeba', 'catalyst', 'tourists (rocket ship)', 'lunar pursuit', "spaga's last stand"]
            ]),
            'player8':pd.DataFrame([
                ['and the ladies were the rest of the night', 'times square', 'morph dusseldorf', 'naeba', 'bernstein and chasnoff'],
                ['the champions', 'freeze', 'grass is green', 'i-man', 'space train'],
                ['why we dance', '42', 'abraxas', 'confrontation', "humuhumunukunukuapua'a"],
                ['aceetobee', 'crickets', 'crystal ball', 'highwire', 'mindless dribble'],
                ["mulberry's dream", 'save the robots', 'running into the night', 'spectacle', '7-11']
            ]),
            'player9':pd.DataFrame([
                ['42', 'hot air balloon', 'therapy', 'house dog party favor', 'mindless dribble'],
                ['shem-rah boo', 'bernstein and chasnoff', 'little betty boop', '7-11', 'i-man'],
                ['morph dusseldorf', 'spraypaint', 'crystal ball', 'rock candy', 'grass is green'],
                ['helicopters', 'save the robots', "mulberry's dream", 'run like hell', 'tempest'],
                ['the great abyss', "humuhumunukunukuapua'a", 'spaga', 'little shimmy in a conga line', 'jigsaw earth']
            ]),
            'player10':pd.DataFrame([
                ['7-11', "spaga's last stand", 'running into the night', 'lunar pursuit', 'anthem'],
                ['confrontation', 'nughuffer', 'spectacle', 'm1', 'jigsaw earth'],
                ['morph dusseldorf', 'munchkin invasion', 'naeba', 'abraxas', 'tourists (rocket ship)'],
                ['spraypaint', 'why we dance', 'shocked!', 'the great abyss', 'i-man'],
                ['helicopters', '42', 'crystal ball', 'on time', 'times square']
            ]),
            'Jesse':pd.DataFrame([
                ['why we dance', 'highwire', 'm.e.m.p.h.i.s.', 'times square', "spaga's last stand"],
                ['munchkin invasion', "trucker's choice", 'rock candy', 'space train', 'magellan'],
                ['little betty boop', 'crystal ball', 'naeba', 'spaga', 'spraypaint'],
                ['twisted in the road', 'anthem', 'home again', 'mindless dribble', "mulberry's dream"],
                ['shocked!', 'to be continued', 'freeze', 'the deal', 'another plan of attack']
            ]),
            # 'player9':pd.DataFrame([
            #     ['', '', '', '', ''],
            #     ['', '', '', '', ''],
            #     ['', '', '', '', ''],
            #     ['', '', '', '', ''],
            #     ['', '', '', '', ''],
            # ]),  
        }
        # self.songs = [i for i in self.boards.values()]
        self.winners = []
        # ['Rank', 'Player', 'Row/Col/Diag']
        self.rank = pd.DataFrame(columns=None)

    def board_songs(self):
        board_songs = []
        for board in self.boards.values():
            for row in board.values.tolist():
                board_songs += row

        board_songs = [' '] + list(set(board_songs))
        self.songs = board_songs
            
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
            self.rank = pd.concat([self.rank, row_df[['count']]])

            # Column
            col_rank = []
            for column in board:
                column = board[column].tolist()
                col_rank.append(column)
            col_df = pd.DataFrame(col_rank)
            col_df['count'] = [i.count('X') for i in col_rank]
            col_df['player'] = player
            col_df = col_df.set_index('player')
            self.rank = pd.concat([self.rank, col_df[['count']]])

            # Diagonal 1
            dia1 = np.diagonal(board)
            dia1_df = pd.DataFrame(dia1)
            dia1_df['count'] = [i.count('X') for i in dia1]
            dia1_df['player'] = player
            dia1_df = dia1_df.set_index('player')
            self.rank = pd.concat([self.rank, dia1_df[['count']]])

            # Diagonal 2
            dia2 = np.fliplr(board).diagonal()
            dia2_df = pd.DataFrame(dia2)
            dia2_df['count'] = [i.count('X') for i in dia2]
            dia2_df['player'] = player
            dia2_df = dia2_df.set_index('player')
            self.rank = pd.concat([self.rank, dia2_df[['count']]])

        self.rank = self.rank.sort_values(by=['count'], ascending=False)
        # self.rank = self.rank.drop_duplicates()
        # print(self.rank[['count']].head(5))

    def check_winner(self):
        self.winners = self.rank[self.rank['count'] == 5].index.unique() 

    def print_boards(self):
        for board in self.boards.items():
            st.write(board[0])
            st.table(board[1])

def main():
    b = Bingo()
    b.board_songs()
    count = 0
    x = st.empty()

    for i in range(200):
        song = st.sidebar.selectbox(f'Song {count+1}:', b.songs, key=str(count))
        count += 1 
        if song:
            b.update_boards(song)
            b.count_hits()
            b.check_winner()
            score = b.rank.sort_values(by=['count'], ascending=False)
            score = score[score['count'] != 0]

            x.dataframe(score.head(5))

    if len(b.winners) > 0:
        st.title('BINGO! The winner(s):')
        st.header(*b.winners.values)
        st.balloons()

    show = st.checkbox('show boards')
    if show:
        b.print_boards()

if __name__ == '__main__':
    main()

