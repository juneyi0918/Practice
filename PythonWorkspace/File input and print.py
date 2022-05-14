# score_file = open("score.txt","w")
# print("Math: 0", file=score_file)
# print("English: 50", file=score_file)
# score_file.close()


# score_file = open("score.txt","a")
# score_file.write("Science: 80\n")
# score_file.write("Coding: 100")

# score_file= open("score.txt","r")
# print(score_file.read())
# score_file.close()

# score_file= open("score.txt","r")
# print(score_file.readline()) #read by line, after one read go next line
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt","r")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()


score_file = open("score.txt","r")
lines = score_file.readlines()
for line in lines:
    print(line, end="")

score_file.close()
