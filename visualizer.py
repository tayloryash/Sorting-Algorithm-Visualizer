from tkinter import *
from tkinter import ttk
import random
import customtkinter

from colors import *

# Importing algorithms
import algos

# Main window
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
#root = Tk()
root.title("Sorting Algorithms Visualization")
root.iconbitmap('sorting.ico')
root.geometry("870x530")
#root.maxsize(1200, 800)
root.config(bg=WHITE)

algorithm_name = StringVar()
algo_list = ['Bubble Sort', 'Merge Sort', 'Insertion Sort', 'Selection Sort','Quick Sort']

speed_type = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']

sorting_order = StringVar()
order_list = ['Ascending', 'Descending']

data = []


# This function will draw randomly generated list data[] on the canvas as vertical bars
def paintData(data, colorArray,c):
    canvas2.delete('all')
    canvas.delete('all')
    canvas_width = 1000
    canvas_height = 400
    x_width = canvas_width / (len(data)) - 6 / w1.get()
    x_offset = 5
    space = 2

    for i, height in enumerate(data):
        x0 = x_offset + space + i * x_width
        y0 = canvas_height + 10 - (390 / max(data)) * height
        x1 = (i + 1) * x_width + x_offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        if w1.get() <= 40:
            canvas.create_text(x0 + 11, y0 - 8, text=height, fill="black", font='Helvetica 9')
        if 40 < w1.get() < 60 and not i % 5:
            canvas.create_text(x0 + 8, y0 - 8, text=height, fill="black", font='Helvetica 8')

        canvas2.create_text(255, 50, text=c, fill="black", font='Helvetica 11 ')
        if algo_menu.get() == 'Bubble Sort':
            complexities('Bubble Sort')
        elif algo_menu.get() == 'Merge Sort':
            complexities('Merge Sort')
        elif algo_menu.get() == 'Insertion Sort':
            complexities('Insertion Sort')
        elif algo_menu.get() == 'Selection Sort':
            complexities('Selection Sort')
        elif algo_menu.get() == 'Quick Sort':
            complexities('Quick Sort')
    root.update_idletasks()


# This function will generate array with random values every time we hit the generate button
def generateData():
    global data

    data = []
    for i in range(0, w1.get()):
        random_value = random.randint(5, 200)
        data.append(random_value)

    paintData(data, [BLUE for x in range(len(data))],0)


# This function will set sorting speed
def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.5
    elif speed_menu.get() == 'Medium':
        return 0.05
    else:
        return 0


# This funciton will trigger a selected algorithm and start sorting
def sort():
    global data
    timeTick = set_speed()

    if algo_menu.get() == 'Bubble Sort':
        algos.bubble_sort(data, paintData, timeTick, order_menu.get() == 'Ascending')
        algos.c = 0
    elif algo_menu.get() == 'Merge Sort':
        algos.merge_sort(data, 0, len(data) - 1, paintData, timeTick, order_menu.get() == 'Ascending')
        algos.c = 0
    elif algo_menu.get() == 'Insertion Sort':
        algos.insertion_sort(data, paintData, timeTick, order_menu.get() == 'Ascending')
        algos.c = 0
    elif algo_menu.get() == 'Selection Sort':
        algos.selection_sort(data, paintData, timeTick, order_menu.get() == 'Ascending')
        algos.c = 0
    elif algo_menu.get() == 'Quick Sort':
        algos.quick(data, 0, len(data)-1, paintData, timeTick, order_menu.get() == 'Ascending')
        algos.c = 0

