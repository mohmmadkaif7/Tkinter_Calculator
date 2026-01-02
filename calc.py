import tkinter as tk


def press(v):
    entry.insert(tk.END, v )
    # Called when a number or operator butten is clicked, Inserts the pressed value at the end of the entry widget.

def clear():
    entry.delete(0, tk.END)
    # Clears the entry widget.

def backspace():
    current = entry.get()
    if current:
        entry.delete(len(current)-1, tk.END)
    # Clears the entry widget.

def calc():
    try:
        result = eval(entry.get()) # entry.get() retrives the expression (e.g., 5+3)
        entry.delete(0, tk.END)  # clear the screeen
        entry.insert(0, result)  # display the result

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid Expression") # handles invalid expressions 
    
#Main window creation
root = tk.Tk() # Create the main application window
root.title("Calculator") # Set the title of the window
root.configure(bg = "black") # Set the background color 
root.resizable(False, False) # Disable window resizing

# Entry widget (Display screen)

entry = tk.Entry(
    root, 
    font=("Arial", 24),
    bg="#2d2d2d",
    fg="white",
    bd=0,
    justify="right"
)

entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

#Button Labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
] # represents calculator buttons

# Dynamic Buttom creation
r=1
c=0

for b in buttons:
    cmd = calc if b == '=' else lambda x=b: press(x)

    tk.Button(
        root,
        text=b,
        command=cmd,
        font=("Calaibri", 18),
        width=5,
        height=2,
        bg= '#ff9500' if b in "+-*/=" else '#3a4a4a',
        fg = 'white', 
        bd= 0
    ).grid(row=r,column=c, padx=6, pady=6)
    c+=1
    if c==4:
        r+=1
        c=0
        #move to next row after 4 columns

# Clear Button


tk.Button(
    root,
    text='C',
    command=clear,
    font=("Calaibri", 18),
    width=5,
    height=2,
    bg='#ff3b30',
    fg='white',
    bd=0
).grid(row=r, column=1, padx=6, pady=6)

# Backspace Button
tk.Button(
    root,
    text='<',
    command=backspace,
    font=("Calaibri", 18),
    width=5,
    height=2,
    bg="#07276e",
    fg='white',
    bd=0
).grid(row=r, column=2, padx=6, pady=6)

root.mainloop() # Start the Tkinter event loop
