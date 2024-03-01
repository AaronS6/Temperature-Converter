import tkinter

mainWindow = tkinter.Tk()

mainWindow.geometry("500x500")

mainWindow.title("Farenheit to Celsius app by Aaron")

mainWindow.config(bg="#CBF2FA")
def convert():
    celsius = float(farenheit.get()) - 32 * 5/9
    result.config(text=round(celsius,2))
farenheitText = tkinter.Label(text="Farenheit to Celsius conversion")
farenheitText.pack(pady=5)
farenheit = tkinter.Entry()
farenheit.pack()
button = tkinter.Button(text="Convert",command=convert)
button.pack(pady=10)
result = tkinter.Label(text="", bg=mainWindow['bg'], font=("Arial", 10, "italic"))
result.pack()

# run your application
mainWindow.mainloop()