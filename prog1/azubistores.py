


products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]




price_len = len(prices) # this is to get the lenght of the list

ave_g = sum(prices)/len(prices)

print("thanks")

print("this is all i can do")




print("this is the average price of all the products :",format(ave_g,'.2f')) # average price of all the products

print("")

new_price = [x-5 for x in prices] # this is to to subtract -5 from the price list
print("this is the new price list after subtracting 5 ghana cedis from the main price :",new_price) #new price list after subtracting 5 ghana cedis

print("")
#this is to sum eact price by customer from the price list and customer list

total_revenue = sum ([prices * last_week for prices,last_week in zip(prices,last_week)])


print(total_revenue)
 
print("")



ave_daily_rev = total_revenue/7

print("")

print("this is the daily average price of all sales made :",format(ave_daily_rev,'.2f'))

less_price = []
less_prod=[]
new_dict={}
d=0
print("")

newl=[item for item,price in zip(products,new_price) if price<30]

print("The list of product with price less than 30 :\n",newl)
