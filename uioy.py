import os
from random import randint
from tkinter import Tk, Button, Label, Entry, messagebox, StringVar
from tkinter.filedialog import askopenfilename
import math
import random

def hello():
    result = "Привет!"
    output.set(result)
    
def generate():
    file_name = askopenfilename(defaultextension=".txt", filetypes=[("Text files", ".txt"), ("All files", "*.*")])
    if not file_name:
        messagebox.showinfo("Info", "Файл не выбран")
        return

    with open(file_name, 'w') as temp_file:
        for _ in range(10):
            temp_file.write(str(randint(1, 100)) + " ")
            
    with open(file_name, 'r') as temp_file:
        content = temp_file.read()
        output.set("Содержимое: " + content)
        number = list(map(int, content.split()))
        if number:
            average = sum(number) / len(number)
            output.set(output.get() + f"\nСр. значение: {average}")
        else:
            output.set(output.get() + "\nФайл пуст")

def rannum():
    a = [random.randint(1, 99) for i in range(10)]
    a.sort()
    max_num = max(a)
    min_num = min(a)
    result = f'max = {max_num}; min = {min_num}; sum = {sum(a)}'
    output.set(result)

def math_operations():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        
        results = [f'{a} + {b} = {a + b}',
                   f'{a} - {b} = {a - b}',
                   f'{a} * {b} = {a * b}']
        
        if b != 0:
            results.append(f'{a} / {b} = {a / b}')
        else:
            results.append("Деление на 0 невозможно")
        
        results.append(f'{a} ** {b} = {a ** b}')
        
        output.set("\n".join(results))
    except ValueError:
        output.set("Пожалуйста, введите действительные числа.")

root = Tk()
root.title("Ткинкер")
root.geometry("1000x400")

output = StringVar()
output_label = Label(root, textvariable=output, wraplength=400)
output_label.pack(pady=20)

Button(root, text="Генерировать числа", command=generate).pack(pady=5)
Button(root, text="Приветствовать", command=hello).pack(pady=5)
Button(root, text="Случайные числа", command=rannum).pack(pady=5)

Label(root, text="Первое число:").pack()
entry_a = Entry(root)
entry_a.pack(pady=5)

Label(root, text="Второе число:").pack()
entry_b = Entry(root)
entry_b.pack(pady=5)

Button(root, text="Выполнить математические операции", command=math_operations).pack(pady=20)
root.mainloop()