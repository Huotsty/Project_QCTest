"""
test_capture_suicide.py - Unit tests for capture and suicide rules
"""
import sys
from game import GameState, ZIDAN_AI, RULES_AI, HUMAN, EMPTY

def print_board(game):
    """Helper to print board state."""
    print(game.print_board())
    print()

def test_single_stone_capture():
    """Test capturing a single isolated stone."""
    print("=" * 50)
    print("TEST 1: Single Stone Capture")
    print("=" * 50)
    
    game = GameState(mode='A')
    
    # Place white stone at (2,2)
    game.board[2][2] = RULES_AI
    print("White stone at (2,2):")
    print_board(game)
    
    # Surround it with black stones
    game.board[1][2] = ZIDAN_AI  # Top
    game.board[3][2] = ZIDAN_AI  # Bottom
    game.board[2][1] = ZIDAN_AI  # Left
    
    print("Black stones surrounding (top, bottom, left):")
    print_board(game)
    
    # Place final black stone to capture
    success, captures, is_suicide, msg = game.try_move(2, 3, ZIDAN_AI)
    
    print(f"Placing black at (2,3) - the killing move:")
    print(f"Success: {success}")
    print(f"Captures: {captures}")
    print(f"Is Suicide: {is_suicide}")
    print(f"Message: {msg}")
    print_board(game)
    
    assert success, "Move should succeed"
    assert len(captures) == 1, f"Should capture 1 stone, got {len(captures)}"
    assert (2, 2) in captures, "Should capture stone at (2,2)"
    assert game.board[2][2] == EMPTY, "Captured stone should be removed"
    
    print("✅ Test 1 PASSED: Single stone captured correctly\n")

def test_multi_stone_group_capture():
    """Test capturing a connected group of stones."""
    print("=" * 50)
    print("TEST 2: Multi-Stone Group Capture")
    print("=" * 50)
    
    game = GameState(mode='A')
    
    # Create a white group (2,2) and (2,3)
    game.board[2][2] = RULES_AI
    game.board[2][3] = RULES_AI
    print("White group at (2,2) and (2,3):")
    print_board(game)
    
    # Surround the group
    game.board[1][2] = ZIDAN_AI
    game.board[1][3] = ZIDAN_AI
    game.board[3][2] = ZIDAN_AI
    game.board[3][3] = ZIDAN_AI
    game.board[2][1] = ZIDAN_AI
    
    print("Black stones surrounding the group (missing right side):")
    print_board(game)
    
    # Capture with final move
    success, captures, is_suicide, msg = game.try_move(2, 4, ZIDAN_AI)
    
    print(f"Placing black at (2,4) - capturing the group:")
    print(f"Success: {success}")
    print(f"Captures: {captures}")
    print(f"Message: {msg}")
    print_board(game)
    
    assert success, "Move should succeed"
    assert len(captures) == 2, f"Should capture 2 stones, got {len(captures)}"
    assert (2, 2) in captures and (2, 3) in captures, "Should capture both stones"
    assert game.board[2][2] == EMPTY and game.board[2][3] == EMPTY, "Captured stones should be removed"
    
    print("✅ Test 2 PASSED: Multi-stone group captured correctly\n")

def test_suicide_rejection():
    """Test that suicide moves are rejected."""
    print("=" * 50)
    print("TEST 3: Suicide Move Rejection")
    print("=" * 50)
    
    game = GameState(mode='A')
    
    # Create a surrounded position
    game.board[1][2] = RULES_AI
    game.board[3][2] = RULES_AI
    game.board[2][1] = RULES_AI
    game.board[2][3] = RULES_AI
    
    print("White stones forming a trap at (2,2):")
    print_board(game)
    
    # Try to place black stone in suicide position
    success, captures, is_suicide, msg = game.try_move(2, 2, ZIDAN_AI)
    
    print(f"Attempting to place black at (2,2) (suicide):")
    print(f"Success: {success}")
    print(f"Captures: {captures}")
    print(f"Is Suicide: {is_suicide}")
    print(f"Message: {msg}")
    print_board(game)
    
    assert not success, "Suicide move should be rejected"
    assert is_suicide, "Should be flagged as suicide"
    assert game.board[2][2] == EMPTY, "Board should remain unchanged"
    
    print("✅ Test 3 PASSED: Suicide move correctly rejected\n")

