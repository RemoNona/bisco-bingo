import streamlit as st
import pandas as pd

c1, c2, c3, c4, c5 = st.columns(5)
count = 1
songs = ['', '42', '7-11', 'above the waves', 'abraxas', 'aceetobee', 'air song', 'and the ladies were the rest of the night', 'another plan of attack', 'anthem', 'aquatic ape', 'astronaut', 'astronomy domine', 'barfly', 'basis for a day', 'bazaar escape', 'bernstein and chasnoff', 'bombs', 'boom shanker', 'catalyst', 'caterpillar', 'caves of the east', 'chemical warfare brigade', 'clocks', 'commercial amen', 'confrontation', 'crickets', 'crystal ball', 'cyclone', 'dance of the sugar plum fairy', 'digital buddha', 'down to the bottom', 'eulogy', 'everybody needs somebody to love', 'evolve', 'feeling twisted', 'flash mob', 'floes', 'floodlights', 'freeze', 'frog legs', 'grass is green', 'haleakala crater', 'helicopters', 'high speed racer', 'highwire', 'home again', 'hope', 'hot air balloon', 'house dog party favor', "humuhumunukunukuapua'a", 'i remember when', 'i-man', 'jack straw', 'jamillia', 'jigsaw earth', 'kamaole sands', 'king of the world', 'kitchen mitts', 'knights of cydonia', 'konkrete', 'lake shore drive', 'liquid handcuffs', 'little betty boop', 'little lai', 'little shimmy in a conga line', 'loose change', 'lunar pursuit', 'm.e.m.p.h.i.s.', 'm1', 'm80', 'magellan', 'magellan reprise', 'meditation', 'mindless dribble', 'minions', 'miracles', 'mirrors', 'morph dusseldorf', 'moshi fameus', 'mr. don', "mulberry's dream", 'munchkin invasion', 'my lady survives', 'naeba', 'neck romancer', 'new song', 'news from nowhere', 'nughuffer', 'o fortuna', 'on time', 'onamae wa', 'once the fiddler paid', 'one chance to save the world', 'orch theme', 'papercut', 'park ave.', 'pat and dex', "pilin' it high", 'pimp blue rikkis', 'plan b', 'portal to an empty head', 'pygmy twylyte', 'radiator', 'rainbow song', 'resurrection', 'rivers', 'rock candy', 'rock your dance', 'rockafella', 'run like hell', 'running into the night', 'sabre dance', 'save the robots', 'shadow', "she's gone", 'shelby rose', 'shem-rah boo', 'shocked!', "sister judy's soul shack", 'songs of joy', 'sound one', 'space train', 'spacebirdmatingcall', 'spaga', "spaga's last stand", 'spectacle', 'spraypaint', 'spy', 'step inside', 'stone', 'story of the world', 'strobelights and martinis', 'svenghali', 'sweating bullets', 'tamarin alley', 'tempest', 'the big happy', 'the bridge', 'the champions', 'the city', 'the deal', "the devil's waltz", 'the great abyss', 'the overture', 'the safety dance', 'the thieving magpie', 'the truth', 'the tunnel', 'the very moon', 'the wormhole', 'therapy', 'three wishes', 'times square', 'to be continued', 'tourists (rocket ship)', 'tricycle', 'triumph', 'trooper mccue', "trucker's choice", 'twisted in the road', 'uber glue', 'vassillios', 'vibes', 'voices insane', 'we like to party', 'wet', "who's in charge?", 'why we dance', 'widgets', 'widow in the rain', 'wizards in winter', 'world is spinning', 'you and i', 'freebis slinky', 'times square']
board = []

e = st.empty()

for i in range(5):
    row = []
    r1 = c1.selectbox('', songs, key=str(count))
    count += 1
    r2 = c2.selectbox('', songs, key=str(count))
    count += 1
    r3 = c3.selectbox('', songs, key=str(count))
    count += 1
    r4 = c4.selectbox('', songs, key=str(count))
    count += 1
    r5 = c5.selectbox('', songs, key=str(count))
    count += 1
    row = [r1, r2, r3, r4, r5]
    
    board.append(row)


df = pd.DataFrame(board)
e.dataframe(df)

submit = st.checkbox('sumbit')
if submit:
    for i in board:
        print(i)
