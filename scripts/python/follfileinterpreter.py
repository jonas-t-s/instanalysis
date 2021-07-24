import json
import sys


def getusername(user):
    return(user['string_list_data'][0]['value'])
def followerfileinterpreter(followersjsonfile):
    followers = []
    for user in followersjsonfile['relationships_followers']:
        followers.append(getusername(user))
    return followers
def followingfileinterpreter(followingfile):
    following = []
    for user in followingfile['relationships_following']:
        following.append(getusername(user))
    return following
