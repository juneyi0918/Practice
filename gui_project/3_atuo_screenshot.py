import time
from PIL import ImageGrab

time.sleep(5) # 5 sec wait

for i in range(1,11):
    img = ImageGrab.grab()
    img.save("image{}.png".format(i))
    time.sleep(2)
    