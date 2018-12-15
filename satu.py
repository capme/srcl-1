def left_str(x):
 str = ""
 for i in range(0, 2):
  str = "{}{}".format(str, (x-1))
 return str

def right_str(x):
 str = ""
 for i in range(0, x):
  str = "{}{}".format(str, (x+1))
 return str

def fivaa(x):
 for i in range(x, 0, -1):
  row = "{}{}".format(left_str(i), right_str(i))
  print(row)
