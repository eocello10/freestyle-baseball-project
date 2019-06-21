
# df.reindex(df.index.drop(1))


### Code to figure out data frame - don't change line 6-11
import pandas as pd
#Imports for Twilio - have to also install pip-requirements and create a conda envrionment
#import os
#import pprint
#
#from dotenv import load_dotenv
#from twilio.rest import Client

#load_dotenv()
#import requests
df = pd.read_html('http://www.espn.com/mlb/stats/batting/_/year/2019/seasontype/2')
df = pd.DataFrame(df[0])
headers = df.iloc[1]
df = pd.DataFrame(df.values[2:], columns = headers)
#df = df[df.PLAYER != 'PLAYER']
df = df[df.RK != 'RK']
#import requests

# print(len(df.index)) - illustrates I removed the "headers" for everything underneath first row
# all columns are objects which are strings
#df3.OBP = pd.to_numeric(df3.OBP) - need to try and convert this to a float instead of oobject??? OR DO i NEED TO
#df3.OBP.mean() - find the mean of the 40 players on there
#df3.to_csv('Baseballstats.csv', index = False) - saved info to a file - index = False removes row numbers
###This line is not needed. Just for me to see what happened #df.head() - produces data in a readable format for me

###Setup
# Might need to conda create and conda activate than install requirements - refer to twilio exercise

while True:
   rank = input("Please enter a player: ")
   Stats = "PLAYER NAME: " + df[df['RK']==rank]['PLAYER'] + "...TEAM: " + df[df['RK']==rank]['TEAM']
   print(Stats)
   #if (<some condition met>):
   #    exit

#while True:
#   rank = input("Please enter a player: ")
   
#   if rank == df['RK']:# a value in the df list 
#        print(Stats)
#   #else:
   #     request_url = f"http://www.espn.com/mlb/stats/batting/_/year/2019/seasontype/2"
   #     response = requests.get(request_url)
   #     break
        
#print(df[df.PLAYER == 'Cody Bellinger']) 
#print(df[df.RK == '{}.format(rank)']) #Simpler Approach
#IF THEY GIVE SOMETHING ABOVE FORTY IT IS INVALID
#1. get user input
#2. put braces {}
#3. replace braces with user input
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


#
#TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", "OOPS, please specify env var called 'TWILIO_ACCOUNT_SID'")
#TWILIO_AUTH_TOKEN  = os.environ.get("TWILIO_AUTH_TOKEN", "OOPS, please specify env var called 'TWILIO_AUTH_TOKEN'")
#SENDER_SMS  = os.environ.get("SENDER_SMS", "OOPS, please specify env var called 'SENDER_SMS'")
#RECIPIENT_SMS  = os.environ.get("RECIPIENT_SMS", "OOPS, please specify env var called 'RECIPIENT_SMS'")
#
## AUTHENTICATE
#
#client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
#
## COMPILE REQUEST PARAMETERS (PREPARE THE MESSAGE)
#
#content = "Hello, this is a message from your personal notification service. TODO: customize me!"
#
## ISSUE REQUEST (SEND SMS)
#
#message = client.messages.create(to=RECIPIENT_SMS, from_=SENDER_SMS, body=content)
#
## PARSE RESPONSE
#
#pp = pprint.PrettyPrinter(indent=4)
#
#print("----------------------")
#print("SMS")
#print("----------------------")
#print("RESPONSE: ", type(message))
#print("FROM:", message.from_)
#print("TO:", message.to)
#print("BODY:", message.body)
#print("PROPERTIES:")
#pp.pprint(dict(message._properties))


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
#selected_players = []
#Valid_players = []
#for i in PLAYER:
#    Valid_players.append(i["Name"])
#
#while True:
#    Player_name = input("Please enter a player's name:")
#    if Player_name.lower() == "done": #Think I have to use elif
#        break
#    while Player_name not in str(Valid_players): # either make an elif or add another break
#        print ("Invalid player name. Choose again")
#        break
#    else:
#        selected_players.append(Player_name)
#
#
#for Player_name in selected_players:
#    Stats  = [p for p in PLAYER if str(p["Name"]) == str(Player_name)] 
#    Stats = Stats[0]
#    print("Team: " + Stats["Team"] + "Runs: " + Stats["Runs"] + "Hits: " + Stats["Hits"] + "Stats: " + Stats["HR"] + "RBI: " + Stats["RBI"] + "AVG: " + Stats["AVG"]) 
