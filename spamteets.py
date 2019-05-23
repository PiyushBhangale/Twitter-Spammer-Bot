import tweepy
import tkinter
from tkinter import *
consumer_key = 'x2Ln6UagFdQt4uX7IRkvOyK4F'
consumer_secret = 'NbZk8qJ54Oczx5juE1MkU2RFv8zZyDGHvonDEbEKg0x48QtPd9'
access_token = '2642633694-dfwTS6CQEppxPfMeHZWE8pkq59BDovjibWjE5yA'
access_token_secret = 'popprfHATFtgEvfEpCORLh6hlHAHhL18RMtLCwOC74M3t'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def get_lab2():
    return m2.get()


def get_lab3():
    return m3.get()


def get_labd4():
    return m4.get()


def get_labd5():
    return m5.get()


def spamUser():
    no = get_labd5()
    for i in range(int(no)):

        tweetId = get_lab3()
        username = get_lab2()
        api.update_status("@" + username + " " + get_labd4()+str(i)+"th time.",
                          in_reply_to_status_id=tweetId)
        print("Replied with " + get_labd4()+" "+str(i)+"th time.")


root = Tk()
lab1 = Label(root, text="Spam a user")
lab1.pack()

lab2 = Label(root, text="tweetId")
lab2.pack()
m2 = Entry(root, bd=5)
m2.pack()

lab3 = Label(root, text="user name")
lab3.pack()
m3 = Entry(root, bd=5)
m3.pack()

lab4 = Label(root, text="Spam Message")
lab4.pack()
m4 = Entry(root, bd=5)
m4.pack()

lab5 = Label(root, text="Number of times")
lab5.pack()
m5 = Entry(root, bd=5)
m5.pack()

submit = Button(root, text="Spam", command=spamUser)
submit.pack(side=BOTTOM)
root.mainloop()
