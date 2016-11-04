import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class StorkGui(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Stork")
        self.set_default_size(300,400)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                       spacing=2)
        self.add(vbox)

        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.NONE)
        self.stack.add_titled(self.get_setup_stack(), "set_up", "Set up")
        self.stack.add_titled(self.get_release_stack(), "release", "Release")

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(self.stack)

        vbox.pack_start(self.get_menu(), True, True, 0)
        vbox.pack_start(stack_switcher, True, True, 0)
        vbox.pack_start(self.stack, True, True, 0)

    def get_menu(self):
        main_menu = Gtk.MenuBar()

        file_menu = Gtk.Menu()
        file_menu_exit = Gtk.MenuItem("Exit")
        file_menu.append(file_menu_exit)

        file_menu_dropdown = Gtk.MenuItem("File")
        file_menu_dropdown.set_submenu(file_menu)

        pref_menu = Gtk.Menu()
        pref_menu_add_space = Gtk.MenuItem("Add space")
        pref_menu.append(pref_menu_add_space)

        pref_menu_dropdown = Gtk.MenuItem("Preferences")
        pref_menu_dropdown.set_submenu(pref_menu)

        return main_menu

    def get_setup_stack(self):
        stack_setup = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                       spacing=2)
        button_start = Gtk.Button("Start")
        button_start.connect("clicked", self.start)
        stack_setup.pack_start(button_start, True, True, 0)

        button_reset = Gtk.Button("Reset")
        button_reset.connect("clicked", self.reset)
        stack_setup.pack_start(button_reset, True, True, 0)
        
        return stack_setup

    def get_release_stack(self):
        stack_release = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                       spacing=2)

        self.tree_store = Gtk.TreeStore(str, str, str)
        top_row = self.tree_store.append(None, ('Top Level', '', ''))
        ip_row = self.tree_store.append(top_row, ('Ip Name','name','version'))
        self.tree_store.append(ip_row, ('Flow','RtlDesignFlow','Final'))
        self.tree_store.append(ip_row, ('Flow','Databahn','Final'))

        tree_view = Gtk.TreeView()
        tree_view.set_model(self.tree_store)
        tree_view.append_column(Gtk.TreeViewColumn('Tree',
                                                   Gtk.CellRendererText(),
                                                   text=0))
        tree_view.append_column(Gtk.TreeViewColumn('Value',
                                                   Gtk.CellRendererText(),
                                                   text=1))

        liststore_version = Gtk.ListStore(str)
        liststore_version.append(['Initial'])
        liststore_version.append(['Stable'])
        liststore_version.append(['Final'])

        renderer_combo = Gtk.CellRendererCombo()
        renderer_combo.set_property("editable", True)
        renderer_combo.set_property("model", liststore_version)
        renderer_combo.set_property("text-column", 0)
        renderer_combo.set_property("has-entry", False)
        renderer_combo.connect("edited", self.on_combo_changed)

        tree_view.append_column(Gtk.TreeViewColumn('Verision',
                                                   renderer_combo,
                                                   text=2))

        stack_release.pack_start(tree_view, True, True, 0)
        return stack_release

    def on_combo_changed(self, widget, path, text):
        self.tree_store[path][2] = text
        print(widget)
        print(path)
        print(text)

    def start(self, widget):
        print("Start ->")

    def reset(self, widget):
        print("Reset ->")
        self.stack.add_titled(self.get_release_stack(), "release_1", "Release")



def main():
    window = StorkGui()
    window.connect('delete-event', Gtk.main_quit)
    window.show_all()

    Gtk.main()

if __name__ == '__main__':
    main()