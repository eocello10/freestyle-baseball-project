
import pandas as pd

from baseball import determine_player

df = pd.read_html('http://www.espn.com/mlb/stats/batting/_/year/2019/seasontype/2')
df = pd.DataFrame(df[0])
headers = df.iloc[1]
df = pd.DataFrame(df.values[2:], columns = headers)
determine_player = df[(df['RK']>=str(1)) & (df['RK']<=str(40))]
#or is this integer rank???

def test_determination_of_player():
    assert determine_player(1-40) == True # represents a tie
    assert determine_player(>40) == False
#    assert determine_winner("rock", "scissors") == "rock"
#
#    assert determine_winner("paper", "rock") == "paper"
#    assert determine_winner("paper", "paper") == None # represents a tie
#    assert determine_winner("paper", "scissors") == "scissors"
#
#    assert determine_winner("scissors", "rock") == "rock"
#    assert determine_winner("scissors", "paper") == "scissors"
#    assert determine_winner("scissors", "scissors") == None # represents a tie
#
# if we run test with above we will see error..haven't defined/imported determine winner, can import many func on one file