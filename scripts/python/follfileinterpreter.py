import json
import sys
import zipfile

def getusername(user):
    return(user['string_list_data'][0]['value'])
def followerfileinterpreter(followersjsonfile):
    followers = []
    if "relationships_followers" in followersjsonfile:
        followersjsonfile = followersjsonfile["relationships_followers"]
    for user in followersjsonfile:
        followers.append(getusername(user))
    return followers
def followingfileinterpreter(followingfile):
    following = []
    for user in followingfile['relationships_following']:
        following.append(getusername(user))
    return following

def main():
    oldfiles = input("Where is the old downloaded archive located?")
    newfiles = input("Where is the new downloaded archive located?")
    with zipfile.ZipFile(oldfiles, 'r'), zipfile.ZipFile(newfiles, 'r') as oldfile, newfile:
        print(oldfile.read())
        print(newfile.read())
if __name__ == "__main__":
    main()