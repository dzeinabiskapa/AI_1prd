class GameTreeNode:
    """Represents a node in the game tree."""
    def __init__(self, sequence, scores, player_turn, parent=None, depth=0):
        self.sequence = sequence  # Current number sequence
        self.scores = scores  # [Player 1 score, Player 2 score]
        self.player_turn = player_turn  # 0 for P1, 1 for P2
        self.children = []
        self.parent = parent
        self.depth = depth  # Track depth level

    def generate_children(self, max_depth=3):
        """Generates possible moves for both players up to max_depth."""
        if self.depth >= max_depth:  # Stop generating beyond max_depth
            return

        for i, num in enumerate(self.sequence):
            # Copy game state
            new_sequence = self.sequence[:i] + self.sequence[i+1:]
            new_scores = self.scores[:]
            new_scores[self.player_turn] += num  # Taking the number

            # Create a child node for taking the number
            child_node = GameTreeNode(new_sequence, new_scores, 1 - self.player_turn, self, self.depth + 1)
            self.children.append(child_node)
            child_node.generate_children(max_depth)  # Continue recursion

            # Handle splitting rules
            if num == 2:
                split_sequence = self.sequence[:i] + [1, 1] + self.sequence[i+1:]
                split_node = GameTreeNode(split_sequence, new_scores, 1 - self.player_turn, self, self.depth + 1)
                self.children.append(split_node)
                split_node.generate_children(max_depth)

            if num == 4:
                split_sequence = self.sequence[:i] + [2, 2] + self.sequence[i+1:]
                split_scores = new_scores[:]
                split_scores[self.player_turn] += 1  # Gain 1 extra point for splitting 4
                split_node = GameTreeNode(split_sequence, split_scores, 1 - self.player_turn, self, self.depth + 1)
                self.children.append(split_node)
                split_node.generate_children(max_depth)

    #def print_tree(self, depth=0):
    #    """Prints the game tree recursively for debugging."""
    #    print(" " * depth * 4, f"Player {self.player_turn + 1}, Scores: {self.scores}, Sequence: {self.sequence}")
    #    for child in self.children:
    #        child.print_tree(depth + 1)

def generate_full_game_tree(initial_sequence, max_depth=3):
    """Creates the full game tree up to a limited depth and prints it."""
    print(f"Initial Sequence: {initial_sequence}")  # Print the starting sequence
    root = GameTreeNode(initial_sequence, [0, 0], 0, depth=0)  # Start with Player 1
    root.generate_children(max_depth=max_depth)  # Generate full tree up to max_depth
    #root.print_tree()  # Print the tree
    
