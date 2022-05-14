# 자료구조의 변경
from typing import MutableSequence


menu = {"coffee","milk","juice"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))
