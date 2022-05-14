# Quiz) Every week you need to report this document

# - X week's Weekly report -
# Branch :
# Name :
# Summary :
# code program that makes file for 1~50th weekly report
# rule : file name should be '1 week's report.txt', '2 week's report.txt'....


for i in range(1,51):
    # report_file = open("{0} week's report.txt".format(i),"w")   ** HARD WAY **
    with open(str(i) + " " "week's report.txt","w") as report_file:
        report_file.write("- {0} week's weekly report - ".format(i))
        report_file.write("\nBranch : ")
        report_file.write("\nName : ")
        report_file.write("\nSummary : ")
    # report_file.close()  # NO NEED WITH WITH


    