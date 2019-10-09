def convert_float(k):
  new_list = []
  for i in range(len(k)):
    j = int(k[i])
    new_list.append(j)
  return new_list

n = int(input())
z = int(input())

list_biggers = []
for i in range(n):
  numbers = input().split()
  numbers = convert_float(numbers)
  bigger = max(numbers)
  operation = bigger * 3   #calculating f(x) = x * 3
  list_biggers.append(operation)

final = sum(list_biggers)
final = final % z

print(final)
