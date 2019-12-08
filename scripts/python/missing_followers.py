import json
import sys

if len(sys.argv) == 3:
 try:
    print "Old:", sys.argv[1]
    print "New:", sys.argv[2]
    json_file_old = open(sys.argv[1])
    connections_old = json.load(json_file_old)
    json_file_new = open(sys.argv[2])
    connections_new = json.load(json_file_new)
    follower_old = []
    follower_new = []
    for user in connections_old['followers']:
        follower_old.append(user)
    for user in connections_new['followers']:
        follower_new.append(user)

    found = None
    overall = None
    print("Users that followed you before, but now stopped to follow you:")
    for a, val in enumerate(follower_old):
	for b, val in enumerate(follower_new):
		#print b
		if follower_old[a]==follower_new[b]:
			found = True
			break
	if not found:
		overall = True
		print follower_old[a]
		continue
	else:
		found = None

    if not overall:
	print("It looks like your friends like you. Nobody has unfollowed you!")
 except FileNotFoundError:
      sys.exit("At least one of your files does not exist")
 except IOError: 
      sys.exit("At least one of your files is corrupt or doesn't exist")

else:
    print('correct usage: python missing_followers.py <connections_old.json> <connections_new.json>')
