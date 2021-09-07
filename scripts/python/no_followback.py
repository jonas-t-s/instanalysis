import json
import pprint
import sys
import follfileinterpreter
"""
In this file we analyse how the relations of the user to his followers and vice versa are.
"""
if len(sys.argv) == 2 or len(sys.argv) == 3:
    print(sys.argv)
    following_set = set()
    follower_set = set()
    if len(sys.argv) == 2:
        try:
            json_file = open(sys.argv[1])
            connections = json.load(json_file)
            for user in connections['following']:
                following_set.add(user)
            for user in connections['followers']:
                follower_set.add(user)

            print("Your followers that you do not follow back:")
            for user in follower_set.difference(following_set):
                print(user)

            print("Users you follow that do not follow you back")
            for user in following_set.difference(follower_set):
                print(user)
        except FileNotFoundError:
            print('The file:', sys.argv[1], 'does not exist')
    else:
        followerfile = open(sys.argv[1])
        followerjson = json.load(followerfile)
        followingfile= open(sys.argv[2])
        followingjson = json.load(followingfile)
        followers = follfileinterpreter.followerfileinterpreter(followerjson)
        following = follfileinterpreter.followingfileinterpreter(followingjson)
        #print("Your followers that you do not follow back:", set(followers).difference(following))
        pprint.pprint("Your followers that you do not follow back:")
        pprint.pprint(set(followers).difference(following))
        #print("Users you follow that do not follow you back", set(following).difference(followers))
        pprint.pprint("Users you follow that do not follow you back")
        pprint.pprint(set(following).difference(followers))
else:
    print('Correct usage: python no_followback.py <connections.json> OR python no_followback.py <followers.json> <following.json>')
