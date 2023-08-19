import os
import shutil
import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1000x500")
def path():

    pathinput = entry1.get()
    print(pathinput)

    files = os.listdir(pathinput)

    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]

        if os.path.exists(pathinput + '/' + extension):
            shutil.move(pathinput + '/' + file, pathinput + '/' + extension + '/' + file)
        else:
            os.makedirs(pathinput + '/' + extension)
            shutil.move(pathinput + '/' + file, pathinput + '/' + extension + '/' + file)


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="File arranger")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter path")
entry1.pack(pady=12, padx=80)

button = customtkinter.CTkButton(master=frame, text="Submit", command=path)
button.pack(pady=12, padx=10)

root.mainloop()


