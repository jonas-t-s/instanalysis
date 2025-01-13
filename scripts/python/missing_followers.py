import os
import json
import sys
from follfileinterpreter import followerfileinterpreter
# from jsondiff import diff


""" 
In this file we analyse, if there are missing followers, which are no more following. 
Due to the limit of the data export, it may have false positives when an user changes its username. 
"""
if len(sys.argv) == 3 or len(sys.argv) == 2:

	if len(sys.argv) == 2 and os.path.isdir(sys.argv[1]):
		aLL_subdirs = [sys.argv[1] + "/" + d for d in os.listdir(sys.argv[1]) if os.path.isdir(sys.argv[1] + "/" + d)]
		print(aLL_subdirs)
		latest_subdir = max(aLL_subdirs, key=os.path.getmtime)
		json_file_new = open(latest_subdir + "/connections/followers_and_following/followers_1.json")
		print(f"newest subdir:{latest_subdir}")
		secondlatest_subdir = sorted(aLL_subdirs, key=os.path.getmtime)[-2]
		print(f"second newest subdir:{secondlatest_subdir}")
		json_file_old = open(secondlatest_subdir + "/connections/followers_and_following/followers_1.json")
	else:
		print("Old:", sys.argv[1])
		print("New:", sys.argv[2])
		json_file_old = open(sys.argv[1])
		json_file_new = open(sys.argv[2])
	connectionsold = json.load(json_file_old)
	# if the user gives us an old connectionsfile, we interpret it using the old format, else we interpret it in the new format
	if "connections" in sys.argv[1] and False: # Deactivate the old interpreter as the format changed again
		followerold = []
		for key in connectionsold['followers'].keys():
			followerold.append(key)
	else:
		followerold = followerfileinterpreter(connectionsold)
		#interpret it as a new friends file

	connectionsnew = json.load(json_file_new)
	print(connectionsnew)
	print(connectionsold)
	followernew = followerfileinterpreter(connectionsnew)
	json_file_new.close()
	json_file_old.close()

	if len(set(followerold).difference(followernew)) == 0:
		print("It looks like your friends like you. There is no unfollower!")
	else:
		import pprint
		# print("Users that followed you before, but now stopped to follow you:", (set(followerold).difference(followernew)));
		pprint.pprint("Users that followed you before, but now stopped to follow you:")
		pprint.pprint(set(followerold).difference(followernew))
		print("Please note, that these people also could have changed their username and therefore those people could also "
			  "be false positives, but luckily a simple search on the platform will allow you to test it.")
		print("Followers in the old dataset: ",len(followerold))
		print("Followers in the new dataset: ", len(followernew))
		print("Delta: ", len(followernew) - len(followerold))
else:
	print('correct usage: python missing_followers.py <connections_old.json> <connections_new.json> OR python missing_followers.py <followers_old.json> <followers_new.json>\n\n'
		  'Alternatively just provide the parent directory containing dataarchives extracted and we try to figure it out')


