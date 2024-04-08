from abc import ABC, abstractmethod

# Strategy interface
class Strategy(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete strategies
class ConcreteStrategyA(Strategy):
    def execute(self):
        print("Executing strategy A")

class ConcreteStrategyB(Strategy):
    def execute(self):
        print("Executing strategy B")

# Context class using Template Method pattern
class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def template_method(self):
        self.before()
        self.strategy.execute()
        self.after()

    def before(self):
        print("Before executing strategy")

    def after(self):
        print("After executing strategy")

# Example usage
if __name__ == "__main__":
    strategy_a = ConcreteStrategyA()
    context = Context(strategy_a)
    context.template_method()

    strategy_b = ConcreteStrategyB()
    context = Context(strategy_b)
    context.template_method()
