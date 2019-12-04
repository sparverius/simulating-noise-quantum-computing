from qiskit import QuantumCircuit
from qiskit import QiskitError, execute, BasicAer

circ = QuantumCircuit.from_qasm_file("entangled_registers.qasm")
print(circ)

# See the backend
sim_backend = BasicAer.get_backend('qasm_simulator')

# Compile and run the Quantum circuit on a local simulator backend
job_sim = execute(circ, sim_backend)
sim_result = job_sim.result()

# Show the results
print("simulation: ", sim_result)
print(sim_result.get_counts(circ))
