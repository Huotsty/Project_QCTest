"""
game.py - Core game logic and board helpers for 5x5 Quantum Go
"""
import copy

BOARD_SIZE = 5
EMPTY = 0
ZIDAN_AI = 1
RULES_AI = 2
HUMAN = 3

class GameState:
    """Manages the 5x5 Go board and game state."""
    
    def __init__(self, mode='A'):
        """
        Initialize game state.
        mode: 'A' (ZidanAI vs RuleBasedAI) or 'B' (Human vs ZidanAI)
        """
        self.board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.mode = mode
        self.turn_count = 0
        self.max_turns = 30
        self.consecutive_passes = 0
        self.game_log = []
        self.game_over = False
        self.winner = None
        
        # Current player
        if mode == 'A':
            self.current_player = ZIDAN_AI
            self.players = [ZIDAN_AI, RULES_AI]
        else:  # mode == 'B'
            self.current_player = HUMAN
            self.players = [HUMAN, ZIDAN_AI]
    
    def get_player_name(self, player):
        """Get readable name for player."""
        names = {
            EMPTY: "Empty",
            ZIDAN_AI: "ZidanAI",
            RULES_AI: "RuleBasedAI",
            HUMAN: "Human"
        }
        return names.get(player, "Unknown")
    
    def print_board(self):
        """Return string representation of board."""
        symbols = {EMPTY: '.', ZIDAN_AI: 'Z', RULES_AI: 'R', HUMAN: 'H'}
        lines = []
        lines.append("  " + " ".join(str(i) for i in range(BOARD_SIZE)))
        for r in range(BOARD_SIZE):
            row_str = str(r) + " " + " ".join(symbols[self.board[r][c]] for c in range(BOARD_SIZE))
            lines.append(row_str)
        return "\n".join(lines)
    
    def idx_to_rc(self, idx):
        """Convert linear index to (row, col)."""
        return (idx // BOARD_SIZE, idx % BOARD_SIZE)
    
    def rc_to_idx(self, row, col):
        """Convert (row, col) to linear index."""
        return row * BOARD_SIZE + col
    
    def is_legal(self, row, col):
        """Check if move is legal (within bounds and cell is empty)."""
        if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
            return False
        return self.board[row][col] == EMPTY
    
    def apply_move(self, row, col, player):
        """Apply move to board. Returns True if successful, False if illegal."""
        if not self.is_legal(row, col):
            return False
        self.board[row][col] = player
        self.consecutive_passes = 0
        return True
    
    def pass_turn(self):
        """Record a pass."""
        self.consecutive_passes += 1
    
    def get_legal_moves(self):
        """Return list of legal move (row, col) tuples."""
        moves = []
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                if self.is_legal(r, c):
                    moves.append((r, c))
        return moves
    
    def get_neighbors(self, row, col):
        """Get valid neighbor coordinates."""
        neighbors = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE:
                neighbors.append((nr, nc))
        return neighbors
    
    def count_liberties(self, row, col):
        """Count empty spaces (liberties) around a stone."""
        liberties = 0
        for nr, nc in self.get_neighbors(row, col):
            if self.board[nr][nc] == EMPTY:
                liberties += 1
        return liberties
    
    def get_group(self, row, col, player):
        """Get all connected stones of same player using BFS."""
        if self.board[row][col] != player:
            return []
        
        visited = set()
        group = []
        stack = [(row, col)]
        
        while stack:
            r, c = stack.pop()
            if (r, c) in visited:
                continue
            visited.add((r, c))
            group.append((r, c))
            
            for nr, nc in self.get_neighbors(r, c):
                if self.board[nr][nc] == player and (nr, nc) not in visited:
                    stack.append((nr, nc))
        
        return group
    
    def count_territory(self, player):
        """Count empty cells adjacent to player's stones."""
        territory = set()
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                if self.board[r][c] == player:
                    for nr, nc in self.get_neighbors(r, c):
                        if self.board[nr][nc] == EMPTY:
                            territory.add((nr, nc))
        return len(territory)
    
    def count_total_liberties(self, player):
        """Sum all liberties for player's stones."""
        total = 0
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                if self.board[r][c] == player:
                    total += self.count_liberties(r, c)
        return total
    
    def count_connectivity(self, player):
        """Count size of largest connected group."""
        visited = set()
        max_group = 0
        
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                if self.board[r][c] == player and (r, c) not in visited:
                    group = self.get_group(r, c, player)
                    for pos in group:
                        visited.add(pos)
                    max_group = max(max_group, len(group))
        
        return max_group
    
    def calculate_score(self, player):
        """Calculate total score for player."""
        territory = self.count_territory(player)
        liberties = self.count_total_liberties(player)
        connectivity = self.count_connectivity(player)
        
        # Weighted scoring
        score = territory * 2 + liberties + connectivity * 3
        return score
    
    def check_game_over(self):
        """Check if game should end."""
        if self.turn_count >= self.max_turns:
            self.game_over = True
            self.determine_winner()
            return True
        
        if self.consecutive_passes >= 2:
            self.game_over = True
            self.determine_winner()
            return True
        
        return False
    
    def determine_winner(self):
        """Determine winner based on scores."""
        if self.mode == 'A':
            score1 = self.calculate_score(ZIDAN_AI)
            score2 = self.calculate_score(RULES_AI)
            if score1 > score2:
                self.winner = "ZidanAI"
            elif score2 > score1:
                self.winner = "RuleBasedAI"
            else:
                self.winner = "Draw"
        else:  # mode == 'B'
            score1 = self.calculate_score(HUMAN)
            score2 = self.calculate_score(ZIDAN_AI)
            if score1 > score2:
                self.winner = "Human"
            elif score2 > score1:
                self.winner = "ZidanAI"
            else:
                self.winner = "Draw"
    
    def next_turn(self):
        """Advance to next player."""
        self.turn_count += 1
        current_idx = self.players.index(self.current_player)
        self.current_player = self.players[(current_idx + 1) % len(self.players)]
    
    def get_board_snapshot(self):
        """Return copy of current board state."""
        return copy.deepcopy(self.board)
