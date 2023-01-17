numbers,ans,sum = [1,2,3,4,5,6,7],[],0
for i in range(len(numbers)-2):
    if i == 0: sum = numbers[i] + numbers[i+1] + numbers[i+2]; ans.append(sum); continue
    sum = sum - numbers[i-1] + numbers[i+2]
    ans.append(sum)
print(ans)