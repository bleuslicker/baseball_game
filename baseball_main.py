from baseball_utils import *

MAX_TRY = 20

answer = make_answer()

tries =0
win =False
print('숫자 야구! 1~9 사이의 서로 다른 숫자 3개를 맞춰보세요 ')

while tries < MAX_TRY:
    text=input(f'{tries}')