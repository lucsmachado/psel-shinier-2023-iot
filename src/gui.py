from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import *

def user_allows_restart():
    prompt_answer = mb.askokcancel(
        title='Nova versão detectada', 
        message="Detectamos uma nova versão e seu programa será reiniciado. Deseja reiniciar agora?"
    )
    return prompt_answer

def center(w):
    """
    Centers a window on the screen.
    @param w: the window to be centered
    """
    w.eval('tk::PlaceWindow . center')

def render_gui():
    window = Tk()
    window.geometry('300x100')
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
        text="Cadastrar",
        command=handle_submit
    )
    btn_submit.pack()

    frm_name.pack()

    center(window)
    window.mainloop()

if __name__ == '__main__':
    render_gui()
