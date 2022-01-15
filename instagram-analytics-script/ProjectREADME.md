# SETUP
## What you will need installed 
    1. Download Latest Version of python if not installed already 
    2. Install PIP if not installed already
    3. Install requests library if not installed already
    4. Install python.dotenv if not installed already
## Instagram Account Setup
    1. First Your instagram account will have to be set to a buisness account
    2. Next create a facebook page from your facebook you can do this following this link https://www.businessinsider.com/how-to-create-a-facebook-business-page
    3. Next connect your instagram account to your facebook page. Follow this link for help. https://www.businessinsider.com/how-to-create-a-facebook-business-page
## API KEYS SETUP
    1. Now that you have your accounts connected you will need your API Keys and passwords to run this app.
    2. Follow this video to get your access token, clientid, and clientsecret. https://www.youtube.com/watch?v=c8i4CaELPME&t=213s
       1. Note when creating app on facebook give following permissions
          1. pages_manage_instant_articles
          2. pages_show_list
          3. instagram_basic
          4. instagram_manage_comments
          5. instagram_manage_insights
          6. instagram_manage_messages
          7. pages_read_engagment
          8. pages_manage_metadata
          9. pages_read_user_content
          10. pages_manage_engagment
          11. public_profile
    3. Paste those values in the .env file in the same format the dummy values are in. The appID is the client_id and the App secret is the client secret value in .env 
    4. In the terminal  type cd instagram-analytics-script then type python long_lived_access_token.py  copy and paste the value it gives into the accesstoken value in .env file this is a 3 month token so you won't have to generate another one in an hour or whenever you want to run it. 
    5. Next get your facebook pages id by typing python get_users_pages.py paste the number it prints to terminal in the page_id value in .env
    6. Next get your page access token by following the directions below.
        1. Go to https://developers.facebook.com/
        2. Click on My Apps
        3. Select the app you created 
        4. On the top right select tools and then hover down and click on Graph API explorer
        5. Then where it states user or page click on it and select the field under page access tokens
        6. Copy the acccess token at the top and paste it into page access token field in .env
    7. Finally in the terminal type python get_instagram_account.py and paste the instagram account id into the .env file that it provides in the instagram_account field and type the instagramusername of the account in the ig_username field
## Program Run Instructions
    1. Uncomment out lines 8-15 in webscraper.py then in terminal make sure you are cd'ed into instagram-analytics-script then type python webscraper.py this collects the current data from the instagram account and stores it into a sqlite database
    2. Repeat  step 1  after a few seconds as the statistics can only be run if you have 2 datasets but make sure to recomment out lines 8-15
    3. Next type python main.py and it will print out the statistics on your instagram account
    4. Run step 1 wenever desired and see how your instagram stats have changed since you last ran the script.
## Tests


