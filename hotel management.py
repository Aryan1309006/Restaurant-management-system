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
    print("Welcome to our hotel: ")
    item1=input("What do you prefere: ")
    check(item1,menu,bill)


# If item is their then added in bill and using recursion we take order
def check(item,menu,bill):
    if item in menu:
        bill=bill+menu[item]
        print(f"Bill amount:{bill}")
        print("Please weit for 5 minits...")
        want=input("something else you want Yes/ No :")
        if(want=='yes'):
            item2=input("What do you prefere? :")
            check(item2,menu,bill)

        else:
            print(f"Your bill is{bill}")

    else:
        print("Item is not in hotel")
        print(f"Bill amount:{bill}")



print("_______________Hotel Aryan_____________________")
print("Menucard")
for key,value in menu.items():
    print(f"{key}:{value}")
print("\n \n")

TakeOrder(menu)