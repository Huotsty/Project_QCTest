# 📸 Quantum Go - Example Game Outputs

## 🎮 Sample Game Session (Mode A)

### Turn 1: ZidanAI
```
Player: ZidanAI
Move: (2, 2)

Rationale: WINNING (conf=68.2%): Aggressive: expand territory/connectivity

🔮 Quantum Analysis:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Classification: WINNING
Confidence: 68.2%
Entanglement Score: 0.364

Features:
  Territory Delta: 0
  Liberty Pressure: 0
  Connectivity: 0

Bell State Measurements (1024 shots):
  |00⟩: 489 (47.8%)
  |11⟩: 397 (38.8%)
  |01⟩: 78 (7.6%)
  |10⟩: 60 (5.9%)

Strategy: Aggressive positioning
Target: Center control (2,2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Board State:
  0 1 2 3 4
0 . . . . .
1 . . . . .
2 . . Z . .
3 . . . . .
4 . . . . .
```

### Turn 2: RuleBasedAI
```
Player: RuleBasedAI
Move: (2, 3)

Rationale: Move (2,3): blocks opponent (1 adj), center control [score=14.0]

Board State:
  0 1 2 3 4
0 . . . . .
1 . . . . .
2 . . Z R .
3 . . . . .
4 . . . . .
```

### Turn 3: ZidanAI
```
Player: ZidanAI
Move: (1, 2)

Rationale: WINNING (conf=72.5%): Aggressive: expand territory/connectivity

🔮 Quantum Analysis:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Classification: WINNING
Confidence: 72.5%
Entanglement Score: 0.451

Features:
  Territory Delta: 1
  Liberty Pressure: 2
  Connectivity: 1

Bell State Measurements (1024 shots):
  |00⟩: 521 (50.9%)
  |11⟩: 412 (40.2%)
  |01⟩: 58 (5.7%)
  |10⟩: 33 (3.2%)

Strategy: Aggressive - building connectivity
Target: Adjacent to existing stone
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Board State:
  0 1 2 3 4
0 . . . . .
1 . . Z . .
2 . . Z R .
3 . . . . .
4 . . . . .
```

### Turn 15: ZidanAI (Defensive Example)
```
Player: ZidanAI
Move: (2, 1)

Rationale: LOSING (conf=45.8%): Defensive: block opponent/preserve liberties

🔮 Quantum Analysis:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Classification: LOSING
Confidence: 45.8%
Entanglement Score: -0.084

Features:
  Territory Delta: -2
  Liberty Pressure: -1
  Connectivity: 0

Bell State Measurements (1024 shots):
  |00⟩: 234 (22.9%)
  |11⟩: 242 (23.6%)
  |01⟩: 278 (27.1%)
  |10⟩: 270 (26.4%)

Strategy: Defensive - blocking opponent expansion
Target: Block RuleBasedAI group
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Board State:
  0 1 2 3 4
0 . . Z R .
1 . . Z R .
2 . Z Z R .
3 . . Z . .
4 . . . . .
```

## 🏆 Game End Example

```
═══════════════════════════════════════════════════════
                    GAME OVER!
═══════════════════════════════════════════════════════

Final Board:
  0 1 2 3 4
0 Z . Z R .
1 Z . Z R .
2 . Z Z R .
3 . Z Z R R
4 . . Z . .

Turn Count: 25 / 30

Final Scores:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ZidanAI (Blue):
  Territory:     8 cells  → 8 × 2 = 16
  Liberties:     18       → 18 × 1 = 18
  Connectivity:  9        → 9 × 3 = 27
  ─────────────────────────────────
  TOTAL SCORE:                 61

RuleBasedAI (Red):
  Territory:     6 cells  → 6 × 2 = 12
  Liberties:     14       → 14 × 1 = 14
  Connectivity:  7        → 7 × 3 = 21
  ─────────────────────────────────
  TOTAL SCORE:                 47

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🏆 WINNER: ZidanAI 🏆

Quantum advantage: +14 points
Win margin: 29.8%

═══════════════════════════════════════════════════════
```

## 🎯 Mode B Example (Human vs ZidanAI)

### Turn 1: Human
```
Player: Human
Move: (2, 2)
Rationale: Human player move

Board State:
  0 1 2 3 4
0 . . . . .
1 . . . . .
2 . . H . .
3 . . . . .
4 . . . . .
```

