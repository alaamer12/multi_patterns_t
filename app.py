from abc import ABC, abstractmethod

# Abstract class defining the template method
class AbstractClass(ABC):
    def template_method(self):
        self.base_operation1()
        self.required_operation1()
        self.base_operation2()
        self.hook1()
        self.required_operation2()
        self.base_operation3()
        self.hook2()

    # Base operations
    def base_operation1(self):
        print("AbstractClass: Base operation 1 is done")

    def base_operation2(self):
        print("AbstractClass: Base operation 2 is done")

    def base_operation3(self):
        print("AbstractClass: Base operation 3 is done")

    # Abstract methods
    @abstractmethod
    def required_operation1(self):
        pass

    @abstractmethod
    def required_operation2(self):
        pass

    # Hooks
    def hook1(self):
        pass

    def hook2(self):
        pass

# ConcreteClass1 implementing AbstractClass
class ConcreteClass1(AbstractClass):
    def required_operation1(self):
        print("ConcreteClass1: Required operation 1 is implemented")

    def required_operation2(self):
        print("ConcreteClass1: Required operation 2 is implemented")

    def hook2(self):
        print("ConcreteClass1: Hook 2 is implemented")

# ConcreteClass2 implementing AbstractClass
class ConcreteClass2(AbstractClass):
    def required_operation1(self):
        print("ConcreteClass2: Required operation 1 is implemented")

    def required_operation2(self):
        print("ConcreteClass2: Required operation 2 is implemented")

    def hook1(self):
        print("ConcreteClass2: Hook 1 is implemented")

# Client code
def client_code(abstract_class: AbstractClass):
    abstract_class.template_method()

if __name__ == "__main__":
    print("Client: Using ConcreteClass1:")
    concrete_class1 = ConcreteClass1()
    client_code(concrete_class1)

    print("\nClient: Using ConcreteClass2:")
    concrete_class2 = ConcreteClass2()
    client_code(concrete_class2)
