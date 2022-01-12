import math

melody, song_cnt = map(int, input().split())
print(math.ceil(melody / song_cnt))