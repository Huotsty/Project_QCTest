"""
Test Mode B (Human vs ZidanAI) logic without running the full app
"""
from game import GameState, HUMAN, ZIDAN_AI

print("Testing Mode B Logic...")
print("=" * 50)

# Test 1: Initialize Mode B game
print("\n1. Testing Mode B initialization...")
game = GameState(mode='B')
print(f"✓ Game initialized")
print(f"  Mode: {game.mode}")
print(f"  Current player: {game.get_player_name(game.current_player)}")
print(f"  Expected: Human")
assert game.mode == 'B'
assert game.current_player == HUMAN
print("✓ Mode B starts with Human player")

# Test 2: Human can make a move
print("\n2. Testing human move...")
legal_moves = game.get_legal_moves()
print(f"  Legal moves available: {len(legal_moves)}")
assert len(legal_moves) == 25  # All cells empty at start

# Make human move at center
success = game.apply_move(2, 2, HUMAN)
print(f"  Human plays at (2,2): {success}")
assert success == True
print(f"✓ Human move applied successfully")

# Test 3: Check board state
print("\n3. Testing board state...")
print(game.print_board())
assert game.board[2][2] == HUMAN
print("✓ Human stone placed correctly")

# Test 4: Switch to ZidanAI
print("\n4. Testing turn switch...")
game.next_turn()
print(f"  Current player: {game.get_player_name(game.current_player)}")
assert game.current_player == ZIDAN_AI
print("✓ Turn switched to ZidanAI")

# Test 5: Check turn order
print("\n5. Testing turn order...")
print(f"  Players in Mode B: {[game.get_player_name(p) for p in game.players]}")
assert game.players == [HUMAN, ZIDAN_AI]
print("✓ Turn order is correct: Human → ZidanAI")

# Test 6: Simulate full turn cycle
print("\n6. Testing full turn cycle...")
game2 = GameState(mode='B')
print(f"  Start: {game2.get_player_name(game2.current_player)}")
assert game2.current_player == HUMAN

game2.apply_move(1, 1, HUMAN)
game2.next_turn()
print(f"  After human move: {game2.get_player_name(game2.current_player)}")
assert game2.current_player == ZIDAN_AI

game2.apply_move(1, 2, ZIDAN_AI)
game2.next_turn()
print(f"  After AI move: {game2.get_player_name(game2.current_player)}")
assert game2.current_player == HUMAN
print("✓ Full turn cycle works: Human → ZidanAI → Human")

# Test 7: Illegal move handling
print("\n7. Testing illegal move validation...")
game3 = GameState(mode='B')
game3.apply_move(0, 0, HUMAN)
print(f"  First move at (0,0): occupied")
illegal = game3.is_legal(0, 0)
print(f"  Is (0,0) legal now? {illegal}")
assert illegal == False
print("✓ Illegal move detection works")

print("\n" + "=" * 50)
print("✓ All Mode B logic tests passed!")
print("=" * 50)
print("\nMode B is ready:")
print("  1. Human makes move (click cell in UI)")
print("  2. Backend applies human move")
print("  3. Backend automatically runs ZidanAI")
print("  4. Both moves returned in single response")
print("  5. UI updates with both moves")