def test_capture_vs_suicide():
    """Test that capturing opponent stones makes the move legal (not suicide)."""
    print("=" * 50)
    print("TEST 4: Capture vs Suicide (Legal Capture)")
    print("=" * 50)
    
    game = GameState(mode='A')
    
    # Create scenario where black move looks like suicide but actually captures white
    game.board[2][2] = RULES_AI  # White stone with 1 liberty
    game.board[1][2] = ZIDAN_AI  # Black stones surrounding white
    game.board[3][2] = ZIDAN_AI
    game.board[2][1] = ZIDAN_AI
    
    # Black stones also surround (2,3) except white at (2,2)
    game.board[1][3] = ZIDAN_AI
    game.board[3][3] = ZIDAN_AI
    game.board[2][4] = ZIDAN_AI
    
    print("Setup: White at (2,2) with 1 liberty. Black surrounding (2,3):")
    print_board(game)
    
    # Place black at (2,3) - looks like suicide but captures white first
    success, captures, is_suicide, msg = game.try_move(2, 3, ZIDAN_AI)
    
    print(f"Placing black at (2,3):")
    print(f"Success: {success}")
    print(f"Captures: {captures}")
    print(f"Is Suicide: {is_suicide}")
    print(f"Message: {msg}")
    print_board(game)
    
    assert success, "Move should succeed (captures white stone)"
    assert len(captures) == 1, f"Should capture 1 stone, got {len(captures)}"
    assert (2, 2) in captures, "Should capture white stone at (2,2)"
    assert not is_suicide, "Should not be flagged as suicide"
    
    print("✅ Test 4 PASSED: Capture makes move legal (not suicide)\n")

def test_atari_situation():
    """Test atari (putting opponent in 1-liberty danger)."""
    print("=" * 50)
    print("TEST 5: Atari Situation")
    print("=" * 50)
    
    game = GameState(mode='A')
    
    # Place white stone
    game.board[2][2] = RULES_AI
    
    # Surround with black except one liberty
    game.board[1][2] = ZIDAN_AI
    game.board[3][2] = ZIDAN_AI
    game.board[2][1] = ZIDAN_AI
    
    print("White stone at (2,2) with 1 liberty remaining:")
    print_board(game)
    
    liberties = game.get_group_liberties(2, 2)
    print(f"White group has {liberties} liberty/liberties")
    
    assert liberties == 1, "White should have exactly 1 liberty (atari)"
    assert game.board[2][2] == RULES_AI, "White stone should still be on board"
    
    print("✅ Test 5 PASSED: Atari situation recognized (1 liberty)\n")

def test_corner_capture():
    """Test capturing stones in corner positions."""
    print("=" * 50)
    print("TEST 6: Corner Capture")
    print("=" * 50)
    
    game = GameState(mode='A')
    
    # Place white in corner (0,0)
    game.board[0][0] = RULES_AI
    print("White stone in corner (0,0):")
    print_board(game)
    
    # Surround with black (only 2 moves needed for corner)
    game.board[0][1] = ZIDAN_AI  # Right
    
    print("Black at (0,1), white has 1 liberty:")
    print_board(game)
    
    # Capture
    success, captures, is_suicide, msg = game.try_move(1, 0, ZIDAN_AI)
    
    print(f"Placing black at (1,0) - capturing corner:")
    print(f"Success: {success}")
    print(f"Captures: {captures}")
    print_board(game)
    
    assert success, "Move should succeed"
    assert len(captures) == 1, f"Should capture 1 stone, got {len(captures)}"
    assert (0, 0) in captures, "Should capture corner stone"
    
    print("✅ Test 6 PASSED: Corner capture works correctly\n")

