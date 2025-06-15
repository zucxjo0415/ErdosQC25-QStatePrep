# ErdosQC25-QStatePrep

Implements a Qiskit function `stateprep` that takes a numpy vector $\psi \in \mathbb{C}^{2^n}$ with $L^2$-norm 1, and outputs a circuit $U_\psi$, using multicontrolled Z rotations, $S$, $S^\dagger$, $H$ and $X$ gates such that

$$ U_\psi |0\rangle_n = \sum_{x=0}^{2^n−1} \psi_x |x\rangle_n .$$

The circuit is built recursively, and uses $O(2^n)$ gates at $O(2^n)$ depth (where $n$ is the number of qubits). 

The function (including all the necessary auxiliary functions) can be found in the Python script file `qstateprep.py`.

The Jupyter notebook `Quantum State Prep.ipynb` has documented code, including a brief explanation of the construction and demonstrations.
