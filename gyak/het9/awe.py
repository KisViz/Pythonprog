import time
import tkinter.simpledialog
import tkinter as tk
import htmllistparse

def load(tb):
    username=tkinter.simpledialog.askstring("h-s azonosító", "Hallgatói azonosító:")
    pw=tkinter.simpledialog.askstring("Jelszó", "Jelzó:", show="9")
    feladat=tkinter.simpledialog.askstring("feladat sorszáma", "sorszám:")
    try:
        cwd, list= htmllistparse.fetch_listing(f"https://biro2.inf.u-szeged.hu/Hallg/IB088g/{feladat}/{username}", timeout=30, auth=(username, pw))
        for e in list:
            if e.size is None:
                tb.insert(tk.END, f"{e.name.split('/')[0]}. feltöltésUndecidedn -Időpontja: {time.strftime('%Y-%m-%d T%H:%M:%SZ', e.modified)}\n")

    except Exception as e:
        print(e)



def main():
    win=tk.Tk()
    canvas = tk.Canvas(width=800, height=500, bg="#00ced1")
    canvas.grid(columnspan=2, rowspan=5)
    lbl=tk.Label(win, text="Bírós eredmények:", font=("Arial", 30, "bold"), bg="#00ced1")
    lbl.grid(columnspan=2, column=0, row=0) #elsővel összevontam, középre rakja
    tb=tk.Text(win, height=20, width=70, padx=10, pady=10)
    tb.grid(columnspan=2, row=2)
    btn=tk.Button(win, command=lambda:load(tb), text="Bíró betöltése", font="Arial 30 bold", bg="yellow")
    btn.grid(columnspan=2, column=0, row=3)

    win.mainloop()

if __name__=="__main__":
    main()