"""
zidan_ai.py - Quantum Strategic AI using Qiskit for decision making
"""
import warnings
warnings.filterwarnings('ignore')

import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import io
import base64

class ZidanAI:
    """Quantum-powered strategic AI using Bell state measurements."""
    
    def __init__(self, game_state):
        self.game_state = game_state
        self.player = 1  # ZIDAN_AI
        self.backend = AerSimulator()
    
    def extract_features(self):
        """
        Extract strategic features from current board state.
        Returns: (territory_delta, liberty_pressure, connectivity)
        """
        # Get opponent
        if self.game_state.mode == 'A':
            opponent = 2  # RULES_AI
        else:
            opponent = 3  # HUMAN
        
        # Territory delta
        my_territory = self.game_state.count_territory(self.player)
        opp_territory = self.game_state.count_territory(opponent)
        territory_delta = my_territory - opp_territory
        
        # Liberty pressure (my liberties - opponent liberties)
        my_liberties = self.game_state.count_total_liberties(self.player)
        opp_liberties = self.game_state.count_total_liberties(opponent)
        liberty_pressure = my_liberties - opp_liberties
        
        # Connectivity (my group size - opponent group size)
        my_connectivity = self.game_state.count_connectivity(self.player)
        opp_connectivity = self.game_state.count_connectivity(opponent)
        connectivity = my_connectivity - opp_connectivity
        
        return territory_delta, liberty_pressure, connectivity
    
    def normalize_feature(self, value, scale=10.0):
        """Normalize feature to [0, π] range."""
        # Map value to angle using tanh normalization
        normalized = np.tanh(value / scale) * np.pi / 2 + np.pi / 2
        return normalized
    
    def build_quantum_circuit(self, features):
        """
        Build quantum circuit encoding features with entanglement.
        - 3 qubits for features (territory, liberty, connectivity)
        - 2 ancilla qubits for entanglement
        - Measure in Bell basis
        """
        territory_delta, liberty_pressure, connectivity = features
        
        # Create 5-qubit circuit
        qc = QuantumCircuit(5, 2)
        
        # Encode features as rotations on qubits 0, 1, 2
        theta1 = self.normalize_feature(territory_delta)
        theta2 = self.normalize_feature(liberty_pressure)
        theta3 = self.normalize_feature(connectivity)
        
        qc.ry(theta1, 0)
        qc.ry(theta2, 1)
        qc.ry(theta3, 2)
        
        # Entangle with ancilla qubits (3, 4)
        qc.h(3)
        qc.h(4)
        qc.cx(0, 3)
        qc.cx(1, 4)
        qc.cx(2, 3)
        
        # Create Bell-like entanglement
        qc.h(3)
        qc.cx(3, 4)
        
        # Measure ancillas in Bell basis
        qc.h(3)
        qc.measure([3, 4], [0, 1])
        
        return qc
    
    def run_quantum_circuit(self, qc):
        """Execute circuit and return measurement counts."""
        transpiled_qc = transpile(qc, self.backend)
        job = self.backend.run(transpiled_qc, shots=1024)
        result = job.result()
        counts = result.get_counts()
        return counts
    
    def calculate_entanglement_score(self, counts):
        """
        Calculate entanglement score S from Bell measurements.
        S = (p00 + p11) - (p01 + p10)
        Range: [-1, 1]
        """
        total_shots = sum(counts.values())
        
        # Get probabilities
        p00 = counts.get('00', 0) / total_shots
        p01 = counts.get('01', 0) / total_shots
        p10 = counts.get('10', 0) / total_shots
        p11 = counts.get('11', 0) / total_shots
        
        S = (p00 + p11) - (p01 + p10)
        
        return S, {'00': p00, '01': p01, '10': p10, '11': p11}
    
    def classify_state(self, S):
        """
        Classify game state as WINNING or LOSING based on entanglement score.
        S > 0 → WINNING (correlated)
        S <= 0 → LOSING (anti-correlated)
        """
        if S > 0:
            classification = "WINNING"
            confidence = (S + 1) / 2 * 100  # Map [-1,1] to [0,100]
        else:
            classification = "LOSING"
            confidence = (1 - abs(S)) / 2 * 100
        
        return classification, confidence
    
    def choose_aggressive_move(self):
        """Choose aggressive move (maximize territory/connectivity)."""
        legal_moves = self.game_state.get_legal_moves()
        if not legal_moves:
            return None, None, "No legal moves"
        
        best_score = -1000
        best_move = None
        
        for row, col in legal_moves:
            score = 0
            
            # Prioritize center
            center_score = 10 - (abs(row - 2) + abs(col - 2)) * 2
            score += center_score
            
            # Connectivity bonus
            friendly_adjacent = sum(1 for nr, nc in self.game_state.get_neighbors(row, col)
                                   if self.game_state.board[nr][nc] == self.player)
            score += friendly_adjacent * 5
            
            # Territory expansion
            liberty_count = sum(1 for nr, nc in self.game_state.get_neighbors(row, col)
                               if self.game_state.board[nr][nc] == 0)
            score += liberty_count * 3
            
            if score > best_score:
                best_score = score
                best_move = (row, col)
        
        return best_move[0], best_move[1], "Aggressive: expand territory/connectivity"
    
    def choose_defensive_move(self):
        """Choose defensive move (block opponent, preserve liberties)."""
        legal_moves = self.game_state.get_legal_moves()
        if not legal_moves:
            return None, None, "No legal moves"
        
        opponent = 2 if self.game_state.mode == 'A' else 3
        best_score = -1000
        best_move = None
        
        for row, col in legal_moves:
            score = 0
            
            # Block opponent
            enemy_adjacent = sum(1 for nr, nc in self.game_state.get_neighbors(row, col)
                                if self.game_state.board[nr][nc] == opponent)
            score += enemy_adjacent * 8
            
            # Preserve liberties
            liberty_count = sum(1 for nr, nc in self.game_state.get_neighbors(row, col)
                               if self.game_state.board[nr][nc] == 0)
            score += liberty_count * 4
            
            # Avoid edges
            if row in [0, 4] or col in [0, 4]:
                score -= 3
            
            if score > best_score:
                best_score = score
                best_move = (row, col)
        
        return best_move[0], best_move[1], "Defensive: block opponent/preserve liberties"
    
    def generate_circuit_image(self, qc):
        """Generate circuit diagram as base64 encoded image."""
        try:
            fig = qc.draw('mpl', output='mpl')
            buf = io.BytesIO()
            fig.savefig(buf, format='png', bbox_inches='tight', dpi=100)
            buf.seek(0)
            img_base64 = base64.b64encode(buf.read()).decode('utf-8')
            plt.close(fig)
            return img_base64
        except Exception as e:
            return None
    
    def generate_histogram_image(self, counts):
        """Generate histogram of measurement results as base64 encoded image."""
        try:
            fig, ax = plt.subplots(figsize=(6, 4))
            states = ['00', '01', '10', '11']
            values = [counts.get(state, 0) for state in states]
            ax.bar(states, values, color=['blue', 'orange', 'green', 'red'])
            ax.set_xlabel('Bell States')
            ax.set_ylabel('Counts')
            ax.set_title('Quantum Measurement Results')
            ax.grid(axis='y', alpha=0.3)
            
            buf = io.BytesIO()
            fig.savefig(buf, format='png', bbox_inches='tight', dpi=100)
            buf.seek(0)
            img_base64 = base64.b64encode(buf.read()).decode('utf-8')
            plt.close(fig)
            return img_base64
        except Exception as e:
            return None
    
    def choose_move(self):
        """
        Main decision-making pipeline.
        Returns: dict with move info, quantum analysis, and visualizations
        """
        # Extract features
        features = self.extract_features()
        territory_delta, liberty_pressure, connectivity = features
        
        # Build and run quantum circuit
        qc = self.build_quantum_circuit(features)
        counts = self.run_quantum_circuit(qc)
        
        # Calculate entanglement score
        S, bell_probs = self.calculate_entanglement_score(counts)
        
        # Classify state
        classification, confidence = self.classify_state(S)
        
        # Choose move based on classification
        if classification == "WINNING":
            row, col, strategy = self.choose_aggressive_move()
        else:
            row, col, strategy = self.choose_defensive_move()
        
        # Generate visualizations
        circuit_img = self.generate_circuit_image(qc)
        histogram_img = self.generate_histogram_image(counts)
        
        # Compile results
        result = {
            'row': row,
            'col': col,
            'features': {
                'territory_delta': territory_delta,
                'liberty_pressure': liberty_pressure,
                'connectivity': connectivity
            },
            'bell_counts': counts,
            'bell_probs': bell_probs,
            'entanglement_score': S,
            'classification': classification,
            'confidence': confidence,
            'strategy': strategy,
            'circuit_image': circuit_img,
            'histogram_image': histogram_img,
            'rationale': f"{classification} (conf={confidence:.1f}%): {strategy}"
        }
        
        return result
