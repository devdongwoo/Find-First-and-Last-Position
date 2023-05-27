def searchRange(nums, target):
  dict = {target: target}
  temp = []
  result = []

  for i in range(len(nums)):
    if nums[i] in dict:
      temp.append(i)

  if(len(temp) > 0):
    result.append(temp[0])
    result.append(temp[len(temp)-1])
  else:
    result.append(-1)
    result.append(-1)

  return result
print(searchRange([5,7,7,8,8,10],6))