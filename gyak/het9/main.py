import time
import tkinter as tk
import tkinter.simpledialog
import htmllistparse

def load(tb):
    username = tkinter.simpledialog.askstring("h-s azonosító", "Hallgatói azonosító:")
    pw = tkinter.simpledialog.askstring("Jelszó", "Jelszó:", show="*")
    feladat = tkinter.simpledialog.askstring("Feladat sorszáma", "Feladat sorszáma:")
    try:
        cwd, l= htmllistparse.fetch_listing(f"https://biro2.inf.u-szeged.hu/Hallg/IB088g/{feladat}/{username}", timeout=30, auth=(username, pw))
        for e in l:
            if e.size is None: #aakor mappa ha nncs merete
                tb.insert(tk.END, f"{e.name.split('/')[0]}. feltöltésUndecidedn -Időpontja: {time.strftime('%Y-%m-%d T%H:%M:%SZ', e.modified)}\n")



    except Exception as e:
        print(e)

def main():
    win = tk.Tk()
    canvas = tk.Canvas(width=800, height=500, bg='pink')
    canvas.grid(columnspan = 2, rowspan = 5)
    lbl = tk.Label(win, text="Bírós eredmények", font=("arial", 30, "bold"), bg='pink')
    lbl.grid(columnspan = 2,column=0, row=0)
    tb = tk.Text(win, height=20, width=70, padx=10, pady=10)
    tb.grid(columnspan = 2, row=2)
    btn = tk.Button(win, command=lambda:load(tb), text="Öld meg a csirkét", font=("arial", 30, "bold"), bg='purple')
    btn.grid(columnspan = 2,column=0, row=3)
    win.mainloop()

if __name__ == "__main__":
    main()