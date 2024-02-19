from abc import ABC, abstractmethod

# AbstractFactory interface
class AbstractFactory(ABC):
    @abstractmethod
    def create_panel(self):
        pass

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_textbox(self):
        pass

# Concrete Factory for Word90 generation
class Word90Factory(AbstractFactory):
    def create_panel(self):
        return "Panel Word90"

    def create_button(self):
        return "Button Word90"

    def create_textbox(self):
        return "Textbox Word90"

# Concrete Factory for Word00 generation
class Word00Factory(AbstractFactory):
    def create_panel(self):
        return "Panel Word00"

    def create_button(self):
        return "Button Word00"

    def create_textbox(self):
        return "Textbox Word00"

# Concrete Factory for Word10 generation
class Word10Factory(AbstractFactory):
    def create_panel(self):
        return "Panel Word10"

    def create_button(self):
        return "Button Word10"

    def create_textbox(self):
        return "Textbox Word10"

# Concrete Factory for Word24 generation
class Word24Factory(AbstractFactory):
    def create_panel(self):
        return "Panel Word24"

    def create_button(self):
        return "Button Word24"

    def create_textbox(self):
        return "Textbox Word24"

# SingletonRegistry class
class SingletonRegistry:
    _instances = {}
    
    @classmethod
    def get_instance(cls, factory_type):
        if cls._instances.get(factory_type, 0) < 2:
            cls._instances[factory_type] = cls._instances.get(factory_type, 0) + 1
            if factory_type == "Word90":
                return Word90Factory()
            elif factory_type == "Word00":
                return Word00Factory()
            elif factory_type == "Word10":
                return Word10Factory()
            elif factory_type == "Word24":
                return Word24Factory()
        else:
            print(f"Warning: {factory_type} instance requested more than twice.")
            return None

# Client code to run tests based on config
def run_tests(configurations):
    for generation in configurations:
        factory = SingletonRegistry.get_instance(generation)
        if factory:
            print(factory.create_panel())
            print(factory.create_button())
            print(factory.create_textbox())

# Configuration list simulating config file
configurations = [
    "Word90",
    "Word00",
    "Word90",
    "Word24",
    "Word10",
    "Word10",
    "Word00",
    "Word24",
    "Word90",
    "Word00"
]

# Run tests based on configurations hard coded above
run_tests(configurations)
