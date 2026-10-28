
import tkinter as tk
import math


# Main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("330x410")
root.resizable(False, False)
root.configure(bg="#000000")


expression = ""


# Display
display = tk.Entry(
    root,
    font=("Arial", 18),
    justify="right",
    bd=3,
    relief="sunken"
)
display.place(x=15, y=15, width=300, height=38)


def press(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)


def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)


def calculate():
    global expression
    try:
        # Allow only calculator characters before evaluating
        allowed = "0123456789+-*/(). "
        if not all(char in allowed for char in expression):
            raise ValueError

        result = eval(expression, {"__builtins__": {}}, {})
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
        expression = str(result)

    except (ValueError, ZeroDivisionError, SyntaxError, TypeError):
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""


def scientific(operation):
    global expression
    try:
        value = float(display.get())

        if operation == "√":
            result = math.sqrt(value)
        elif operation == "sin":
            result = math.sin(math.radians(value))
        elif operation == "cos":
            result = math.cos(math.radians(value))
        elif operation == "tan":
            result = math.tan(math.radians(value))
        elif operation == "log":
            result = math.log10(value)
        elif operation == "x²":
            result = value ** 2
        else:
            return

        expression = str(result)
        display.delete(0, tk.END)
        display.insert(tk.END, expression)

    except (ValueError, ZeroDivisionError):
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""


# Button helper
def make_button(text, x, y, width, command, color="#FF9500"):
    button = tk.Button(
        root,
        text=text,
        font=("Arial", 11),
        bg=color,
        fg="white",
        activebackground="#E68A00",
        activeforeground="white",
        command=command
    )
    button.place(x=x, y=y, width=width, height=30)


# Number buttons
buttons = [
    ("1", 15, 60), ("2", 95, 60), ("3", 175, 60),
    ("4", 15, 98), ("5", 95, 98), ("6", 175, 98),
    ("7", 15, 136), ("8", 95, 136), ("9", 175, 136),
    ("0", 95, 174),
]

for text, x, y in buttons:
    make_button(
        text, x, y, 75,
        lambda value=text: press(value),
        color="#3A3A3C"
    )


# Basic operation buttons
make_button("+", 15, 212, 75, lambda: press("+"))
make_button("-", 95, 212, 75, lambda: press("-"))
make_button("*", 175, 212, 75, lambda: press("*"))
make_button("/", 15, 250, 75, lambda: press("/"))
make_button("Clear", 95, 250, 155, clear, color="#3A3A3C")
make_button("=", 60, 288, 170, calculate)


# Scientific functions
make_button("√", 15, 326, 45, lambda: scientific("√"))
make_button("x²", 68, 326, 45, lambda: scientific("x²"))
make_button("sin", 121, 326, 45, lambda: scientific("sin"))
make_button("cos", 174, 326, 45, lambda: scientific("cos"))
make_button("log", 227, 326, 45, lambda: scientific("log"))


root.mainloop()
