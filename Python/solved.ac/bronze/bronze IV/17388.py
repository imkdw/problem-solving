s, k, h = map(int, input().split())
if s + k + h >= 100:
    print('OK')
else:
    noob = min(s, k, h)
    if noob == s:
        print('Soongsil')
    elif noob == k:
        print('Korea')
    elif noob == h:
        print('Hanyang')