import string
import random
import tkinter
import pyperclip
import customtkinter

def gen_pass():
    data.delete(0, customtkinter.END)
    if sel.get() == "Length":
        print(">>> Error Occured!")
        tkinter.messagebox.showerror("Error", "Choose the Length")
    else:
        len = int(sel.get())
        passwd = ""
        val = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
        for i in range(0, len):
                passwd = passwd + random.choice(val)
        data.insert(customtkinter.END, passwd)
        print(">>> Generated Password:", passwd)

def copy_pass():
    passwd = data.get()
    pyperclip.copy(passwd)
    print(">>> Password Copied Successfully!")
    tkinter.messagebox.showinfo("Copy", "Password Copied")

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

window = customtkinter.CTk()
window.geometry("420x220")
window.title("Random Password Generator")

fontdt = customtkinter.CTkFont('arial', 16, weight="bold")
lbl = customtkinter.CTkLabel(window, text="Choose Password Length", font=fontdt)
lbl.place(x=20, y=30)
var = customtkinter.StringVar(value="Length")
sel = customtkinter.CTkOptionMenu(window, values=["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"], font=fontdt, width=170, variable=var, corner_radius=5)
sel.place(x=230, y=30)
lbl2 = customtkinter.CTkLabel(window, text="Generated Password", font=fontdt)
lbl2.place(x=20, y=90)
data = customtkinter.CTkEntry(window, placeholder_text="Password", placeholder_text_color="lightgreen", width=200, fg_color=("#3B8ED0", "#1F6AA5"), text_color='lightgreen', font=fontdt, border_width=0, border_color=("#3E454A", "#949A9F"), corner_radius=5)
data.place(x=200, y=90)
btn = customtkinter.CTkButton(window, text="Generate Password", command=lambda: gen_pass(), font=fontdt, corner_radius=10)
btn.place(x=125, y=170, anchor=customtkinter.CENTER)
btn2 = customtkinter.CTkButton(window, text="Copy Password", command=lambda: copy_pass(), font=fontdt, corner_radius=10)
btn2.place(x=305, y=170, anchor=customtkinter.CENTER)

window.mainloop()