def test_edge_suicide():
    """Test suicide detection on board edge."""
    print("=" * 50)
    print("TEST 7: Edge Suicide")
    print("=" * 50)
    
    game = GameState(mode='A')
    
    # Create suicide trap on edge
    game.board[0][1] = RULES_AI  # Top edge
    game.board[1][0] = RULES_AI
    game.board[1][1] = RULES_AI
    
    print("White stones forming edge trap:")
    print_board(game)
    
    # Try suicide on edge
    success, captures, is_suicide, msg = game.try_move(0, 0, ZIDAN_AI)
    
    print(f"Attempting black at corner (0,0) - suicide:")
    print(f"Success: {success}")
    print(f"Is Suicide: {is_suicide}")
    print(f"Message: {msg}")
    
    assert not success, "Edge suicide should be rejected"
    assert is_suicide, "Should be flagged as suicide"
    
    print("✅ Test 7 PASSED: Edge suicide correctly rejected\n")

def test_complex_capture_scenario():
    """Test complex scenario with multiple groups."""
    print("=" * 50)
    print("TEST 8: Complex Multi-Group Scenario")
    print("=" * 50)
    
    game = GameState(mode='A')
    
    # Create complex board state
    # White group 1: (1,1)
    game.board[1][1] = RULES_AI
    # White group 2: (3,3)
    game.board[3][3] = RULES_AI
    
    # Black stones
    game.board[0][1] = ZIDAN_AI
    game.board[1][0] = ZIDAN_AI
    game.board[1][2] = ZIDAN_AI
    game.board[2][1] = ZIDAN_AI  # Surrounds white group 1
    
    game.board[2][3] = ZIDAN_AI
    game.board[3][2] = ZIDAN_AI
    game.board[3][4] = ZIDAN_AI
    game.board[4][3] = ZIDAN_AI  # Surrounds white group 2
    
    print("Two white groups, both in atari:")
    print_board(game)
    
    # Check liberties before capture
    lib1 = game.get_group_liberties(1, 1)
    lib2 = game.get_group_liberties(3, 3)
    print(f"White group 1 at (1,1) has {lib1} liberties")
    print(f"White group 2 at (3,3) has {lib2} liberties")
    
    # Capture both groups with one move
    success1, captures1, _, _ = game.try_move(2, 2, ZIDAN_AI)
    print(f"Move: Black at (2,2) captures: {captures1}")
    print_board(game)
    
    # Both groups should be captured since (2,2) fills the last liberty for both
    assert success1, "Move should succeed"
    assert len(captures1) == 2, f"Should capture 2 stones (both groups), got {len(captures1)}"
    assert (1, 1) in captures1 and (3, 3) in captures1, "Should capture both white stones"
    
    print("✅ Test 8 PASSED: Complex scenario - both groups captured\n")

def run_all_tests():
    """Run all capture and suicide tests."""
    print("\n" + "=" * 50)
    print("RUNNING ALL CAPTURE & SUICIDE TESTS")
    print("=" * 50 + "\n")
    
    tests = [
        test_single_stone_capture,
        test_multi_stone_group_capture,
        test_suicide_rejection,
        test_capture_vs_suicide,
        test_atari_situation,
        test_corner_capture,
        test_edge_suicide,
        test_complex_capture_scenario
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"❌ TEST FAILED: {e}\n")
            failed += 1
        except Exception as e:
            print(f"❌ TEST ERROR: {e}\n")
            failed += 1
    
    print("\n" + "=" * 50)
    print(f"TEST SUMMARY: {passed} passed, {failed} failed")
    print("=" * 50 + "\n")
    
    return failed == 0

if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
