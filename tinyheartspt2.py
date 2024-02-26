import tkinter as tk

def pop_up_heart():
    global big_heart
    big_heart = tk.Label(window, text="❤️", font=("Arial", 80), fg="red")
    big_heart.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

window = tk.Tk()
window.title("Big Heart Pop Up")

button = tk.Button(window, text="Pop Up Big Heart", command=pop_up_heart)
button.pack(pady=10)

window.geometry("400x300")  # Set window size

window.mainloop()
