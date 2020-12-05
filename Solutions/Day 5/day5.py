with open("data.txt") as f:
  data = f.readlines()

def row(p):
    s = 0
    for i, c in enumerate(reversed(p)):
        if c == 'B':
            s += 2**i
    return s

def col(p):
    s = 0
    for i, c in enumerate(reversed(boarding_pass)):
        if c == 'R':
            s += 2**i
    return s

_data = [row(p[:7]) * 8 + col(p[7:]) for p in data]))
print(max(_data))

_ids = sorted(_data)

for a, b in zip(_ids, _ids[1:]):
    if b - a == 2:
        print(b - 1)
        break
