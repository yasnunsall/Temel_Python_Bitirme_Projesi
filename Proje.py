# 1. Soru -------------------------------------------------------

iste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flatten_list = []

def flatten(x):
  global flatten_list
  for i in x:
    if type(i)==list:
      flatten(i)
    else:
      flatten_list.append(i)

flatten(liste)
print(flatten_list)

# 2. soru ---------------------------------------------------------

liste = [[1, 2], [3, 4], [5, 6, 7]]

def reverse_list(x):
  reversed_list = [None for i in range(len(x))]
  for idx, i in zip(range(len(x)-1, -1, -1), x):
    i.reverse()
    reversed_list[idx] = i

  return reversed_list

print(reverse_list(liste))
