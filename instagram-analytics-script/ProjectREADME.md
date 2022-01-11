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
    2. Follow this video to get your access token, clientid, and clientsecret, [API Access tokens](https://www.youtube.com/watch?v=c8i4CaELPME&list=PL0glhsZ01I-BAFwPmQBWMNqUDnkSlOR6r&index=9)
    3. Paste those values in the .env file in the same format the dummy values are
    4. in the terminal cd into instagram-analytics0script then type python long_lived_access_token.py  copy and paste the value it gives into the accesstoken value in.env this is a 3 month token so you won't have to generate another one in an hour or whenever you want to run it. 
    5. Next get your facebook pages id by typing python get_users_pages.py paste the number it prints to terminal in the page_id value in .env
    6. Next get your page access token by following the directions below.
    7. Finally in the terminal type python get_instagram_account and paste the instagram account id into the .env file that it provides



