from tkinter import *

root = Tk()
root.geometry('700x400')
root.configure(bg = '#141414')

imagepath = "C:/Users/Win/Downloads/Gold Exclusive Royal Luxury Hotel Logo.png"
image_pic = PhotoImage(file = imagepath).subsample(1, 1)
Label(root, image = image_pic, bg = '#141414').place(x = 310, y = -50)

Label(root, text = "Our Culinary and Hospitality Offerings",bg = "#141414", fg = "#c08e31", 
      font = ('Lucida Bright', 16, 'bold')).place(x = 15, y = 60)
Button(root, text = "Luxurious Rooms",bd = 0, bg = '#141414', fg = '#c08e31',
       font = ('Lucida Bright', 15), relief=RAISED).place(x = 15, y = 120)
Button(root, text = "Dine in", bd = 0, bg = '#141414', fg = '#c08e31',
       font = ('Lucida Bright', 15), relief=RAISED).place(x = 15, y = 160)
Button(root, text = "Party Hall", bd = 0, bg = '#141414', fg = '#c08e31',
       font = ('Lucida Bright', 15), relief=RAISED).place(x = 15, y = 200)
Button(root, text = "Bar", bd = 0, bg = '#141414', fg = '#c08e31',
       font = ('Lucida Bright', 15), relief=RAISED).place(x = 15, y = 240)
root.mainloop()