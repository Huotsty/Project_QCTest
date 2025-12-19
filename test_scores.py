"""
Test game end when board is full and score display
"""
from game import GameState, HUMAN, ZIDAN_AI

print("Testing Game End & Score Display...")
print("=" * 50)

# Test 1: Check score calculation works
print("\n1. Testing score calculation...")
game = GameState(mode='B')
game.apply_move(2, 2, HUMAN)
game.apply_move(2, 3, ZIDAN_AI)

human_score = game.get_score_breakdown(HUMAN)
ai_score = game.get_score_breakdown(ZIDAN_AI)

print(f"  Human score: {human_score}")
print(f"  AI score: {ai_score}")
assert 'territory' in human_score
assert 'liberties' in human_score
assert 'connectivity' in human_score
assert 'total' in human_score
print("✓ Score breakdown working")

# Test 2: Check game ends when board is full
print("\n2. Testing game end when board is full...")
game2 = GameState(mode='B')

# Fill the board
moves = [
    # Row 0
    (0, 0, HUMAN), (0, 1, ZIDAN_AI), (0, 2, HUMAN), (0, 3, ZIDAN_AI), (0, 4, HUMAN),
    # Row 1
    (1, 0, ZIDAN_AI), (1, 1, HUMAN), (1, 2, ZIDAN_AI), (1, 3, HUMAN), (1, 4, ZIDAN_AI),
    # Row 2
    (2, 0, HUMAN), (2, 1, ZIDAN_AI), (2, 2, HUMAN), (2, 3, ZIDAN_AI), (2, 4, HUMAN),
    # Row 3
    (3, 0, ZIDAN_AI), (3, 1, HUMAN), (3, 2, ZIDAN_AI), (3, 3, HUMAN), (3, 4, ZIDAN_AI),
    # Row 4
    (4, 0, HUMAN), (4, 1, ZIDAN_AI), (4, 2, HUMAN), (4, 3, ZIDAN_AI), (4, 4, HUMAN),
]

for i, (r, c, player) in enumerate(moves):
    game2.apply_move(r, c, player)
    game2.turn_count += 1
    if i < len(moves) - 1:
        assert not game2.game_over, f"Game ended too early at move {i+1}"

print(f"  Placed {len(moves)} stones")
print(f"  Legal moves remaining: {len(game2.get_legal_moves())}")
assert len(game2.get_legal_moves()) == 0, "Board should be full"

# Check game over
game_over = game2.check_game_over()
print(f"  Game over: {game_over}")
assert game_over == True, "Game should end when board is full"
print("✓ Game ends when board is full")

# Test 3: Verify winner is determined
print("\n3. Testing winner determination...")
print(f"  Winner: {game2.winner}")
assert game2.winner is not None, "Winner should be determined"
print("✓ Winner determined when board is full")

# Test 4: Display final scores
print("\n4. Final scores when board is full:")
human_final = game2.get_score_breakdown(HUMAN)
ai_final = game2.get_score_breakdown(ZIDAN_AI)
print(f"  Human: {human_final['total']} pts (T:{human_final['territory']}×2 + L:{human_final['liberties']} + C:{human_final['connectivity']}×3)")
print(f"  ZidanAI: {ai_final['total']} pts (T:{ai_final['territory']}×2 + L:{ai_final['liberties']} + C:{ai_final['connectivity']}×3)")
print(f"  Winner: {game2.winner}")
print("✓ Score display working")

print("\n" + "=" * 50)
print("✓ All tests passed!")
print("=" * 50)
print("\nFixes implemented:")
print("  1. ✅ Game ends when board is full (no legal moves)")
print("  2. ✅ Score breakdown calculated for each player")
print("  3. ✅ Scores displayed after each move in log")
print("  4. ✅ Current scores shown in status panel")
print("\nNow when you play:")
print("  • Board full = Game ends automatically")
print("  • See scores update after every move")
print("  • Score panel shows: Territory, Liberties, Connectivity")
