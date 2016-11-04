from tkinter import ttk
import tkinter as tk

class MainWindow:

    def __init__(self):
        self.root = tk.Tk()
        self.root.minsize(width=200, height=300)
    
        self.add_menu()
        self.add_notebook()
        self.add_tree()

    def run(self):
        self.root.mainloop()

    def do_nothing(self):
        print('do nothing')
    
    def add_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
    
        file_menu = tk.Menu(self.root)
        menu.add_cascade(label='File',
                         menu=file_menu)
        file_menu.add_command(label='Save state',
                              command=self.do_nothing)
        file_menu.add_separator()
        file_menu.add_command(label='Exit',
                              command=self.do_nothing)
    
        preference_menu = tk.Menu(self.root)
        menu.add_cascade(label='Preferences',
                         menu=preference_menu)
        preference_menu.add_command(label='editor',
                                    command=self.do_nothing)
        preference_menu.add_command(label='add_tab',
                                    command=self.add_tab)
        preference_menu.add_command(label='del_tab',
                                    command=self.del_tab)
        preference_menu.add_command(label='add_tree',
                                    command=self.add_tree)

    def add_notebook(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack()

    def add_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame,
                          text='Release')
        label = tk.Label(frame, text="stork2")
        label.pack()

    def del_tab(self):
        count = self.notebook.index(tab_id='end')
        print(count)
        if count:
            self.notebook.forget(tab_id=count-1)

    def add_tree(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='Setup')

        tree = ttk.Treeview(frame,
                            columns=('name', 'version'))
        tree.column('name',
                    width=100,
                    anchor='center')
        tree.heading('name', text='Name')
        tree.column('version', width=100, anchor='center')
        tree.heading('version', text='Nersion')

        top_id = tree.insert('', '0', text='top_dir', values=('str'), tags=('top_dir',))
        ip_id = tree.insert(top_id, 'end', text='ip_nme', values=('name version'))
        tree.insert(ip_id, '0', text='flow', values=('RTL Final'))
        tree.insert(ip_id, '1', text='flow', values=('Databan Final'))

        tree.tag_configure('top_dir', background='red')
        tree.pack()
        self.notebook.pack()

    def edit_satrt(self):
        pass

def main():
    main_window = MainWindow()
    main_window.run()

if __name__ == '__main__':
    main()