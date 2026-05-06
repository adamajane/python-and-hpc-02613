with open("content.txt", "a") as f:
  f.write("Hello world")

with open("content.txt") as f:
  print(f.read())
