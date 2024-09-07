import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import calendar

def click_button(value):
    current_text = calc_display.get()
    if current_text == "0" and value.isdigit():
        calc_display.delete(0, tk.END)
        calc_display.insert(tk.END, value)
    else:
        calc_display.insert(tk.END, value)

def clear_display():
    calc_display.delete(0, tk.END)
    calc_display.insert(0, "0")

def calculate_result():
    try:
        expression = calc_display.get()
        expression = expression.replace('×', '*').replace('÷', '/')
        result = eval(expression)
        calc_display.delete(0, tk.END)
        calc_display.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalido")
        calc_display.delete(0, tk.END)
        calc_display.insert(tk.END, "0")


def add_event():
    event = event_entry.get()
    if event:
        agenda_listbox.insert(tk.END, event)
        event_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Evento no esta vacio")

def delete_event():
    try:
        selected_event_index = agenda_listbox.curselection()[0]
        agenda_listbox.delete(selected_event_index)
    except IndexError:
        messagebox.showwarning("OJOO", "NO AHI UN EVENTO SELECCIONADOOOO")

# Función para actualizar el reloj
def update_clock():
    now = datetime.now()
    time_str = now.strftime("%I:%M %p")
    clock_label.config(text=time_str)
    clock_label.after(1000, update_clock)  # Actualizar cada segundo

# Función para mostrar el calendario
def show_calendar():
    try:
        year = int(year_spinbox.get())
        month = int(month_spinbox.get())
        cal = calendar.month(year, month)
        calendar_text.config(state=tk.NORMAL)
        calendar_text.delete(1.0, tk.END)
        calendar_text.insert(tk.END, cal)
        calendar_text.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Error", "Año invalido")

# Crear la ventana principal
root = tk.Tk()
root.title("Escritorio")

# Crear la calculadora
calc_frame = tk.Frame(root)
calc_frame.pack(pady=10)

calc_display = tk.Entry(calc_frame, width=20, font=('Arial', 18), borderwidth=2, relief="solid")
calc_display.grid(row=0, column=0, columnspan=4)
calc_display.insert(0, "0")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('÷', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('×', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0, 4)
]

for button in buttons:
    if len(button) == 4:
        text, row, col, colspan = button
        if text == '=':
            b = tk.Button(calc_frame, text=text, command=calculate_result)
        elif text == 'C':
            b = tk.Button(calc_frame, text=text, command=clear_display)
        else:
            b = tk.Button(calc_frame, text=text, command=lambda t=text: click_button(t))
        b.grid(row=row, column=col, columnspan=colspan, sticky="nsew")
    elif len(button) == 3:
        text, row, col = button
        b = tk.Button(calc_frame, text=text, command=lambda t=text: click_button(t))
        b.grid(row=row, column=col, sticky="nsew")

# Crear la agenda
agenda_frame = tk.Frame(root)
agenda_frame.pack(pady=10)

agenda_listbox = tk.Listbox(agenda_frame, width=50, height=10)
agenda_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(agenda_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
agenda_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=agenda_listbox.yview)

event_entry = tk.Entry(root, width=50)
event_entry.pack(pady=5)

add_button = tk.Button(root, text="Añadir evento", command=add_event)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Borrar evento", command=delete_event)
delete_button.pack(pady=5)

# Crear el reloj
clock_frame = tk.Frame(root)
clock_frame.pack(pady=10)

clock_label = tk.Label(clock_frame, font=('Arial', 40))
clock_label.pack()
update_clock()

# Crear el calendario
calendar_frame = tk.Frame(root)
calendar_frame.pack(pady=10)

year_spinbox = tk.Spinbox(calendar_frame, from_=1900, to=2100, width=4)
year_spinbox.grid(row=0, column=0, padx=5)
year_spinbox.delete(0, tk.END)
year_spinbox.insert(0, "2024")

month_spinbox = tk.Spinbox(calendar_frame, from_=1, to=12, width=2)
month_spinbox.grid(row=0, column=1, padx=5)
month_spinbox.delete(0, tk.END)
month_spinbox.insert(0, "9")

show_cal_button = tk.Button(calendar_frame, text="Mostrar calendario", command=show_calendar)
show_cal_button.grid(row=0, column=2, padx=5)

calendar_text = tk.Text(calendar_frame, width=20, height=8, state=tk.DISABLED)
calendar_text.grid(row=1, column=0, columnspan=3)

# Ajustar el tamaño de las filas y columnas
for frame in [calc_frame, agenda_frame, clock_frame, calendar_frame]:
    for i in range(5):
        frame.grid_rowconfigure(i, weight=1)
    for i in range(4):
        frame.grid_columnconfigure(i, weight=1)

root.mainloop()







