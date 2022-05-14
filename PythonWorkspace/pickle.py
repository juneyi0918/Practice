import pickle

### Make pickle
profile_file = open("profile.pickle","wb")
profile = {"Name":"June", "Age":24, "Hobby":["Soccer","Computer","Coding"]}
print(profile)
pickle.dump(profile, profile_file) # Save information in profile to FILE
profile_file.close()


### Read pickle
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)  # load profile_file to profile
print(profile)
profile_file.close()
