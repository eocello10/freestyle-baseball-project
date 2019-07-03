
# df.reindex(df.index.drop(1))

#conda create -n notifcation-env python=3.7 environment
#conda activate notification-env for twilio
#Import for Twilios #have to also install pip-requirements and create a conda envrionment
### Code to figure out data frame - don't change line 6-11
#pip install -r requirements.txt, pip install pandas, # Not required - pip install lxml, pip instalL html5lib....

import pandas as pd

import os
import pprint
from dotenv import load_dotenv
from twilio.rest import Client
import datetime

load_dotenv()

df = pd.read_html('http://www.espn.com/mlb/stats/batting/_/year/2019/seasontype/2')

df = pd.DataFrame(df[0])

headers = df.iloc[1]
df = pd.DataFrame(df.values[2:], columns = headers)
df = df[df.PLAYER != 'PLAYER']
df = df.reset_index()
df = df.drop(columns = ['index'])
df = df.fillna(method = 'ffill')

#deleted my index
#df = df[df.RK != 'RK']
#this deletes my index
df2 = pd.read_html('http://www.espn.com/mlb/stats/batting/_/count/41/qualified/true')

df2 = pd.DataFrame(df2[0])

headers = df2.iloc[1]
df2 = pd.DataFrame(df2.values[2:], columns = headers)

df2 = df2[df2.PLAYER != 'PLAYER']

df2 = df2.reset_index()
df2 = df2.drop(columns = ['index'])
df2 = df2.fillna(method = 'ffill')

df3 = pd.read_html('http://www.espn.com/mlb/stats/batting/_/count/81/qualified/true')

df3 = pd.DataFrame(df3[0])

headers = df3.iloc[1]
df3 = pd.DataFrame(df3.values[2:], columns = headers)

df3 = df3[df3.PLAYER != 'PLAYER']

df3 = df3.reset_index()
df3 = df3.drop(columns = ['index'])
df3 = df3.fillna(method = 'ffill')

df4 = pd.read_html('http://www.espn.com/mlb/stats/batting/_/count/121/qualified/true')

df4 = pd.DataFrame(df4[0])

headers = df4.iloc[1]
df4 = pd.DataFrame(df4.values[2:], columns = headers)

df4 = df4[df4.PLAYER != 'PLAYER']

df4 = df4.reset_index()
df4 = df4.drop(columns = ['index'])
df4 = df4.fillna(method = 'ffill')

df5 = pd.concat([df, df2, df3, df4])
###Consider updating from rank to player. If do this add list of players in README
#print(df3)
#http://www.espn.com/mlb/stats/batting/_/count/81/qualified/true
#http://www.espn.com/mlb/stats/batting/_/count/121/qualified/true
#

#print(df3)
##dr.drop(['1'], axis=1) - Trying to drop column to left of rank. Does not work
#df = df[(df['RK']>=str(1)) & (df['RK']<=str(40))]
#print(df)
# print(len(df.index)) - illustrates I removed the "headers" for everything underneath first row


###Setup
# Might need to conda create and conda activate than install requirements - refer to twilio exercise

print("You must enter a qualified player's name. These are batters that currently rank 1-160. Refer to README links under Instructions.")


while True:
    #rank = input("Please enter a player's rank between 1-160 (NAN included for players tied in rank): ")
   #if rank.lower() == "done": #Think I have to use elif
   #    break
   #if df2.lower() == "done": #Think I have to use elif
   #    break
   #player = input("Please enter a player that is qualified based on ESPN's list(view README): ")
   ##if rank.lower() == "done": #Think I have to use elif
   ##    break
   ##if df2.lower() == "done": #Think I have to use elif
   ##    break
   # ROW = df5[df5['PLAYER']==player][['RK', 'PLAYER','TEAM','H','HR','AVG','OPS']]
  # if player in df5[df5['PLAYER']:
    name = str(input("Please Enter a player's name: "))# if wanted to focus on upper versus lower would have to add at end of input
    now = datetime.datetime.now()
    if name in str([i for i in df5.PLAYER]):  #find rank that is less than 41. need 1-40
        ROW = df5[df5['PLAYER']==name][['PLAYER','TEAM','H','R','HR','RBI','AVG','OPS']]
        #NAME_TEAM = "PLAYER NAME: " + df[df['RK']==rank]['PLAYER'] + "...TEAM: " + df[df['RK']==rank]['TEAM']
        #STATS = "HITS: " + df[df['RK']==rank]['H'] + "...HOME RUNS: " + df[df['RK']==rank]['HR']
        #MORE_STATS = "BATTING AVERAGE: " + df[df['RK']==rank]['AVG'] + "...OPS: " + df[df['RK']==rank]['OPS']
        print("Request date and time: " + now.strftime('%b %d %Y %I:%M %p'))
        print("PLAYER: " + str(ROW['PLAYER'].values[0]))
        print("TEAM: " + str(ROW['TEAM'].values[0]))
        print("HITS: " + str(ROW['H'].values[0]))
        print("RUNS: " + str(ROW['R'].values[0]))
        print("HOME RUNS: " + str(ROW['HR'].values[0]))
        print("RBI: " + str(ROW['RBI'].values[0]))
        print("AVG: " + str(ROW['AVG'].values[0]))
        print("OPS: " + str(ROW['OPS'].values[0]))
        print("------------------------------")
        break
   
