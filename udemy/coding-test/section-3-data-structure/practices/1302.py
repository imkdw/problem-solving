# https://www.acmicpc.net/problem/1302

from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())
books = [input().strip() for _ in range(N)]

books_count = Counter(books)
sorted_book_count = sorted(books_count.items(), key=lambda x: (-x[1], x[0]))
print(sorted_book_count[0][0])