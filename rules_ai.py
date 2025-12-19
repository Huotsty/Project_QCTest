"""
rules_ai.py - Classical rule-based AI with heuristic strategy
"""
import random

class RuleBasedAI:
    """Classical heuristic AI for Go."""
    
    def __init__(self, game_state):
        self.game_state = game_state
        self.player = 2  # RULES_AI
    
    def choose_move(self):
        """
        Choose move based on heuristics:
        1. Maximize liberties
        2. Block opponent
        3. Increase connectivity
        Returns: (row, col, rationale) or (None, None, "Pass")
        """
        legal_moves = self.game_state.get_legal_moves()
        
        if not legal_moves:
            return None, None, "No legal moves available - Pass"
        
        # Score each move
        move_scores = []
        for row, col in legal_moves:
            score = self.evaluate_move(row, col)
            move_scores.append((score, row, col))
        
        # Sort by score (descending)
        move_scores.sort(reverse=True)
        
        best_score, best_row, best_col = move_scores[0]
        
        # Generate rationale
        rationale = self.generate_rationale(best_row, best_col, best_score)
        
        return best_row, best_col, rationale
    
    def evaluate_move(self, row, col):
        """Evaluate move quality based on heuristics."""
        score = 0
        
        # 1. Liberty count (more liberties = better)
        liberty_count = len([n for n in self.game_state.get_neighbors(row, col) 
                            if self.game_state.board[n[0]][n[1]] == 0])
        score += liberty_count * 3
        
        # 2. Block opponent (adjacent to enemy stones)
        opponent = 1 if self.player == 2 else 2  # ZIDAN_AI
        enemy_adjacent = 0
        for nr, nc in self.game_state.get_neighbors(row, col):
            if self.game_state.board[nr][nc] == opponent:
                enemy_adjacent += 1
        score += enemy_adjacent * 5
        
        # 3. Connectivity (adjacent to own stones)
        friendly_adjacent = 0
        for nr, nc in self.game_state.get_neighbors(row, col):
            if self.game_state.board[nr][nc] == self.player:
                friendly_adjacent += 1
        score += friendly_adjacent * 4
        
        # 4. Center control bonus
        center_distance = abs(row - 2) + abs(col - 2)
        score += (4 - center_distance) * 2
        
        # 5. Edge penalty (avoid edges unless necessary)
        if row == 0 or row == 4 or col == 0 or col == 4:
            score -= 2
        
        return score
    
    def generate_rationale(self, row, col, score):
        """Generate human-readable rationale for move."""
        reasons = []
        
        # Check liberties
        liberty_count = len([n for n in self.game_state.get_neighbors(row, col) 
                            if self.game_state.board[n[0]][n[1]] == 0])
        if liberty_count >= 3:
            reasons.append(f"high liberties ({liberty_count})")
        
        # Check blocking
        opponent = 1  # ZIDAN_AI
        enemy_adjacent = sum(1 for nr, nc in self.game_state.get_neighbors(row, col)
                            if self.game_state.board[nr][nc] == opponent)
        if enemy_adjacent > 0:
            reasons.append(f"blocks opponent ({enemy_adjacent} adj)")
        
        # Check connectivity
        friendly_adjacent = sum(1 for nr, nc in self.game_state.get_neighbors(row, col)
                               if self.game_state.board[nr][nc] == self.player)
        if friendly_adjacent > 0:
            reasons.append(f"connects stones ({friendly_adjacent} adj)")
        
        # Center control
        if abs(row - 2) + abs(col - 2) <= 2:
            reasons.append("center control")
        
        if reasons:
            rationale = f"Move ({row},{col}): " + ", ".join(reasons) + f" [score={score:.1f}]"
        else:
            rationale = f"Move ({row},{col}): strategic position [score={score:.1f}]"
        
        return rationale