#    #How dataframes work - When you pull a dtaaframe you get the index, value, column name, and data type
#    # #In order to only get the value out of a DF you have to use the values construct. by not using that previosuly I was getting all information (i.e. data type, index, etc.)    
#        #print(NAME_TEAM)
#        #print(STATS)
#        #print(MORE_STATS)
    else:
        print("Invalid name. Please enter a valid player.")
        exit()



#   rank = input("Please enter a player's rank between 41-80 (NAN included for players tied in rank): ")
#   if int(rank) <81:#find rank that is less than 41. need 1-40
#       ROW = df2[df2['RK']==rank][['PLAYER','TEAM','H','HR','AVG','OPS']]
#       #NAME_TEAM = "PLAYER NAME: " + df[df['RK']==rank]['PLAYER'] + "...TEAM: " + df[df['RK']==rank]['TEAM']
#       #STATS = "HITS: " + df[df['RK']==rank]['H'] + "...HOME RUNS: " + df[df['RK']==rank]['HR']
#       #MORE_STATS = "BATTING AVERAGE: " + df[df['RK']==rank]['AVG'] + "...OPS: " + df[df['RK']==rank]['OPS']
#       print("PLAYER: " + str(ROW['PLAYER'].values[0]))
#       print("TEAM: " + str(ROW['TEAM'].values[0]))
#       print("HITS: " + str(ROW['H'].values[0]))
#       print("HOME RUNS: " + str(ROW['HR'].values[0]))
#       print("AVG: " + str(ROW['AVG'].values[0]))
#       print("OPS: " + str(ROW['OPS'].values[0]))
#       print("------------------------------")
#       break
#    #How dataframes work - When you pull a dtaaframe you get the index, value, column name, and data type
#    # #In order to only get the value out of a DF you have to use the values construct. by not using that previosuly I was getting all information (i.e. data type, index, etc.)    
#        #print(NAME_TEAM)
#        #print(STATS)
#        #print(MORE_STATS)
#    else:
#        print("Invalid Rank. Ranks for this input has to be between 1-40. NAN also included (This means this player is tied in rank with another). Please enter again")
#        break
   #df[df['RK']==rank]['RK']
   #if df[df['RK']==rank]['RK'] not in df:
   #    print ("Invalid Rank. Ranks for this input has to be between 1-40. NAN also included (This means this player is tied in rank with another). Please enter again")
   #    break
   #else:
   #    print(NAME_TEAM)
   #    print(STATS)
   #    print(MORE_STATS)
   #    exit()
       
   #xrange = str(1-41)
   #if rank not in xrange(1, 41):
   #     print ("Invalid Rank. Ranks for this input has to be between 1-40. NAN also included (This means this player is tied in rank with another). Please enter again")
   #     break    
   #if rank in xrange(1, 41):
   #     print(NAME_TEAM)
   #     print (STATS)
   #     print(MORE_STATS)
   #     exit()
      
   #df[df['RK']==rank]['RK'] - this gave me all the information from the dataframe to make it cleanr see above description of values
   #    exit

        
#print(df[df.PLAYER == 'Cody Bellinger']) 
#print(df[df.RK == '{}.format(rank)']) #Simpler Approach
##try to figure out how to show the players they can choose from - make menu with a number


