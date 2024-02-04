try:
    from tkinter import *
    import tkinter
    import webbrowser
    from random import randrange
    import random
    from tkinter import *
except ValueError as e:
    print(f"Error: {e}")


def open_domain(domain):
    webbrowser.open_new("https://www.%s.com" % domain)


def mdp():
    password = input("Quel est le mot de passe ? : ")
    if password == "" or password == "cherche !":
        pass
    else:
        print("Le mot de passe n'est pas valide ! ")
        mdp()


def on_return(event):
    entry = event.widget
    input_value = entry.get()
    #print("valeur: %s" % input_value)
    entry.delete(0, len(entry.get()))
    open_domain(input_value)

def main():
    # creer la couleur
    choice = "0"
    if choice == "0":
        color = '#5E74AF'
    else:
        color = '#41B77F'

    # fenetre
    window = Tk()

    # creer les frames
    frame = Frame(window, bg=color, bd=0)
    frame_two = Frame(frame, bg='black', bd=5)

    # personnaliser cette fenetre
    window.title("Mon moteur de recherche")
    #screen_width = window.winfo_screenwidth()
    #screen_height = window.winfo_screenheight()
    #print("%dx%0.0f" % (screen_width, screen_height))
    #window.geometry("%dx%0.0f+0+0" % (screen_width, screen_height - 68))
    window.geometry("1051x650")
    window.minsize(809, 500)
    window.config(background=color)

    # ajouter un premeir texte
    label_title = Label(window, text="Bienvenue dans ce moteur de recherche fait par Max",
                        font=("Lucida Handwriting", 24), bg=color, fg='white')
    label_title.pack(side=TOP)

    # ajouter un deuxieme texte
    label_title_two = Label(frame, text="""Vous pouvez cherchez ce que vous voulez tant que ce que vous""",
                            font=("Source Code Pro ExtraLight", 19), bg=color, fg='white')
    label_title_two.pack(expand=YES, side=TOP)

    # ajouter un deuxieme texte
    label_title_two = Label(frame, text="""chercher est un site sécuriser et que ça termine par ".com" """,
                            font=("Source Code Pro ExtraLight", 19), bg=color, fg='white')
    label_title_two.pack(expand=YES, side=TOP)

    # ajout d un bouton exit
    ext_button = Button(window, text="exit", font=("Source Code Pro ExtraLight", 13), bg='white', fg='black', command=exit)
    ext_button.pack(side=BOTTOM)

    # entrée
    value = StringVar()
    value.set("texte par défaut")
    entree = Entry(frame_two, textvariable=str, width=65, bd=5)
    entree.pack()

    # position des frames
    frame_two.pack(side=TOP)
    frame.pack(expand=YES)

    # réagir au changement du texte
    entree.bind("<Return>", on_return)

    # afficher
    window.mainloop()


if __name__ == '__main__':
    mdp()
    main()


