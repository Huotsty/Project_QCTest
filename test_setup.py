"""
Test script to verify quantum components are working
"""
import warnings
warnings.filterwarnings('ignore')

print("Testing Quantum Go components...")
print("=" * 50)

# Test imports
print("\n1. Testing imports...")
try:
    from qiskit import QuantumCircuit
    from qiskit_aer import AerSimulator
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    print("✓ All quantum imports successful!")
except Exception as e:
    print(f"✗ Import error: {e}")
    exit(1)

# Test quantum circuit
print("\n2. Testing quantum circuit creation...")
try:
    qc = QuantumCircuit(5, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    print("✓ Quantum circuit created successfully!")
except Exception as e:
    print(f"✗ Circuit error: {e}")
    exit(1)

# Test simulator
print("\n3. Testing quantum simulator...")
try:
    backend = AerSimulator()
    from qiskit import transpile
    transpiled_qc = transpile(qc, backend)
    job = backend.run(transpiled_qc, shots=100)
    result = job.result()
    counts = result.get_counts()
    print(f"✓ Simulator working! Sample counts: {counts}")
except Exception as e:
    print(f"✗ Simulator error: {e}")
    exit(1)

# Test game components
print("\n4. Testing game components...")
try:
    from game import GameState
    from zidan_ai import ZidanAI
    from rules_ai import RuleBasedAI
    
    game = GameState(mode='A')
    print(f"✓ Game state initialized!")
    print(f"  Board size: 5x5")
    print(f"  Mode: A (ZidanAI vs RuleBasedAI)")
except Exception as e:
    print(f"✗ Game error: {e}")
    exit(1)

# Test ZidanAI
print("\n5. Testing ZidanAI decision making...")
try:
    zidan = ZidanAI(game)
    result = zidan.choose_move()
    print(f"✓ ZidanAI working!")
    print(f"  Classification: {result['classification']}")
    print(f"  Confidence: {result['confidence']:.1f}%")
    print(f"  Entanglement Score: {result['entanglement_score']:.3f}")
    print(f"  Chosen move: ({result['row']}, {result['col']})")
except Exception as e:
    print(f"✗ ZidanAI error: {e}")
    exit(1)

# Test RuleBasedAI
print("\n6. Testing RuleBasedAI...")
try:
    rules = RuleBasedAI(game)
    row, col, rationale = rules.choose_move()
    print(f"✓ RuleBasedAI working!")
    print(f"  Chosen move: ({row}, {col})")
    print(f"  Rationale: {rationale}")
except Exception as e:
    print(f"✗ RuleBasedAI error: {e}")
    exit(1)

# Test Flask
print("\n7. Testing Flask...")
try:
    from flask import Flask
    test_app = Flask(__name__)
    print("✓ Flask working!")
except Exception as e:
    print(f"✗ Flask error: {e}")
    exit(1)

print("\n" + "=" * 50)
print("✓ All tests passed! Ready to run the application.")
print("=" * 50)
print("\nTo start the game:")
print("  Windows: run.bat")
print("  Python:  python app.py")
print("  Or:      python launcher.py")
