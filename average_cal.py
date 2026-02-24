# Given the list below
# sales = [120,450,800,50,900,300]
# Write a Python code that classifies items in the list as Low, Medium, or High. 
# Also, do a count of items based on this classification and finally give a sum of items in each classification
# Key: less than 300 – low
#        > 300 <= 700 medium
# > 700 that's high



sales=[120,450,800,50,900,300]
low =[]
medium =[]
high =[]

for sale in sales:
  if sale<=300:
    print(f"{sale} is low")
    low.append(sale)
  elif 300 < sale <=700:
    print(f"{sale} is medium")
    medium.append(sale)
  elif sale > 700:
    print(f"{sale} is high")
    high.append(sale)

sum_low = sum(low)
sum_medium=sum(medium)
sum_high= sum(high)

print (f"total sum of low sale is {sum_low} ")
print (f"total sum of medium sale is {sum_medium} ")
print (f"total sum of high sale is {sum_high} ")











