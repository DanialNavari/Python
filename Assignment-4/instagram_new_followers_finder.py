#import library
import instaloader
import getpass

#save old followers in array
old_followers = []
f = open('followers.txt','r')
for user in f:
    old_followers.append(user)

#login instagram
L = instaloader.Instaloader()
username =  input("Enter username: ")
password = getpass.getpass("Enter password: ")
L.login(username,password)
print('Hoora!!')

#save user followers in array
profile = instaloader.profile.from_username(L.context,username)
new_followers = []
for follower in profile.get_followers():
    new_followers.append(follower)

#compare new and old followers together
for new_follower in new_followers:
    if new_follower not in old_followers:
        print(new_follower)

#save new list of followers
f = open('followers.txt','w')
for user in new_followers:
    f.write(user + '\n')

#close file
f.close()