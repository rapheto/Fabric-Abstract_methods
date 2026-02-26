from abc import ABC, abstractmethod

#Define o que um botão deve fazer
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def on_click(self, callback):
        pass

# Tipos de botões
class WindowsButton(Button):
    def render(self):
        print("botão no Windows.")

    def on_click(self, callback):
        print("clique do botão Windows.")
        callback()

class HTMLButton(Button):
    def render(self):
        print("botão no HTML.")

    def on_click(self, callback):
        print("clique do botão HTML.")
        callback()


#Factory Method
class Dialog(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    def render(self):
        #Método fábrica
        ok_button = self.create_button()
        
        ok_button.on_click(self.close_dialog)
        ok_button.render()

    def close_dialog(self):
        print("fechando diálogo...")

#Criadores concretos sobrescrevem o método fábrica para mudar o tipo de produto resultante.
class WindowsDialog(Dialog):
    def create_button(self) -> Button:
        return WindowsButton()
class WebDialog(Dialog):
    def create_button(self) -> Button:
        return HTMLButton()


class Application:
    def __init__(self):
        self.dialog: Dialog = None

    def initialize(self):
        config = self.read_application_config_file()

        if config["OS"] == "Windows":
            self.dialog = WindowsDialog()
        elif config["OS"] == "Web":
            self.dialog = WebDialog()
        else:
            raise Exception("Error! Unknown operating system.")

    def read_application_config_file(self):
        return {"OS": "Windows"}  # Alterar para "Web" ou "Windows" para testar os botões

    def main(self):
        self.initialize()
        self.dialog.render()


if __name__ == "__main__":
    app = Application()
    app.main()