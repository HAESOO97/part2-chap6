<삽입정렬>
데이터를 하나씩 확인하며,특정한 데이터를 적절한 위치에 삽입

array = [7,5,9,0,3,1,6,2,4,8]
for i in range(1,len(array)):
  for j in range(i,0,-1):인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
    if array[j]<array[j-1]:
      array[j],array[j-1] = array[j-1],array[j]
    else:
      break
print(array)
