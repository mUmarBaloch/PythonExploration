inputOrders:list[dict] = [
  { 'orderId': 101,'product': "abc" },
  { 'orderId': 102, 'product': "def" },
  { 'orderId': 104, 'product': "jkl" },
  { 'orderId': 103, 'product': "ghi" },
  { 'orderId': 105, 'product': "mno" },
  { 'orderId': 106, 'product': "jkl" },
  { 'orderId': 107, 'product': "mno" },
  { 'orderId': 108, 'product': "mno"}
]

employeedIds = ["xfg1e", "pol5c", "kkj8q"]
print(len(employeedIds))
outputOrders = [x for x in inputOrders]
index = 0 
for x in range(0,len(outputOrders)):
    outputOrders[x].update(employeeId=employeedIds[index])
    index+=1
    if(index > len(employeedIds)-1):
        index = 0

print(outputOrders)



