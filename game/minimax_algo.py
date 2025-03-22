from collections import Counter
from data_structurs import GameTreeNode

class MinimaxAI:
    def __init__(self, game_logic, max_depth=3):
        self.game_logic = game_logic
        self.max_depth = max_depth

    def getBestMove(self):
        print(f"Current Sequence: {self.game_logic.sequence}")  # for debug
        print(f"Current Scores: {self.game_logic.scores}")  # for debug
        print(f"Player Turn: {self.game_logic.player_turn}")  # for debug
        root = GameTreeNode(
            sequence = self.game_logic.sequence,
            scores = self.game_logic.scores,
            player_turn = self.game_logic.player_turn,
            depth = 0
        )

        root.generate_children(max_depth = self.max_depth)

        bestValue = -float('inf')
        bestMove = None

        for child in root.children:
            value = self._minimax(child, depth = 1, isMaximizing = False)
            if value > bestValue:
                bestValue = value
                bestMove = self._getMoveFromChild(root, child)

        print(f"Best Move: {bestMove}")
        return bestMove

    def _minimax(self, node, depth, isMaximizing):
        if depth == self.max_depth or not node.sequence:
            return self._evaluate(node)

        if isMaximizing:
            value = -float('inf')
            
            for child in node.children:
                value = max(value, self._minimax(child, depth + 1, False))
                
            return value
        else:
            value = float('inf')
            
            for child in node.children:
                value = min(value, self._minimax(child, depth + 1, True))
                
            return value

    def _evaluate(self, node):
        delta = node.scores[1] - node.scores[0]

        fourExists = 4 in node.sequence
        aN4 = 1 if fourExists else 0

        threeExists = 3 in node.sequence and not fourExists
        aN3 = 1 if threeExists else 0

        highestFigure = max(node.sequence) if node.sequence else 0
        aHighest = highestFigure

        twoExists = 2 in node.sequence and not (threeExists or fourExists)
        aN2 = 1 if twoExists else 0

        fN = delta + 0.5 * aN4 + 0.4 * aN3 + 0.3 * aHighest + 0.15 * aN2
        return fN

    def _getMoveFromChild(self, parent, child):
        parentCounts = Counter(parent.sequence)
        childCounts = Counter(child.sequence)
        
        for num in parentCounts:
            if parentCounts[num] == childCounts[num] + 1:
                for i in range(len(parent.sequence)):
                    if i >= len(child.sequence) or parent.sequence[i] != child.sequence[i]:
                        if parent.sequence[i] == num:
                            print(f"Move: Take number {num} at index {i}")  # for debug
                            return ("take", i)
        
        if childCounts[1] == parentCounts[1] + 2 and childCounts[2] == parentCounts[2] - 1:
            for i, num in enumerate(parent.sequence):
                if num == 2:
                    print(f"Move: Split number {num} at index {i}")  # for debug
                    return ("split", i)
        elif childCounts[2] == parentCounts[2] + 2 and childCounts[4] == parentCounts[4] - 1:
            for i, num in enumerate(parent.sequence):
                if num == 4:
                    print(f"Move: Split number {num} at index {i}")  # for debug
                    return ("split", i)
        
        print("No valid move found!")  # for debug
        return None  # Return None if no move is found         

    