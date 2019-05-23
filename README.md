## Twitter bot

#### This Twitter bot is meant to:
  - Follow everyone following you.
  - Favorite and Retweet a Tweet based on keywords.
  - Reply to a user based on a keyword.

#### How it works ?

You need to get the following credentials by creating an app on Twitter.
```
consumer_key = 'consumer key'
consumer_secret = 'consumer secrets'
access_token = 'access token'
access_token_secret = 'access token secret'

```
##### To retweet,favourite a tweet or to follow your followers run the following script.
```
sudo python3 tweet-bot.py
```
  - Fill in the _consumer_key,consumer_secret, access_token and access_token_secret_ and click _**Get User**_ button to authenticate.
 
  - Fill the _reply, retweet, favourite and follow_ with a response _**yes**_ for the respective functionality to be performed. Here follow with a _**yes**_ response wil follow all of your followers.

  - The _search_ needs to be filled with the _keyword_ regarding which the tweets will be fetched.

  - The _Number of tweets_ must be filled with a number.

![alt text](https://github.com/PiyushBhangale/Twitter-Bot/blob/master/Screenshot%20from%202019-05-23%2021-30-05.png)


##### To spam a users profile with n number of tweets run the following script.
```
sudo python3 spamteets.py
```
  - Fill in the authentication details.
  - Enter the tweetId and Username of the profile to be spammed.
  - Enter the spam message and number of times th tweet to be repeated.

![alt text](https://github.com/PiyushBhangale/Twitter-Bot/blob/master/Screenshot%20from%202019-05-23%2021-40-57.png)
