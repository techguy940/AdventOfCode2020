with open("data.txt") as f:
  data = f.readlines()

data = list(map(int, data))

for i in data:
  for j in data:
      if i+j == 2020:
        print(i*j)
        break
