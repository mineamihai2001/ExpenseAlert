import tkinter
import customtkinter


def show(message="Error", title="Modal"):
    customtkinter.set_appearance_mode("system")
    customtkinter.set_default_color_theme("dark-blue")

    app = customtkinter.CTk()
    app.geometry("400x200")
    app.title(title)

    frame_1 = customtkinter.CTkFrame(master=app)
    frame_1.pack(pady=10, padx=12, fill="both", expand=True)

    label_1 = customtkinter.CTkLabel(
        master=frame_1, width=375, height=85, text=message,
        text_font=("Roboto", 11))
    label_1.pack(pady=10, padx=10)

    button = customtkinter.CTkButton(
        master=app, text="Ok", text_font=("Roboto", "12"))  # command=lambda app=app: quit(app)
    button.pack(pady=10, padx=10)
    app.mainloop()


def quit(app):
    app.destroy()
