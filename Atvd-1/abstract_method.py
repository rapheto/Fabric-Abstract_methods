from abc import ABC, abstractmethod
import platform

#Define botão e checkbox
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass
    
class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

#Produtos 
class WinButton(Button):
    def paint(self):
        print("botão Windows.")
class WinCheckbox(Checkbox):
    def paint(self):
        print("checkbox Windows.")

class MacButton(Button):
    def paint(self):
        print("botão macOS.")
class MacCheckbox(Checkbox):
    def paint(self):
        print("checkbox macOS.")

#Fábrica Abstrata
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass
    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


#Fábricas Concretas
class WinFactory(GUIFactory):
    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

class Application:
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.button = None
        self.checkbox = None

    def create_ui(self):
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()

    def paint(self):
        self.button.paint()
        self.checkbox.paint()

class ApplicationConfigurator:
    @staticmethod
    def main():
        os_name = platform.system()

        if os_name == "Windows":
            factory = WinFactory()
        elif os_name == "Darwin":
            factory = MacFactory()
        else:
            raise Exception("Error! Unknown operating system.")

        app = Application(factory)
        app.create_ui()
        app.paint()

if __name__ == "__main__":
    ApplicationConfigurator.main()