from tkinter import *
from tkinter.messagebox import *
import re

product_list = []

def name_validator(name):
    if re.match(r"^[a-zA-Z0-9\s]{3,15}$", name):
        return True
    else:
        return False


def price_validator(price):
    if re.match(r"^[0-9]+$", price):
        return True
    else:
        return False


def save_product():
    name = product_name.get()
    quantity = product_quantity.get()
    price = product_price.get()

    if name_validator(name) and price_validator(price) and\
            price.isdigit() and 0< int(price)< 1000 and\
            quantity.isdigit() and 1 < int(quantity) < 10:
        product={"name": name, "quantity": quantity, "price": price}
        product_list.append(product)
        print(product_list)
        product_name.set("")
        product_quantity.set("")
        product_price.set("")
        # total
        total = int(quantity) * int(price)
        total_label.config(text=f"Total: {total}")

        showinfo("Save","Product Saved")
    else:
        showerror("Error", "Please enter a valid value!")



window = Tk()

window.geometry("300x300")
window.title("Product List")

# variables
product_name = StringVar()
product_quantity = StringVar()
product_price = StringVar()

# product name
Label(window, text="Product Name:").place(x=20, y=20)
Entry(window, width=20, textvariable=product_name).place(x=20, y=50)

# product quantity
Label(window, text="Product Quantity:").place(x=20, y=80)
Entry(window, width=20, textvariable=product_quantity).place(x=20, y=110)

# product price
Label(window, text="Product Price:").place(x=20, y=140)
Entry(window, width=20, textvariable=product_price).place(x=20, y=170)

#total label
total_label=Label(window, text="Total:",font=10)
total_label.place(x=130, y=130)

# save button
Button(window, text="Save", width=10, command=save_product).place(x=110, y=230)

window.mainloop()
