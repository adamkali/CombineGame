from node import Node

class Grid:
    
    def __init__(self) -> None:
        self.grid = [[ Node() for __ in range(7) ] for _ in range(7)]
    
    def get_index(
        self,
        row: int,
        column: int
    ) -> Node:
        return self.grid[row][column]
    
    def set_index(
        self,
        row: int,
        column: int,
        node: Node
    ) -> None:
        self.grid[row][column] = node
        
    @staticmethod
    def double(number: Node) -> None:
        number.number = number.number*2
    
    @staticmethod
    def quadruple(nubmer: Node) -> None:
        number.number = number.number*4
        
    @staticmethod
    def octuple(nubmer: Node) -> None:
        number.number = number.number*8    
    
    def collapse(self, row: int, colomn: int) -> None:
        node = self.get_index(row-1, column)
        if row == 0:
            return
        else:
            self.set_index(row, column, node)
            self.collapse(row-1, column)
        return
         
    def update(self):
        flag = True
        while flag:
            for i in range(7):
                for j in range(7):
                    left = Node()
                    right = Node()
                    down = Node()
                    center = self.get_index(i,j)

                    if j == 0:
                        left.dormant()
                    else:
                        left = self.get_index(i,j-1)
                    if j == 6:
                        right.dormant()
                    else:
                    right = self.get_index(i,j+1)
                    if i == 6:
                        down.dormant()
                    else:
                        down = self.get_index(i+1,j)

                    all_available = left.in_play and right.in_play and down.in_play
                    left_equal = left.number == center.number and left.number != 0 and center.number != 0
                    right_equal = right.number == center.number and right.number != 0 and center.number != 0
                    down_equal = down.number == center.number and down.number != 0 and center.number != 0
                    if all_available:
                        if (left_equal and right_equal and down_equal):
                            self.set_index(i,j-1, Node())
                            self.collapse(i,j-1)
                            self.set_index(i,j+1, Node())
                            self.collapse(i,j+1)
                            self.set_index(i+1,j, center)
                            self.set_index(i,j, center)
                            self.collapse(i,j)
                        elif left_equal and down_equal:
                            self.set_index(i,j-1, Node())
                            self.collapse(i,j-1)
                            self.set_index(i+1,j, center)
                            self.set_index(i,j, center)
                            self.collapse(i,j)
                        elif right_equal and down_equal:
                            self.set_index(i,j+1, Node())
                            self.collapse(i,j+1)
                            self.set_index(i+1,j, center)
                            self.set_index(i,j, center)
                            self.collapse(i,j)
                        elif down_equal:
                            self.set_index(i+1,j, center)
                            self.set_index(i,j, center)
                            self.collapse(i,j)
                    elif left.in_play and down.in_play and not right.in_play:
                        if left_equal and down_equal:
                            self.set_index(i,j-1, Node())
                            self.collapse(i,j-1)
                            self.set_index(i+1,j, center)
                            self.set_index(i,j, center)
                            self.collapse(i,j)
                        elif down_equal:
                            self.set_index(i+1,j, center)
                            self.set_index(i,j, center)
                            self.collapse(i,j)
                    elif right.in_play and down.in_play and not left.in_play:
                        if right_equal and down_equal:
                            self.set_index(i,j-1, Node())
                            self.collapse(i,j-1)
                            self.set_index(i+1,j, center)
                            self.set_index(i,j, center)
                            self.collapse(i,j)
                        elif down_equal:
                            self.set_index(i+1,j, center)
                            self.set_index(i,j, center)
                            self.collapse(i,j)
                    elif right.in_play and left.in_play and not down.in_play:
                        if right_equal:
                            self.set_index(i,j-1, Node())
                            self.collapse(i,j-1)
                            self.set_index(i,j, center)
                            self.set_index(i,j, center)
                            self.collapse(i,j)
                        elif down_equal:
                            self.set_index(i+1,j, center)
                            self.set_index(i,j, center)
                            self.collapse(i,j)
                                  
            
        
        
    def dropdown(
        self,
        number: Node,
        column: int
    ) -> bool:
        for row in range(7):
            if row == 6:
                self.set_index(row, column, number)
                return True
            if row <= 6:
                next_node = self.get_index(row, column)
                
                if next_node.number != 0:
                    self.set_index(row, column, number)
                    return True
                if next_node.number != 0 and row == 0:
                    return False
                                       
    def are_moves_available(self, node: Node) -> bool:
        for colum in range(7):
            check = self.get_index(0, column)
            if check.number != 0 and check.number != node.number:
                return False
            elif check.number != 0 and check.number == node.number:
                return True
        return True
            
    def get_points(self) -> int:
        temp = 0
        for i in range(7):
            for j in range(7):
                temp += self.get_index(i,j).number
        return temp