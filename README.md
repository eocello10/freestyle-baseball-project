# freestyle-baseball-project
Create code in order to allow inputs of certain players and receive outputs of their statistics. If I can include this in a notification service.

# Setup
- To start your setup there are a few prerequisites:
    1. Create a conda environment. Anaconda 3.7:
        - Type in conda create -n notifcations-env python=3.7 (first time only)
    2. Activate your conda environment
        - conda activate notifications-env
    3. You will need to install a few items:
     - pip install -r requirements.txt
        - This will connect with your requirements.txt which contains information about your notification service you will set up
            - python-dotenv
            - twilio
        - pip install pandas
            - This will help us deal with datframes
    4. Twilio Account setup
        - For SMS capabilities, [sign up for a Twilio account](https://www.twilio.com/try-twilio), click the link in a confirmation email to verify your account, then confirm a code sent to your phone to enable 2FA.
        - Then [create a new project](https://www.twilio.com/console/projects/create) with "Programmable SMS" capabilities. And from the console, view that project's Account SID and Auth Token. Update the contents of the ".env" file to specify these values as environment variables called `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN`, respectively.
        - You'll also need to [obtain a Twilio phone number](https://www.twilio.com/console/sms/getting-started/build) to send the messages from. After doing so, update the contents of the ".env" file to specify this value (including the plus sign at the beginning) as an environment variable called `SENDER_SMS`.
        - Finally, set an environment variable called `RECIPIENT_SMS` to specify the recipient's phone number (including the plus sign at the beginning).
    5. Create an .env file and setup with the below information:
        - TWILIO_ACCOUNT_SID="ABC123" # This will be provided once you create a twilio account
        - TWILIO_AUTH_TOKEN="123ABC" # This will be provided once you create a twilio account
        - SENDER_SMS="+1234567890" # This will be provided once you create a twilio account
        - RECIPIENT_SMS="+0987654321" # This can be whatever number you want your notification sent to
  

# Instructions

- As the user you have to ensure you have a command line properly set up. The proper setup is highlighted in the above SETUP section. This includes creating/activing the proper conda environment and installing the proper requirements.
- Once all requirements are instaled(note this only needs to happen the first time you enter into the command line) you will run the app. Type in python baseball.py
- Once that is entered you will see: "You must enter a qualified player's name. These are batters that currently ranked 1-160. Refer to README."
    - This is prompted to notify you that based on ESPN's statistics database/information the app only uses the players provided by the below links:
        - 'http://www.espn.com/mlb/stats/batting/_/year/2019/seasontype/2' #Players ranked 1-40
        - 'http://www.espn.com/mlb/stats/batting/_/count/41/qualified/true' #Players ranked 41-80
        - 'http://www.espn.com/mlb/stats/batting/_/count/81/qualified/true' #Players ranked 81-120
        - 'http://www.espn.com/mlb/stats/batting/_/count/121/qualified/true' #Players ranked 121-160
- After the note above you will be prompted to input a player's name (i.e. Cody Bellinger). You must enter it exactly as seen above. Capital first name and capital last name. The name comes specifically from the site. 
- Once you enter the player's name you will receive that player's stats as of the date you entered and a notification will be prompted and sent to your phone with the statistics requested via the Twilio information as created in SETUP
    - Example input: "Please Enter a player's name: Cody Bellinger"
    - Example output:   
                - PLAYER: Cody Bellinger
                - TEAM: LAD
                - HITS: 102
                - RUNS: 67
                - HOME RUNS: 27
                - RBI: 67
                - AVG: .346
                - OPS: 1.137
- NOTE: If a player is not in the links above you will receive a prompt "Invalid name. Please enter again." Also, after entering one player's name the code will end and you can run it again to enter a new player.
- That is STATS CHECK. Enjoy checking for your favorite players/fantasy player updates.
