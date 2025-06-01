import flet as ft
from model.studente import Studente

from model import corso


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_iscritti(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        corso = self._view._DDcorsi.value



        if corso is None or corso == "":
            self._view.txt_result.clean()
            self._view.txt_result.controls.append(ft.Text("Selezionare un corso",color="red"))
            self._view.update_page()
            return
        studenti=self._model.getIscrittiCorsi(corso)
        self._view.txt_result.clean()
        self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(studenti)} iscritti al corso"))
        for studente in studenti:
            self._view.txt_result.controls.append(ft.Text(studente))
        self._view.update_page()
        # print(self._view._txt_matricola.value)
        # Studente= self._model.getStudente (self._view._txt_matricola.value)
        # print(Studente)
        # self._view._txt_nome.value(ft.Text(f"{Studente.nome} "))
        # self._view._txt_cognome.value(ft.Text(f"{Studente.cognome} "))


    # def fillDDcorsi(self):
    #     corsi=self._model.getCorsi()
    #     options = [
    #         ft.Dropdown.options(key=corso.codins, text=str(corso), data=corso)
    #         for corso in corsi
    #     ]
    #     self._view._DDcorsi.options= corsi
    #     self._view.update_page()

    def handle_studente(self,e):
        studente = self._model.getStudente(self._view._txt_matricola.value)
        if studente is None:
            self._view.txt_result.clean()
            self._view.txt_result.controls.append(ft.Text("Selezionare una matricola esistente",color="red"))
            self._view.update_page()
            return
        self._view._txt_nome.value=(f"{studente.nome} ")
        self._view._txt_cognome.value=(f"{studente.cognome} ")
        self._view.update_page()


    def fillDDcorsi(self):
        corsi = self._model.getCorsi()

        options = [
            ft.DropdownOption(key=corso.codins,text=corso.__str__()) #text=str(corso))
            for corso in corsi
        ]

        self._view._DDcorsi.options = options
        self._view.update_page()

    def handle_corsi(self,e):
        studente1 = self._model.getStudente(self._view._txt_matricola.value)
        if studente1 is None:
            self._view.txt_result.clean()
            self._view.txt_result.controls.append(ft.Text("Selezionare una matricola esistente", color="red"))
            self._view.update_page()
            return
        corsi = self._model.getCorsiperStudente(self._view._txt_matricola.value)
        self._view.txt_result.clean()
        self._view.txt_result.controls.append(ft.Text(f"Risultano {len(corsi)} corsi"))
        for corso in corsi:
            self._view.txt_result.controls.append(ft.Text(corso))
        self._view.update_page()
