import random
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# =========================
# DATA GENERATOR
# =========================

def generate_data(size):

    global data
    data = [random.randint(10,100) for _ in range(size)]
    draw_data(data)


# =========================
# DRAW GRAPH
# =========================

def draw_data(data):

    ax.clear()

    bars = ax.bar(range(len(data)), data)

    ax.set_title("Algorithm Visualizer")

    canvas.draw()


# =========================
# BUBBLE SORT
# =========================

def bubble_sort():

    arr = data.copy()

    def generator():

        for i in range(len(arr)):

            for j in range(len(arr)-i-1):

                if arr[j] > arr[j+1]:

                    arr[j],arr[j+1] = arr[j+1],arr[j]

                yield arr

    animate(generator())


# =========================
# INSERTION SORT
# =========================

def insertion_sort():

    arr = data.copy()

    def generator():

        for i in range(1,len(arr)):

            key = arr[i]
            j = i-1

            while j>=0 and arr[j] > key:

                arr[j+1] = arr[j]
                j -= 1
                yield arr

            arr[j+1] = key
            yield arr

    animate(generator())


# =========================
# SELECTION SORT
# =========================

def selection_sort():

    arr = data.copy()

    def generator():

        for i in range(len(arr)):

            min_idx = i

            for j in range(i+1,len(arr)):

                if arr[j] < arr[min_idx]:
                    min_idx = j

                yield arr

            arr[i],arr[min_idx] = arr[min_idx],arr[i]
            yield arr

    animate(generator())


# =========================
# HYBRID SORT
# =========================

def hybrid_sort():

    if len(data) <= 20:
        insertion_sort()
    else:
        selection_sort()


# =========================
# ANIMATION
# =========================

def animate(generator):

    def update(arr):

        ax.clear()
        ax.bar(range(len(arr)), arr)
        ax.set_title("Sorting Animation")

    animation.FuncAnimation(
        fig,
        update,
        frames=generator,
        interval=speed_scale.get(),
        repeat=False
    )

    canvas.draw()


# =========================
# GUI
# =========================

root = tk.Tk()
root.title("Algorithm Visualizer")

data = []

# controls
controls = tk.Frame(root)
controls.pack()

tk.Label(controls,text="Data Size").grid(row=0,column=0)

size_entry = tk.Entry(controls,width=5)
size_entry.insert(0,"30")
size_entry.grid(row=0,column=1)

tk.Button(
    controls,
    text="Generate Data",
    command=lambda: generate_data(int(size_entry.get()))
).grid(row=0,column=2)


# algorithm selector
algo_menu = ttk.Combobox(
    controls,
    values=[
        "Bubble Sort",
        "Insertion Sort",
        "Selection Sort",
        "Hybrid Sort"
    ]
)

algo_menu.grid(row=0,column=3)
algo_menu.current(0)


# speed control
tk.Label(controls,text="Speed").grid(row=0,column=4)

speed_scale = tk.Scale(
    controls,
    from_=10,
    to=500,
    orient=tk.HORIZONTAL
)

speed_scale.set(100)
speed_scale.grid(row=0,column=5)


# start button
def start_sort():

    algo = algo_menu.get()

    if algo == "Bubble Sort":
        bubble_sort()

    elif algo == "Insertion Sort":
        insertion_sort()

    elif algo == "Selection Sort":
        selection_sort()

    elif algo == "Hybrid Sort":
        hybrid_sort()


tk.Button(
    controls,
    text="Start Sorting",
    command=start_sort
).grid(row=0,column=6)


# matplotlib figure
fig, ax = plt.subplots()

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()