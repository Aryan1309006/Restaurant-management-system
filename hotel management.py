#Menu card 

menu={
    "tea":15,
    "coffee":15,
    "vada pav":18,
    "Misal pav":50,
    "Margherita Pizza": 250,
    "Paneer Tikka": 180,
    "Chicken Biryani": 220,
    "Veg Burger": 120,
    "French Fries": 80,
    "Cold Coffee": 90,
    "Masala Dosa": 100,
    "Pav Bhaji": 110,
    "Gulab Jamun (2 pcs)": 50,
    "Butter Naan": 35
}

bill=0

#First order
def TakeOrder(menu):
    print("welcome to our hotel: ")
    item1=input("what do you prefere: ")
    check(item1,menu,bill)


# If item is their then added in bill and using recursion we take order
def check(item,menu,bill):
    if item in menu:
        bill=bill+menu[item]
        print(f"bill amount:{bill}")
        print("please weit for 5 minits...")
        want=input("something else you want Yes/ No :")
        if(want=='yes'):
            item2=input("what you want? :")
            check(item2,menu,bill)

        else:
            print(f"your bill is{bill}")

    else:
        print("item is not in hotel 😭")
        print(f"bill amount:{bill}")



print("_______________Hotel Aryan_____________________")
print("menucard")
for key,value in menu.items():
    print(f"{key}:{value}")
print("\n \n")

TakeOrder(menu)