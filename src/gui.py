from tkinter import *
from tkinter.ttk import *

def render_gui():
    window = Tk()
    window.title("Processo Seletivo Shinier 2023")

    frm_name = Frame()

    lbl_name = Label(master=frm_name, text="Nome:")
    lbl_name.pack()

    lbl_candidate = Label(master=frm_name)

    ent_name = Entry(master=frm_name)
    ent_name.pack()

    def handle_submit():
        name = ent_name.get()
        ent_name.delete(0, END)
        lbl_candidate["text"] = "Candidato processo seletivo Shinier Iot: " + name
        lbl_candidate.pack()

    btn_submit = Button(
        master=frm_name,
        text="Click me",
        command=handle_submit
    )
    btn_submit.pack()

    frm_name.pack()

    window.mainloop()

if __name__ == '__main__':
    render_gui()