def complexities(case):

    if case == 'Bubble Sort':
        canvas2.create_text(150, 50, text="No. of Comparisons: ", fill="black", font='Helvetica 11 bold')
        canvas2.create_text(150, 180, text="Worst Case: O(n²)", fill="black", font='Helvetica 11 bold')
        canvas2.create_text(150, 140, text="Average Case: Θ(n²)", fill="black", font='Helvetica 11 bold')
        canvas2.create_text(150, 100, text="Best Case: Ω(n)", fill="black", font='Helvetica 11 bold')
    elif case == 'Merge Sort':
        canvas2.create_text(150, 50, text="No. of Comparisons: ", fill="black", font='Helvetica 11 bold')
        canvas2.create_text(150, 180, text="Worst Case: O(n log n)", fill="black", font='Helvetica 11 bold')
        canvas2.create_text(150, 140, text="Average Case: Θ(n log n)", fill="black", font='Helvetica 11 bold')
        canvas2.create_text(150, 100, text="Best Case: Ω(n log n)", fill="black", font='Helvetica 11 bold')
    elif case == 'Insertion Sort':
        canvas2.create_text(150, 50, text="No. of Comparisons: ", fill="black", font='Helvetica 11 bold')
        canvas2.create_text(150, 180, text="Worst Case: O(n²)", fill="black", font='Helvetica 11 bold')
        canvas2.create_text(150, 140, text="Average Case: Θ(n²)", fill="black", font='Helvetica 11 bold')
        canvas2.create_text(150, 100, text="Best Case: Ω(n)", fill="black", font='Helvetica 11 bold')
    elif case == 'Selection Sort':
        canvas2.create_text(150, 50, text="No. of Comparisons: ", fill="black", font='Helvetica 11 bold')
        canvas2.create_text(150, 180, text="Worst Case: O(n²)", fill="black", font='Helvetica 11 bold')
        canvas2.create_text(150, 140, text="Average Case: Θ(n²)", fill="black", font='Helvetica 11 bold')
        canvas2.create_text(150, 100, text="Best Case: Ω(n²)", fill="black", font='Helvetica 11 bold')
    elif case == 'Quick Sort':
        canvas2.create_text(150, 50, text="No. of Comparisons: ", fill="black", font='Helvetica 11 bold')
        canvas2.create_text(150, 180, text="Worst Case: O(n²)", fill="black", font='Helvetica 11 bold')
        canvas2.create_text(150, 140, text="Average Case: Θ(n*log n)", fill="black", font='Helvetica 11 bold')
        canvas2.create_text(150, 100, text="Best Case: Ω(n*log n)", fill="black", font='Helvetica 11 bold')

### User interface here ###
portion_UI =  customtkinter.CTkFrame(root, width=300, height=200)
portion_UI.grid(row=0, column=0, padx=10, pady=5)

# dropdown to select sorting algorithm
l1 = customtkinter.CTkLabel(portion_UI, text="Algorithm:")
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(portion_UI, state="readonly", textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

# dropdown to select sorting speed
l2 = customtkinter.CTkLabel(portion_UI, text="Sorting Speed:", bg=BLUE)
l2.grid(row=0, column=2, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(portion_UI, state="readonly", textvariable=speed_type, values=speed_list)
speed_menu.grid(row=0, column=3, padx=5, pady=5)
speed_menu.current(1)

# Array size
l3 = customtkinter.CTkLabel(portion_UI, text="Array Size:", bg=BLUE)
l3.grid(row=1, column=0, padx=10, pady=5, sticky=W)
w1 = Scale(portion_UI, from_=20, to=100, orient=HORIZONTAL)

w1.set(50)
w1.grid(row=1, column=1, padx=10, pady=5)

# Order
l4 = customtkinter.CTkLabel(portion_UI, text="Order of Sorting", bg=BLUE)
l4.grid(row=1, column=2, padx=10, pady=5, sticky=W)
order_menu = ttk.Combobox(portion_UI, state="readonly", textvariable=sorting_order, values=order_list, style='D.TCombobox')
order_menu.grid(row=1, column=3, padx=5, pady=5)
order_menu.current(0)






# sort button
b1 = customtkinter.CTkButton(portion_UI, text="Sort", command=sort)
b1.grid(row=2, column=1, padx=5, pady=5)

# button for generating array
b3 = customtkinter.CTkButton(portion_UI, text="Generate Array", command=generateData)
b3.grid(row=2, column=0, padx=5, pady=5)

# canvas to draw our array
canvas = Canvas(root, width=1000, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5, columnspan=2)

canvas2 = Canvas(root, width=290, height=200, bg=WHITE, highlightbackground=BLUE, highlightthickness=2)
canvas2.grid(row=0, column=1, padx=10, pady=5)


root.mainloop()
