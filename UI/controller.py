import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self,e):
        distanza_minima = self._view._txtIn.value
        try:
            float(distanza_minima)
        except ValueError:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Per favore inserisci un valore numero per la distanza minima."))
            self._view.update_page()
            return

        self._view._txt_result.controls.clear()
        self._model.crea_grafo(float(distanza_minima))
        self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato!"))
        self._view._txt_result.controls.append(ft.Text(f"Numero di nodi: {self._model.getNumNodes()}"))
        self._view._txt_result.controls.append(ft.Text(f"Numero di archi: {self._model.getNumEdges()}"))

        self._view._txt_result.controls.append(ft.Text(""))
        allEdges = self._model.getAllEdges()
        for e in allEdges:
            self._view._txt_result.controls.append(ft.Text(f"{e[0]} -> {e[1]}    ---     Distanza media: {self._model.getDistMedia(e[0], e[1])}"))
        self._view.update_page()