### Turn 2: ZidanAI Response
```
Player: ZidanAI
Move: (2, 3)

Rationale: WINNING (conf=65.3%): Aggressive: expand territory/connectivity

🔮 Quantum Analysis:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Classification: WINNING
Confidence: 65.3%
Entanglement Score: 0.306

Features:
  Territory Delta: 0
  Liberty Pressure: 0
  Connectivity: 0

Bell State Measurements (1024 shots):
  |00⟩: 476 (46.5%)
  |11⟩: 394 (38.5%)
  |01⟩: 92 (9.0%)
  |10⟩: 62 (6.1%)

Strategy: Mirror human move with adjacent placement
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Board State:
  0 1 2 3 4
0 . . . . .
1 . . . . .
2 . . H Z .
3 . . . . .
4 . . . . .
```

## 📊 Statistics Example

### Quantum Analysis Over Game
```
Turn Distribution:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WINNING  ████████████░░░ 72%
LOSING   ████░░░░░░░░░░░ 28%

Average Confidence: 67.3%

Entanglement Score Range:
  Maximum:  +0.672 (Turn 8)
  Minimum:  -0.234 (Turn 17)
  Average:  +0.218

Bell State Distribution (Total):
  |00⟩: 9,847 (48.1%)  ████████████
  |11⟩: 8,123 (39.7%)  ██████████
  |01⟩: 1,456 (7.1%)   ██
  |10⟩: 1,038 (5.1%)   █
```

### Strategy Breakdown
```
ZidanAI Move Types:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Aggressive:  █████████ 65%
Defensive:   ████░░░░░ 35%

RuleBasedAI Move Types:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Center:      ████░░░░░ 30%
Blocking:    ██████░░░ 40%
Connecting:  ████░░░░░ 30%
```

## 🔮 Quantum Circuit Visualization

### Example Circuit Diagram
```
     ┌────────┐                    
q_0: ┤ Ry(θ₁) ├──■─────────────────
     ├────────┤  │                 
q_1: ┤ Ry(θ₂) ├──┼────■────────────
     ├────────┤  │    │            
q_2: ┤ Ry(θ₃) ├──┼────┼────■───────
     ├───┐    │  │    │    │       
q_3: ┤ H ├────┼──X────X────┤ H ├──■──
     ├───┤    │            └───┘  │  
q_4: ┤ H ├────┼───────────────────X──
     └───┘    │                      
c: 2/═════════╩════════════════════╬═
              0                    1
```

### Example Histogram
```
Bell State Measurement Counts

500 │                  
    │         ███      
400 │         ███ ███  
    │         ███ ███  
300 │         ███ ███  
    │         ███ ███  
200 │         ███ ███  
    │         ███ ███  
100 │  ███    ███ ███  ███
    │  ███    ███ ███  ███
  0 └──┴──────┴───┴────┴──
     |00⟩   |11⟩  |01⟩ |10⟩
```

## 📝 Game Log Format (JSON)

```json
{
  "turn": 5,
  "player": "ZidanAI",
  "move": "(2, 1)",
  "rationale": "WINNING (conf=71.2%): Aggressive: expand territory/connectivity",
  "features": {
    "territory_delta": 2,
    "liberty_pressure": 3,
    "connectivity": 1
  },
  "classification": "WINNING",
  "confidence": "71.2%",
  "entanglement_score": "0.424",
  "bell_counts": {
    "00": 512,
    "11": 389,
    "01": 71,
    "10": 52
  },
  "circuit_image": "iVBORw0KGgoAAAANS...",
  "histogram_image": "iVBORw0KGgoAAAANS...",
  "board": "  0 1 2 3 4\n0 . . Z R .\n1 . Z Z R .\n..."
}
```

## 🎮 UI Screenshots Description

