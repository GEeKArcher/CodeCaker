import tkinter as tk

class FooterBar(tk.Frame):
    def __init__(self, master=None, **options):
        tk.Frame.__init__(self, master, **options)
        self.lines = tk.Label(self, text='Lines: ', relief='sunken', border=1, padx=10)
        self.lines.pack(side='left')
        self.chars = tk.Label(self, text='Chars: ', relief='sunken', border=1, padx=10)
        self.chars.pack(side='left')

    def set(self, mouse_pos):
        self.lines['text'] = 'Line: ' + mouse_pos.split('.')[0]
        self.chars['text'] = 'Charater: ' + mouse_pos.split('.')[1]

def run():
    master = tk.Tk()
    text = tk.Text(master)
    text.pack(expand=True, fill='both')
    text.bind('<KeyRelease>', lambda e: footer.set(text.index('current')))
    # nota que estou a usar <KeyRelease>
    footer = FooterBar(master, background='#eee')
    footer.pack(fill='x')
    master.mainloop()

if __name__ == '__main__':
    run()