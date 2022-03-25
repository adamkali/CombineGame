class Node:
    
    def __init__(self):
        self.number = 0
        self.in_play = True
        
    def spawn(number: int) -> None:
        self.number = number
        
    def dormant() -> None:
        self.in_play = False
      
    def display(self) -> str:
        if self.number != 0:
            return str(self.number)
        return " "