#Assignment_Day_1
#1
Rainbow
#2
for word in 'letsupgrade' :
    print(word.upper())
#3
cost_price = int(input(""))
selling_price = int(input(""))

if(cost_price > selling_price) :
    amount = cost_price - selling_price
    print("loss")
elif(cost_price < selling_price) :
    amount = selling_price - cost_price
    print("profit")
else:
    print("Neither")
#4
indian_rupee = int(input(""))
euro = indian_rupee * 80
print(euro)
   
       
    
