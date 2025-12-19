"""
app.py - Flask web application for Quantum Go
"""
import warnings
warnings.filterwarnings('ignore')

from flask import Flask, render_template, request, jsonify, session
import os
import sys
from game import GameState, ZIDAN_AI, RULES_AI, HUMAN
from zidan_ai import ZidanAI
from rules_ai import RuleBasedAI

app = Flask(__name__)
app.secret_key = 'quantum_go_secret_key_2025'

# Global game state storage (in production, use database or Redis)
games = {}

@app.route('/')
def index():
    """Main page with mode selection and game board."""
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_game():
    """Initialize a new game with selected mode."""
    try:
        data = request.get_json()
        mode = data.get('mode', 'A')
        
        if mode not in ['A', 'B']:
            return jsonify({'error': 'Invalid mode'}), 400
        
        # Create new game
        game_id = len(games) + 1
        game = GameState(mode=mode)
        games[game_id] = game
        
        # Store game_id in session
        session['game_id'] = game_id
        
        # Initial log entry
        log_entry = {
            'turn': 0,
            'player': 'System',
            'message': f'Game started in Mode {mode}',
            'board': game.print_board()
        }
        game.game_log.append(log_entry)
        
        response = {
            'game_id': game_id,
            'mode': mode,
            'board': game.board,
            'current_player': game.get_player_name(game.current_player),
            'game_log': game.game_log,
            'game_over': game.game_over
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/play', methods=['POST'])
def play_turn():
    """
    Execute a turn:
    - Mode A: Auto-play (ZidanAI or RuleBasedAI)
    - Mode B: Accept human move or auto-play ZidanAI
    """
    try:
        data = request.get_json()
        game_id = session.get('game_id')
        
        if game_id not in games:
            return jsonify({'error': 'Game not found'}), 404
        
        game = games[game_id]
        
        if game.game_over:
            return jsonify({'error': 'Game already over', 'winner': game.winner}), 400
        
        # Handle human move in Mode B
        if game.mode == 'B' and game.current_player == HUMAN:
            row = data.get('row')
            col = data.get('col')
            
            if row is None or col is None:
                return jsonify({'error': 'Row and col required for human move'}), 400
            
            if not game.is_legal(row, col):
                return jsonify({'error': 'Illegal move'}), 400
            
            # Apply human move
            game.apply_move(row, col, HUMAN)
            
            log_entry = {
                'turn': game.turn_count + 1,
                'player': 'Human',
                'move': f'({row}, {col})',
                'rationale': 'Human player move',
                'board': game.print_board()
            }
            game.game_log.append(log_entry)
            
            game.next_turn()
            
            # Check game over
            if game.check_game_over():
                return jsonify({
                    'board': game.board,
                    'current_player': None,
                    'game_log': game.game_log,
                    'game_over': True,
                    'winner': game.winner
                })
        
        # AI turn
        if game.current_player == ZIDAN_AI:
            # ZidanAI move
            zidan = ZidanAI(game)
            result = zidan.choose_move()
            
            row, col = result['row'], result['col']
            
            if row is None:
                # Pass
                game.pass_turn()
                log_entry = {
                    'turn': game.turn_count + 1,
                    'player': 'ZidanAI',
                    'move': 'Pass',
                    'rationale': result['rationale'],
                    'board': game.print_board()
                }
            else:
                # Apply move
                game.apply_move(row, col, ZIDAN_AI)
                
                log_entry = {
                    'turn': game.turn_count + 1,
                    'player': 'ZidanAI',
                    'move': f'({row}, {col})',
                    'rationale': result['rationale'],
                    'features': result['features'],
                    'classification': result['classification'],
                    'confidence': f"{result['confidence']:.1f}%",
                    'entanglement_score': f"{result['entanglement_score']:.3f}",
                    'bell_counts': result['bell_counts'],
                    'circuit_image': result['circuit_image'],
                    'histogram_image': result['histogram_image'],
                    'board': game.print_board()
                }
            
            game.game_log.append(log_entry)
            game.next_turn()
        
        elif game.current_player == RULES_AI:
            # RuleBasedAI move
            rules = RuleBasedAI(game)
            row, col, rationale = rules.choose_move()
            
            if row is None:
                # Pass
                game.pass_turn()
                log_entry = {
                    'turn': game.turn_count + 1,
                    'player': 'RuleBasedAI',
                    'move': 'Pass',
                    'rationale': rationale,
                    'board': game.print_board()
                }
            else:
                # Apply move
                game.apply_move(row, col, RULES_AI)
                
                log_entry = {
                    'turn': game.turn_count + 1,
                    'player': 'RuleBasedAI',
                    'move': f'({row}, {col})',
                    'rationale': rationale,
                    'board': game.print_board()
                }
            
            game.game_log.append(log_entry)
            game.next_turn()
        
        # Check game over
        game.check_game_over()
        
        response = {
            'board': game.board,
            'current_player': game.get_player_name(game.current_player) if not game.game_over else None,
            'game_log': game.game_log,
            'game_over': game.game_over,
            'winner': game.winner if game.game_over else None,
            'turn_count': game.turn_count
        }
        
        return jsonify(response)
    
    except Exception as e:
        import traceback
        return jsonify({'error': str(e), 'trace': traceback.format_exc()}), 500

@app.route('/get_state', methods=['GET'])
def get_state():
    """Get current game state."""
    try:
        game_id = session.get('game_id')
        
        if game_id not in games:
            return jsonify({'error': 'No active game'}), 404
        
        game = games[game_id]
        
        response = {
            'board': game.board,
            'current_player': game.get_player_name(game.current_player) if not game.game_over else None,
            'game_log': game.game_log,
            'game_over': game.game_over,
            'winner': game.winner if game.game_over else None,
            'turn_count': game.turn_count,
            'mode': game.mode
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
