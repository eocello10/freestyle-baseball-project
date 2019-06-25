# freestyle-baseball-project
Create code in order to allow inputs of certain players and receive outputs of their statistics. If I can include this in a notification service.

# Setup
- To start your setup there are a few things you will need to do:
    1. Create a conda environment. I created:
        - Type in conda create notifcation-env python-3.7 environment into your command line
            - Note: notification-env can be anything you would like
    2. Activate your conda environment
        - conda activate notification-env
    3. You will need to install a few items:
     - pip install -r requirements.txt
        - This will connect with your requirements.txt which contains information about your notification service you will set up
            - python-dotenv
            - twilio
        - pip install lxml
        - pip install pandas
            - We will need to import pandas in order to deal with dataframe
    4. Twilio Account setup
        - For SMS capabilities, [sign up for a Twilio account](https://www.twilio.com/try-twilio), click the link in a confirmation email to verify your account, then confirm a code sent to your phone to enable 2FA.
        - Then [create a new project](https://www.twilio.com/console/projects/create) with "Programmable SMS" capabilities. And from the console, view that project's Account SID and Auth Token. Update the contents of the ".env" file to specify these values as environment variables called `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN`, respectively.
        - You'll also need to [obtain a Twilio phone number](https://www.twilio.com/console/sms/getting-started/build) to send the messages from. After doing so, update the contents of the ".env" file to specify this value (including the plus sign at the beginning) as an environment variable called `SENDER_SMS`.
        - Finally, set an environment variable called `RECIPIENT_SMS` to specify the recipient's phone number (including the plus sign at the beginning).
    5. Create an Env file and setup with the below information:
        - TWILIO_ACCOUNT_SID="ABC123" # This will be provided once you create a twilio account
        - TWILIO_AUTH_TOKEN="123ABC" # This will be provided once you create a twilio account
        - SENDER_SMS="+1234567890" # This will be provided once you create a twilio account
        - RECIPIENT_SMS="+0987654321" # This can be whatever number you want your notification sent to
    5. Required to have VS Text code editor and github.

# Requirements
 - You will need to import a few packages/modules
    - import pandas as pd
    - import os
    - import pprint
    - from dotenv import load_dotenv
    - from twilio.rest import Client
    - load_dotenv()

- Now you need to pull your dataframe. For this project, I combined four different urls that I converted to a dataframe using pandas. For each link shown below you need to repeate the steps that I will mention:
    - 'http://www.espn.com/mlb/stats/batting/_/year/2019/seasontype/2' #Players ranked 1-40
    - 'http://www.espn.com/mlb/stats/batting/_/count/41/qualified/true' #Players ranked 41-80
    - 'http://www.espn.com/mlb/stats/batting/_/count/81/qualified/true' #Players ranked 81-120
    - 'http://www.espn.com/mlb/stats/batting/_/count/121/qualified/true' #Players ranked 121-160

- Go into your command line and enter python to run this code and make sure it works properly. Once you ensure your dataframe is cleaned then you can enter this into your VS text code editor. Once comfortable with the dataframe these steps need to be repated for each url above:
    - df = pd.read_html('http://www.espn.com/mlb/stats/batting/_/year/2019/seasontype/2')
        - This step uses pandas to help read your dataframe and produce it in a readable fashion in our command line. If you enter df you will see the entire dataframe.
    - df = pd.DataFrame(df[0])
    - headers = df.iloc[1]
        - This will be used below. The goal is to remove headers. When we convert the url into a dataframe it repeast headers such as sortable batting and what column number each are. This will complicate our code if we leave it in so we must remove it.
    - df = pd.DataFrame(df.values[2:], columns = headers)
        - This code helps to remove the headers highlighted above. Also, it further cleans up our code to make it more readable and removes one of the rows pulled from the url (sortable batting)
    - df = df[df.RK != 'RK']
        - This code removes the rows that are repeated (i.e. PLAYER, RK, AVG, ETC.) after each 10 players. This is extra and not needed.
    - df = df.reset_index()
        - This needs to be performed so are index starts at 0 and does not skip any numbers. By editing the dataframe using the code above some of our index numbers got removed.       
    - df = df.drop(columns = ['index'])
        - Using code above  we add an extra column that we do not need.So we need to drop that column to simplify our dataframe.
    - df = df.fillna(method = 'ffill')
        - In our dataframe we have values = NaN. The best way is to use this code which will fill the NaN with the previous rank value (i.e. if the previous rank was 28. NaN will become 28. When we enter 28 into our code we will get two results)
- Once you repeat the code for each url you will want to concatenate it into one dataframe so when we ask for input and produce a result we are only pulling from one dataframe. It should look like:
    - df5 = pd.concat([df, df2, df3, df4])
