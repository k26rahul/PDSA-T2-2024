def shuffle(my_l1, my_l2):
  min_length = min([len(my_l1), len(my_l2)])

  result = []
  for i in range(min_length):
    result.append(my_l1[i])
    result.append(my_l2[i])

  result += my_l1[min_length:]
  result += my_l2[min_length:]

  return result


# l1 = list(map(int, input().split()))
# l2 = list(map(int, input().split()))

l1 = eval(input())
l2 = eval(input())
print(shuffle(l1, l2))
