from tkinter import *

root = Tk()
root.title("Profit Calculator")
root.geometry("1600x1600")
root.configure(bg="pale green")

Title = Label(root, text="Min And Max Profit", bg="pale green", font=("Arial", 30))
MinProfitLabel = Label(root, bg="pale green", font=("Arial", 30))
MaxProfitLabel = Label(root, bg="pale green", font=("Arial", 30))


Month = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "october",
    "november",
    "december",
)

profit = (133, 234324, 32, 432, 4, 324, 23, 423, 6, 32, 32, 543)
monthIndex = 1

minIndex = profit.index(min(profit))
MinProfitLabel[
    "text"
] = f"The Minimum Profit of {profit[minIndex]} Which Is In {Month[minIndex]}"
maxIndex = profit.index(max(profit))
MaxProfitLabel[
    "text"
] = f"The Maximum Profit of {profit[maxIndex]} Which Is In {Month[maxIndex]}"

Title.place(relx=0.5, rely=0.1, anchor=CENTER)
MinProfitLabel.place(relx=0.5, rely=0.3, anchor=CENTER)
MaxProfitLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

root.mainloop()
