class EightPuzzleDFS:
    def __init__(self, start_state, goal_state):
        self.start_state = tuple(start_state)
        self.goal_state = tuple(goal_state)
        self.moves = {
            'Up': -3,
            'Down': 3,
            'Left': -1,
            'Right': 1
        }

    def get_valid_moves(self, state):
        """Finds all valid adjacent states and the actions that lead to them."""
        blank_idx = state.index(0)
        row, col = divmod(blank_idx, 3)
        valid_neighbors = []

        for move_name, shift in self.moves.items():
            new_idx = blank_idx + shift
            
            # Boundary checks for 3x3 grid transitions
            if 0 <= new_idx < 9:
                new_row, new_col = divmod(new_idx, 3)
                # Prevent horizontal wrapping (e.g., index 2 to 3 via 'Right')
                if abs(row - new_row) + abs(col - new_col) == 1:
                    # Create new state configuration
                    new_state = list(state)
                    new_state[blank_idx], new_state[new_idx] = new_state[new_idx], new_state[blank_idx]
                    valid_neighbors.append((tuple(new_state), move_name))
                    
        return valid_neighbors

    def solve(self, max_depth=20):
        """Executes Depth-First Search up to a specified maximum depth boundary."""
        # Stack stores tuples of: (current_state, path_taken, visited_set_at_this_branch)
        stack = [(self.start_state, [], {self.start_state})]
        
        while stack:
            state, path, visited = stack.pop()
            
            if state == self.goal_state:
                return path
                
            if len(path) >= max_depth:
                continue
                
            # Explore moves (reversed to preserve standard evaluation order when popping)
            for next_state, move in reversed(self.get_valid_moves(state)):
                if next_state not in visited:
                    new_visited = visited.copy()
                    new_visited.add(next_state)
                    stack.append((next_state, path + [move], new_visited))
                    
        return None

def print_board(state):
    """Utility to print the board configuration cleanly."""
    for i in range(0, 9, 3):
        print(f"[ {state[i]} {state[i+1]} {state[i+2]} ]")
    print()

# --- Example Execution ---
if __name__ == "__main__":
    # 0 represents the empty space tile
    # A simple initial state reachable within a short depth bound
    initial = (1, 2, 3, 
               4, 0, 5, 
               7, 8, 6)
               
    goal    = (1, 2, 3, 
               4, 5, 6, 
               7, 8, 0)

    print("--- Initial State ---")
    print_board(initial)
    
    print("--- Goal State ---")
    print_board(goal)

    solver = EightPuzzleDFS(initial, goal)
    solution_path = solver.solve(max_depth=15)

    if solution_path is not None:
        print(f"Success! Solution found in {len(solution_path)} moves.")
        print(f"Path sequence: {' -> '.join(solution_path)}")
    else:
        print("Failed to find a solution within the maximum depth limit.")