#1. how to iterate through the numbers (i.e. 41, 81, etc. for the url) - take url shell put curly braces in it and append to the url string the number you want to insert. need to do a for loop. When get to end of loop. have to append it to a dataframe that not working with
#x = pd.DataFrame()
# perform a for loop here for the above. insde of foor loop works with process above
##df = pd.read_html('http://www.espn.com/mlb/stats/batting/_/year/{}/seasontype/2'.format(i)) - take whatever number you are looping 

####Notification Service via Twilio
# adapted from:
# ... https://www.twilio.com/docs/libraries/python
# ... https://github.com/s2t2/birthday-wishes-py/commit/007c23f89dba5a8a87d85c6cf843c83514fc4736
# ... https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/twilio.md

#possibly might need to add a check here to make sure if greater than 40 error isn't an issue 
#Ask how i can get the message sent to someone else's phone
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", "OOPS, please specify env var called 'TWILIO_ACCOUNT_SID'")
TWILIO_AUTH_TOKEN  = os.environ.get("TWILIO_AUTH_TOKEN", "OOPS, please specify env var called 'TWILIO_AUTH_TOKEN'")
SENDER_SMS  = os.environ.get("SENDER_SMS", "OOPS, please specify env var called 'SENDER_SMS'")
RECIPIENT_SMS  = os.environ.get("RECIPIENT_SMS", "OOPS, please specify env var called 'RECIPIENT_SMS'")

### AUTHENTICATE

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

### COMPILE REQUEST PARAMETERS (PREPARE THE MESSAGE)

content = "Your 'STATS CHECK' notification as of " + now.strftime('%b %d %Y %I:%M %p') + "\nPlayer: " + str(ROW['PLAYER'].values[0]) + "\nTeam: " + str(ROW['TEAM'].values[0]) + "\nHITS: " + str(ROW['H'].values[0]) + "\nRUNS: " + str(ROW['R'].values[0]) + "\nHOME RUNS: " + str(ROW['HR'].values[0]) + "\nRBIs: " + str(ROW['RBI'].values[0]) + "\nAVG: " + str(ROW['AVG'].values[0]) + "\nOPS: " + str(ROW['OPS'].values[0])
#content = "Your daily 'STATS CHECK' notification. See the player you chose and his stats as of " + now.strftime('%b %d %Y %I:%M %p') + "\nPlayer: " + str(ROW['PLAYER'].values[0]) + "\nTeam: " + str(ROW['TEAM'].values[0]) 
### ISSUE REQUEST (SEND SMS)

message = client.messages.create(to=RECIPIENT_SMS, from_=SENDER_SMS, body=content)

### PARSE RESPONSE

pp = pprint.PrettyPrinter(indent=4)

print("----------------------")
print("SMS")
print("----------------------")
print("RESPONSE: ", type(message))
print("FROM:", message.from_)
print("TO:", message.to)
print("BODY:", message.body)
print("PROPERTIES:")
pp.pprint(dict(message._properties))
# Initial test with list to ensure I can test the simplified version of the code above 
#PLAYER = [
#{"Name": "Cody Bellinger", "Team": "LAD", "Runs":"54", "Hits":"88", "HR":"23", "RBI": "58", "AVG": ".355"},
#{"Name": "Christian Yelich", "Team":"MIL", "Runs": "56","Hits":"81", "HR":"26", "RBI": "57", "AVG": ".343",},	
#{"Name": "David Dahl", "Team": "COL", "Runs":"43", "Hits":"77", "HR":"7", "RBI": "35", "AVG": ".336",},
#{"Name": "Charlie Blackmon", "Team":"COL", "Runs": "49","Hits":"82", "HR":"16", "RBI": "47", "AVG": ".336"},	
#{"Name": "Jeff Mcneil", "Team": "NYM", "Runs":"26", "Hits":"70", "HR":"3", "RBI": "20", "AVG": ".333"},
#{"Name": "Jorge Polanco", "Team":"MIN", "Runs": "45","Hits":"90", "HR":"10", "RBI": "37", "AVG": ".332"},	
#{"Name": "Nolan Arenado", "Team": "COL", "Runs":"52", "Hits":"89", "HR":"17", "RBI": "57", "AVG": ".321"},
#{"Name": "Josh Bell", "Team":"PIT", "Runs": "52","Hits":"87", "HR":"19", "RBI": "65", "AVG": ".321"},	
#]
#
##print(PLAYER)
#