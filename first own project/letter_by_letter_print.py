import time

#sentence = 출력할 문자, timesl = 글자가 출력되는 시간간격(단위:초)
def slow_print (sentence, timesl=0.05):
    for i in range(len(sentence)):
        print(sentence[i], end="")
        time.sleep(timesl)
        