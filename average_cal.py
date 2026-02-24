# Given the list below
# sales = [120,450,800,50,900,300]
# Write a Python code that classifies items in the list as Low, Medium, or High. 
# Also, do a count of items based on this classification and finally give a sum of items in each classification
# Key: less than 300 – low
#        > 300 <= 700 medium
# > 700 that's high



sales=[120,450,800,50,900,300]
for item in sales:
  if item<=300:
    print("low")
  elif 300 < item <=700:
    print("medium")
  elif item > 700:
    print("high")










