#map function
#basic syntax
def mul2(x):
  return x*2
testList = [1,2,3,4]
print map(mul2,testList)
print map(lambda x: x*3,testList)
#map function that has two arguments
def mul(x,y):
  return x*y
print map(mul,[1,2,3,4],testList)