### Main Page (Before Game)
```
╔════════════════════════════════════════════════╗
║         ⚛️ Quantum Go - ZidanAI               ║
║  Experience quantum-powered strategic gameplay ║
╠════════════════════════════════════════════════╣
║                                                ║
║  Mode Selection:                               ║
║  ┌──────────────┐  ┌──────────────┐          ║
║  │   Mode A     │  │   Mode B     │          ║
║  │   ZidanAI    │  │   Human      │          ║
║  │     vs       │  │     vs       │          ║
║  │ RuleBasedAI  │  │  ZidanAI     │          ║
║  └──────────────┘  └──────────────┘          ║
║                                                ║
║  ┌──────────────────────────────────┐         ║
║  │      Start New Game              │         ║
║  └──────────────────────────────────┘         ║
║                                                ║
║  Game Status:                                  ║
║  Mode: Not started                             ║
║  Turn: 0 / 30                                  ║
║  Current Player: -                             ║
║  Status: Waiting to start                      ║
║                                                ║
║  ╔════════════════════���                        ║
║  ║   Game Board       ║                        ║
║  ║                    ║                        ║
║  ║   □ □ □ □ □       ║                        ║
║  ║   □ □ □ □ □       ║                        ║
║  ║   □ □ □ □ □       ║                        ║
║  ║   □ □ □ □ □       ║                        ║
║  ║   □ □ □ □ □       ║                        ║
║  ╚════════════════════╝                        ║
║                                                ║
║  Game Log:                                     ║
║  Game log will appear here...                  ║
╚════════════════════════════════════════════════╝
```

### During Game (Mode A)
```
╔════════════════════════════════════════════════╗
║  Turn: 8 / 30                                  ║
║  Current Player: ZidanAI                       ║
║  Status: Game in progress                      ║
║                                                ║
║  ╔════════════════════╗                        ║
║  ║   Game Board       ║                        ║
║  ║                    ║                        ║
║  ║   . . Z R .        ║                        ║
║  ║   . Z Z R .        ║                        ║
║  ║   . Z . R .        ║                        ║
║  ║   . . . . .        ║                        ║
║  ║   . . . . .        ║                        ║
║  ╚════════════════════╝                        ║
║                                                ║
║  ┌──────────────────────────────────┐         ║
║  │      Next Turn  ⚛️                │         ║
║  └──────────────────────────────────┘         ║
║                                                ║
║  Game Log:                                     ║
║  ┌────────────────────────────────────────┐   ║
║  │ Turn 8 - ZidanAI                       │   ║
║  │ Move: (2, 1)                           │   ║
║  │ WINNING (conf=73.8%)                   │   ║
║  │                                        │   ║
║  │ 🔮 Quantum Analysis:                   │   ║
║  │ Entanglement Score: 0.476              │   ║
║  │ Bell: {00:524, 11:403, 01:61, 10:36}  │   ║
║  │                                        │   ║
║  │ [Circuit Diagram]                      │   ║
║  │ [Histogram Chart]                      │   ║
║  └────────────────────────────────────────┘   ║
╚════════════════════════════════════════════════╝
```

### Game Over
```
╔════════════════════════════════════════════════╗
║  ┌──────────────────────────────────────────┐ ║
║  │     🏆 Game Over! Winner: ZidanAI 🏆     │ ║
║  └──────────────────────────────────────────┘ ║
║                                                ║
║  Final Board:                                  ║
║  ╔════════════════════╗                        ║
║  ║   Z . Z R .        ║                        ║
║  ║   Z . Z R .        ║                        ║
║  ║   . Z Z R .        ║                        ║
║  ║   . Z Z R R        ║                        ║
║  ║   . . Z . .        ║                        ║
║  ╚════════════════════╝                        ║
║                                                ║
║  ZidanAI Score: 61                             ║
║  RuleBasedAI Score: 47                         ║
║                                                ║
║  Turn Count: 25 / 30                           ║
╚════════════════════════════════════════════════╝
```

## 🧪 Test Output Example

```bash
$ python test_setup.py

Testing Quantum Go components...
==================================================

1. Testing imports...
✓ All quantum imports successful!

2. Testing quantum circuit creation...
✓ Quantum circuit created successfully!

3. Testing quantum simulator...
✓ Simulator working! Sample counts: {'00': 52, '11': 48}

4. Testing game components...
✓ Game state initialized!
  Board size: 5x5
  Mode: A (ZidanAI vs RuleBasedAI)

5. Testing ZidanAI decision making...
✓ ZidanAI working!
  Classification: WINNING
  Confidence: 68.5%
  Entanglement Score: 0.370
  Chosen move: (2, 2)

6. Testing RuleBasedAI...
✓ RuleBasedAI working!
  Chosen move: (2, 1)
  Rationale: Move (2,1): high liberties (4), center control [score=16.0]

7. Testing Flask...
✓ Flask working!

==================================================
✓ All tests passed! Ready to run the application.
==================================================

To start the game:
  Windows: run.bat
  Python:  python app.py
  Or:      python launcher.py
```

---

**These examples demonstrate the complete functionality of the Quantum Go application!** 🎮⚛️
