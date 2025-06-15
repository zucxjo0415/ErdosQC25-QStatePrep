from qiskit.circuit import QuantumCircuit, QuantumRegister, AncillaRegister
import numpy as np

def stateprep_r(amp, phase, reg):
    # helper function that is called recursively
    n = reg.size
    K = amp.size
    k = int(np.log2(K))
    stateprep_circ = QuantumCircuit(reg, name="U_psi")
    
    # amplitude preparation
    if sum(amp**2) > 0: 
        ampang = 2*np.arccos(np.sqrt(sum(amp[:(K>>1)]**2) / sum(amp**2)))
        stateprep_circ.sdg(reg[k-1])
        stateprep_circ.h(reg[k-1])
        if k < n: 
            stateprep_circ.mcrz(ampang,reg[k:],reg[k-1])
        else: 
            stateprep_circ.rz(ampang,reg[k-1])
        stateprep_circ.h(reg[k-1])
        stateprep_circ.s(reg[k-1])

    # phase preparation
    theta = (sum(phase[K>>1:])-sum(phase[:K>>1]))/(1<<(k-1))
    if k < n: 
        stateprep_circ.mcrz(theta,reg[k:],reg[k-1])
    else: 
        stateprep_circ.rz(theta,reg[k-1])

    # recursively prepare less significant qubits
    if k > 1:
        stateprep_circ.x(reg[k-1])
        stateprep_circ.compose(stateprep_r(amp[:K>>1],phase[:K>>1],reg),inplace=True) 
        stateprep_circ.x(reg[k-1])
        stateprep_circ.compose(stateprep_r(amp[K>>1:],phase[K>>1:],reg),inplace=True) 

    return stateprep_circ

def stateprep(psi):
    # main function
    n = int(np.log2(psi.size))
    if n < np.log2(psi.size): raise Exception("Input vector of wrong size!")

    reg = QuantumRegister(size = n, name="x")
    return stateprep_r(np.abs(psi), np.angle(psi), reg)
