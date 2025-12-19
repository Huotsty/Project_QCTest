# 🎮 Quantum Go - Quick Start Guide

## 📋 What You Have

A complete Flask web application for 5x5 Quantum Go featuring:
- **ZidanAI**: Quantum-powered AI using Qiskit Bell measurements
- **RuleBasedAI**: Classical heuristic strategy
- **Human Mode**: Play against ZidanAI via web UI

## 🚀 Getting Started (3 Steps)

### Step 1: Install Dependencies
Open terminal in project folder and run:
```bash
pip install -r requirements.txt
```

### Step 2: Start the Server
Choose one method:

**Windows Users:**
```bash
run.bat
```

**Any OS:**
```bash
python app.py
```

**Alternative:**
```bash
python launcher.py
```

### Step 3: Open Browser
Navigate to:
```
http://localhost:5000
```

## 🎯 Playing the Game

### Mode A: Watch AI Battle
1. Click **"Mode A"** button
2. Click **"Start New Game"**
3. Click **"Next Turn"** repeatedly to watch AIs play
4. View quantum analysis in game log

### Mode B: Play vs ZidanAI
1. Click **"Mode B"** button
2. Click **"Start New Game"**
3. Click any **empty cell** to place your stone (green)
4. **ZidanAI automatically responds** with its quantum-powered move (blue)
5. Repeat until game ends (both moves happen in one request)

## 🔍 Understanding the Output

### Board Colors
- 🔵 **Blue (Z)**: ZidanAI
- 🔴 **Red (R)**: RuleBasedAI
- 🟢 **Green (H)**: Human

### ZidanAI Quantum Info
Each ZidanAI move shows:
- **Classification**: WINNING or LOSING
- **Confidence**: 0-100%
- **Entanglement Score**: -1 to +1
- **Features**: Territory, Liberty, Connectivity values
- **Circuit Diagram**: Visual quantum circuit
- **Histogram**: Bell state measurements

### Game End
Game ends when:
- 30 turns reached, OR
- 2 consecutive passes

Winner = highest score:
```
Score = Territory×2 + Liberties + Connectivity×3
```

## 🧪 Test Before Running

Verify everything works:
```bash
python test_setup.py
```

Should see:
```
✓ All tests passed! Ready to run the application.
```

## 🐛 Troubleshooting

### "Module not found"
```bash
pip install -r requirements.txt
```

### "Port 5000 already in use"
Edit `app.py` line 177:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Changed to 5001
```

### Page won't load
- Check terminal for errors
- Try restarting the server
- Clear browser cache

## 📚 Project Files

```
Project/
├── app.py              # Flask server ⚙️
├── game.py             # Game logic 🎲
├── zidan_ai.py         # Quantum AI 🔮
├── rules_ai.py         # Classical AI 🤖
├── templates/
│   └── index.html      # Web UI 🌐
├── requirements.txt    # Dependencies 📦
├── README.md           # Full documentation 📖
├── IMPLEMENTATION.md   # Technical details 📝
├── test_setup.py       # Test script ✅
└── run.bat            # Windows launcher 🚀
```

## 💡 Tips

1. **Mode A**: Great for observing quantum vs classical strategies
2. **Mode B**: Try different opening strategies against ZidanAI
3. **Center Control**: Often strategic due to connectivity bonus
4. **Watch Confidence**: ZidanAI adjusts strategy based on quantum confidence
5. **Logs**: Scroll through to see full quantum analysis history

## 🎓 Key Concepts

### Quantum Advantage
ZidanAI uses quantum entanglement to:
- Encode multiple features simultaneously
- Measure correlations via Bell states
- Make probabilistic strategic decisions
- Adapt between aggressive/defensive play

### Classical Strategy
RuleBasedAI uses deterministic rules:
- Maximize liberties (freedom)
- Block opponent expansion
- Build connected groups
- Control center territory

## 📊 Example Quantum Output

```
Turn 3 - ZidanAI
Move: (2, 2)
Classification: WINNING
Confidence: 73.5%
Entanglement Score: 0.470

Features:
- Territory Delta: +2
- Liberty Pressure: +3
- Connectivity: +1

Bell Counts: {'00': 512, '11': 381, '01': 89, '10': 42}

Strategy: Aggressive - expand territory/connectivity
```

## 🏆 Win Conditions

### Territory (×2 weight)
Empty cells adjacent to your stones

### Liberties (×1 weight)
Free spaces around each stone

### Connectivity (×3 weight)
Size of largest connected group

**Example:**
```
Territory: 5 × 2 = 10
Liberties: 8 × 1 = 8
Connectivity: 4 × 3 = 12
Total Score: 30
```

## 🎨 UI Features

- **Real-time Updates**: Board refreshes after each move
- **Embedded Visualizations**: Circuit diagrams and histograms in logs
- **Color-coded Logs**: Different colors for each player
- **Winner Banner**: Animated announcement at game end
- **Turn Counter**: Track progress (X/30 turns)
- **Status Panel**: Current player and game state

## ⚡ Performance

- **Circuit Execution**: ~0.5-1 second per move
- **Bell Measurements**: 1024 shots
- **Simulator**: Aer local quantum simulator
- **No Internet Required**: Runs completely offline

## 🔐 Session Management

Each game is stored in server memory with unique session ID. Multiple browser tabs = independent games.

---

**Ready to play? Run `python app.py` and open http://localhost:5000** 🚀

Enjoy your quantum-powered Go experience! ⚛️
