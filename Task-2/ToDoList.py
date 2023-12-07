import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)

def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)

def edit_task():
    selected_task = listbox.curselection()
    if selected_task:
       
        current_task = listbox.get(selected_task)
        
        edit_window = tk.Toplevel(harshik)
        edit_window.title("Edit Task")
        
        edit_entry = tk.Entry(edit_window, width=30)
        edit_entry.insert(tk.END, current_task)
        edit_entry.pack(pady=10)
        
       
        def update_task():
            new_task = edit_entry.get()
            if new_task:
                
                listbox.delete(selected_task)
                
                listbox.insert(selected_task, new_task)
               
                edit_window.destroy()

        update_button = tk.Button(edit_window, text="Update", command=update_task)
        update_button.pack(pady=5)

harshik = tk.Tk()
harshik.title("To-Do List")
harshik.configure(bg="blue")

entry = tk.Entry(harshik, width=30)
entry.pack(pady=10)

add_button = tk.Button(harshik, text="Add", command=add_task)
add_button.pack(pady=5)

listbox = tk.Listbox(harshik, selectmode=tk.SINGLE, width=30, height=10)
listbox.pack(pady=10)

delete_button = tk.Button(harshik, text="Delete", command=delete_task)
delete_button.pack(pady=5)

edit_button = tk.Button(harshik, text="Edit", command=edit_task)
edit_button.pack(pady=5)

harshik.mainloop()
