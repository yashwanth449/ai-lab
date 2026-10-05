class PuzzleState:
    def __init__(self, board, parent=None, move="", depth=0):
        # The board is represented as a 1D tuple of 9 elements for fast hashing
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth

    def get_blank_index(self):
        return self.board.index(0)

    def generate_neighbors(self):
        neighbors = []
        blank = self.get_blank_index()
        row, col = divmod(blank, 3)

        # Define valid moves for the blank space: (row_change, col_change, move_name)
        moves = [
            (-1, 0, "Up"),
            (1, 0, "Down"),
            (0, -1, "Left"),
            (0, 1, "Right")
        ]

        for dr, dc, move_name in moves:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_blank = new_row * 3 + new_col
                
                # Create a new board configuration by swapping
                new_board = list(self.board)
                new_board[blank], new_board[new_blank] = new_board[new_blank], new_board[blank]
                
                neighbors.append(PuzzleState(tuple(new_board), self, move_name, self.depth + 1))
        
        return neighbors

def solve_8_puzzle_dfs(start_board, goal_board, max_depth=20):
    start_state = PuzzleState(tuple(start_board))
    goal_tuple = tuple(goal_board)
    
    # Stack stores tuples of (current_state)
    stack = [start_state]
    
    # Visited dictionary keeps track of the minimum depth we reached a specific configuration
    visited = {start_state.board: 0}

    while stack:
        current = stack.pop()

        # Check if goal is reached
        if current.board == goal_tuple:
            return backtrack_path(current)

        # If we have reached the depth limit, do not expand neighbors further
        if current.depth >= max_depth:
            continue

        # Expand neighbors (reversed to preserve standard left-to-right exploration order when popped)
        for neighbor in reversed(current.generate_neighbors()):
            # Only explore if state hasn't been visited, or if found at a shallower depth
            if neighbor.board not in visited or neighbor.depth < visited[neighbor.board]:
                visited[neighbor.board] = neighbor.depth
                stack.append(neighbor)

    return None

def backtrack_path(state):
    path = []
    moves = []
    current = state
    while current is not None:
        path.append(current.board)
        if current.move:
            moves.append(current.move)
        current = current.parent
    return path[::-1], moves[::-1]

def print_grid(board):
    for i in range(0, 9, 3):
        print(f" {board[i]} {board[i+1]} {board[i+2]} ")
    print("-" * 11)

# --- Example Execution ---
if __name__ == "__main__":
    # 0 represents the blank space
    # Standard easy-to-solve initial state for demonstration (DFS struggles with highly scrambled states)
    initial_state = [
        1, 2, 3,
        4, 0, 6,
        7, 5, 8
    ]
    
    goal_state = [
        1, 2, 3,
        4, 5, 6,
        7, 8, 0
    ]

    print("Initial State:")
    print_grid(initial_state)

    print("Searching for solution via DFS (Depth Limit: 20)...")
    result = solve_8_puzzle_dfs(initial_state, goal_state, max_depth=20)

    if result:
        states, moves = result
        print(f"\n✅ Solution Found in {len(moves)} steps!")
        print("Sequence of moves:", " -> ".join(moves))
        print("\nStep-by-step states:")
        for idx, state in enumerate(states):
            print(f"Step {idx}:" if idx > 0 else "Start:")
            print_grid(state)
    else:
        print("\n❌ No solution found within the specified depth limit.")
