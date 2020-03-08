
import json
import sys
# from jsondiff import diff

if len(sys.argv) == 3:
    print "Old:", sys.argv[1]
    print "New:", sys.argv[2]
    json_file_old = open(sys.argv[1])
    connectionsold = json.load(json_file_old)
    json_file_new = open(sys.argv[2])
    connectionsnew = json.load(json_file_new)
    followerold = []
    followernew = []
    for user in connectionsold['followers']:
        followerold.append(user)
    for user in connectionsnew['followers']:
        followernew.append(user)

    found = None
    overall = None
    print("Users that followed you before, but now stopped to follow you:")
    for a, val in enumerate(followerold):
	for b, val in enumerate(followernew):
		#print b
		if followerold[a]==followernew[b]:
			found = True
			break
	if not found:
		overall = True
		print followerold[a]
		continue
	else:
		found = None

    if not overall:
	print("It looks like your friends like you. There is no unfollower!")
else:
    print('correct usage: python missing_followers.py <connections_old.json> <connections_new.json>')
