import json
import sys

if len(sys.argv) == 2:
    print(sys.argv[1])
    try:
        following_set = set()
        follower_set = set()
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
    print('correct usage: python no_followback.py <connections.json>')
