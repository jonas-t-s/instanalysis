
import json
import sys
from follfileinterpreter import followerfileinterpreter
# from jsondiff import diff


""" 
In this file we analyse, if there are missing followers, which are no more following. 
Due to the limit of the data export, it may have false positives when an user changes it username. 
"""
if len(sys.argv) == 3:
	print("Old:", sys.argv[1])
	print("New:", sys.argv[2])
	json_file_old = open(sys.argv[1])
	connectionsold = json.load(json_file_old)
	# if the user gives us an old connectionsfile, we interpret it using the old format, else we interpret it in the new format
	if "connections" in sys.argv[1]:
		followerold = []
		for key in connectionsold['followers'].keys():
			followerold.append(key)
	else:
		followerold = followerfileinterpreter(connectionsold)
		#interpret it as a new friends file
	json_file_new = open(sys.argv[2])
	connectionsnew = json.load(json_file_new)
	followernew = followerfileinterpreter(connectionsnew)
	json_file_new.close()
	json_file_old.close()

	if len(set(followerold).difference(followernew)) == 0:
		print("It looks like your friends like you. There is no unfollower!")
	else:
		print("Users that followed you before, but now stopped to follow you:", (set(followerold).difference(followernew)));
		print("Please note, that these people also could have changed their username and therefore those people could also "
			  "false positives, but luckily a simple search on the platform will allow you to test it.")
else:
	print('correct usage: python missing_followers.py <connections_old.json> <connections_new.json> OR python missing_followers.py <followers_old.json> <followers_new.json>')


