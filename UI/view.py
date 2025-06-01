import flet as ft


class View():
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None


    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App gestione studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name

        self._DDcorsi=ft.Dropdown(label="corso",width=600)

        # button for the "hello" reply
        self.btn_iscritti = ft.ElevatedButton(text="Cerca iscritti", on_click=self._controller.handle_iscritti)
        row1 = ft.Row([self._DDcorsi, self.btn_iscritti],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._controller.fillDDcorsi()
        self._page.controls.append(row1)

        self._txt_matricola=ft.TextField(label="matricola")
        self._txt_nome=ft.TextField(label="nome", read_only=True)
        self._txt_cognome=ft.TextField(label="cognome",read_only=True)

        row2=ft.Row([ self._txt_matricola,self._txt_nome,self._txt_cognome],alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self._btn_cercaStudente=ft.ElevatedButton(text="Cerca studente",on_click=self._controller.handle_studente)
        self._btn_cercaCorsi=ft.ElevatedButton(text="Cerca corsi", on_click=self._controller.handle_corsi)
        self._btn_iscrivi=ft.ElevatedButton(text="Iscrivi",on_click=self._controller.handle_iscritti)


        row3=ft.Row([ft.Container(self._btn_cercaStudente),ft.Container(self._btn_cercaCorsi),ft.Container(self._btn_iscrivi)],alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
