# import pickle


# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))


#### Write txt using open ####
with open("study.txt", "w") as study_file:
    study_file.write("I am studying Python hard")

#### Load and Read txt using open ####
with open("study.txt","r") as study_file:
    print(study_file.read())
