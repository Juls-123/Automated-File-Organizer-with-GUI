import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500*350")

def path():
    input_text = entry1.get()
    print(input_text)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="File arranger")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter path")
entry1.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Submit", command=path)
button.pack(pady=12, padx=10)

root.mainloop()