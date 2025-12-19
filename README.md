# ⚛️ Quantum Go - ZidanAI Project

A Flask web application for a 5x5 Quantum Go game featuring **ZidanAI**, a quantum-powered strategic AI using Qiskit for decision-making through Bell state measurements.

## 🎮 Game Modes

- **Mode A**: ZidanAI (Quantum AI) vs RuleBasedAI (Classical Heuristic AI)
- **Mode B**: Human (via UI clicks) vs ZidanAI (Quantum AI)

## 🚀 Features

### ZidanAI (Quantum Strategic AI)
- Extracts game features: territory delta, liberty pressure, connectivity
- Encodes features into 3-qubit quantum circuit with 2 ancilla qubits
- Measures in Bell basis to compute entanglement score
- Classifies game state as WINNING/LOSING with confidence percentage
- Generates circuit diagrams and measurement histograms
- Makes strategic decisions (aggressive/defensive) based on quantum analysis

### RuleBasedAI (Classical Heuristic AI)
- Uses classical heuristics: maximize liberties, block opponent, increase connectivity
- Provides rationale for each move

### Game Rules
- 5x5 board (simplified Go)
- Max 30 turns or game ends after 2 consecutive passes
- Scoring: territory count + liberties + connectivity bonus
- Winner determined by highest score

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip

### Setup Steps

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Open in browser:**
   ```
   http://localhost:5000
   ```

## 🎯 How to Play

### Mode A (AI vs AI)
1. Select "Mode A" button
2. Click "Start New Game"
3. Click "Next Turn" to watch each AI take turns
4. View quantum analysis and circuit diagrams in the game log

### Mode B (Human vs AI)
1. Select "Mode B" button
2. Click "Start New Game"
3. Click any empty cell on the board to place your stone (green with 'H')
4. ZidanAI automatically responds after your move
5. Continue alternating turns until game ends

## 📊 Understanding the Output

### Game Board
- **Blue stones (Z)**: ZidanAI
- **Red stones (R)**: RuleBasedAI
- **Green stones (H)**: Human player

### Quantum Analysis (ZidanAI only)
- **Features**: Territory delta, liberty pressure, connectivity values
- **Bell Counts**: Measurement results from quantum circuit (00, 01, 10, 11)
- **Entanglement Score (S)**: Ranges from -1 to 1
  - S > 0 → WINNING (correlated states)
  - S ≤ 0 → LOSING (anti-correlated states)
- **Classification**: WINNING or LOSING state
- **Confidence**: Percentage confidence in classification
- **Circuit Diagram**: Visual representation of quantum circuit
- **Histogram**: Bar chart of Bell state measurements

### Game Log
Each turn shows:
- Turn number and player
- Move coordinates or "Pass"
- Rationale/strategy
- Board snapshot
- Quantum analysis (for ZidanAI moves)

## 🏗️ Project Structure

```
Project/
├── app.py                 # Flask web application with routes
├── game.py               # Core game logic and board helpers
├── zidan_ai.py           # Quantum AI with Qiskit
├── rules_ai.py           # Classical rule-based AI
├── templates/
│   └── index.html        # Web UI
└── requirements.txt      # Python dependencies
```

## 🔬 Quantum Circuit Design

ZidanAI uses a 5-qubit circuit:
- **Qubits 0-2**: Feature encoding (territory, liberty, connectivity)
- **Qubits 3-4**: Ancilla qubits for entanglement
- **Measurement**: Bell basis on ancilla qubits
- **Strategy**: 
  - WINNING → Aggressive moves (expand territory)
  - LOSING → Defensive moves (block opponent, preserve liberties)

## 📝 Technical Details

### Backend Technologies
- **Flask**: Web framework
- **Qiskit**: Quantum computing framework
- **Qiskit Aer**: Quantum simulator
- **Matplotlib**: Circuit and histogram visualization
- **NumPy**: Numerical computations

### Frontend Technologies
- **HTML5/CSS3**: Modern responsive UI
- **Vanilla JavaScript**: Interactive gameplay
- **Fetch API**: Asynchronous communication with backend

## 🎨 UI Features
- Gradient background and modern design
- Real-time board updates
- Scrollable game log with embedded quantum visualizations
- Color-coded player indicators
- Winner announcement banner
- Turn counter and status display

## 🔧 Configuration

### Quantum Settings
- **Shots**: 1024 measurements per circuit
- **Backend**: AerSimulator (local quantum simulator)
- **Normalization**: Features normalized to [0, π] using tanh

### Game Settings
- **Board Size**: 5x5
- **Max Turns**: 30
- **Pass Limit**: 2 consecutive passes end game

## 🐛 Troubleshooting

1. **Import Errors**: Ensure all packages in `requirements.txt` are installed
2. **Port Already in Use**: Change port in `app.py` (default: 5000)
3. **Matplotlib Warnings**: Already suppressed with Agg backend
4. **Session Issues**: Clear browser cookies or use incognito mode

## 📄 License

This project is created for educational purposes demonstrating quantum computing applications in game AI.

## 🙏 Acknowledgments

- Qiskit team for quantum computing framework
- Flask community for web framework
- Quantum computing research in game AI

---

**Enjoy exploring quantum strategy in Go! ⚛️🎮**
