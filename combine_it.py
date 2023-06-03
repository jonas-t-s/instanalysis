import json
import os
import sys

from scripts.python.follfileinterpreter import followerfileinterpreter


def main():
    print("hi")
    if len(sys.argv) != 3:
        print("USAGE: python3 combine_it.py FOLDER-TO-EXTRACTED-FOLDERS")
        sys.exit(1)
    data = dict()
    for filename in os.listdir(sys.argv[2]):
        if os.path.isdir(filename):

            #TODO: GET and process FORMAT FOR CONNECTIONS.json
            if os.path.exists(os.path.join(filename, "connections.json")):
                connectionsold = json.load(os.path.join(filename, "connections.json"))
                followerold = []
                for key in connectionsold['followers'].keys():
                    followerold.append(key)
                if os.path.basename in data.keys():
                    pass
                else:
                    data[os.path.basename(filename)]= dict()
                    data[os.path.basename(filename)]["followers"] = followerold
                continue
            else:
                followers = followerfileinterpreter(os.path.join(filename, "followers_and_following/followers_1.json"))
                following = followerfileinterpreter(os.path.join(filename, "followers_and_following/following.json"))
                data[os.path.basename(filename)] = dict()
                data[os.path.basename(filename)]["followers"] = followers
                data[os.path.basename(filename)]["following"] = following


            #TODO: GET and process FORMAT for newer


if __name__ == "__main__":
    main()
