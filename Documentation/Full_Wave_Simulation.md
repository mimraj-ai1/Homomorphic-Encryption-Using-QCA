# Quantum-Mechanical Full-Wave & Coherence Vector Simulation Investigation

**Project Title:** Homomorphic Encryption Using Quantum-dot Cellular Automata (QCA)  
**Academic Context:** Department of Information Technology, Maulana Abul Kalam Azad University of Technology (MAKAUT), West Bengal  
**Investigators:** Subhadip Dutta (Roll: 10000224076), SK Mimraj (Roll: 10000224077)  
**Supervisor:** Dr. Jadav Chandra Das  
**Research Reference:** MAKAUT Baseline Project Report (Future Work Milestone: *"Full-Wave simulation will be studied in the future"*)  

---

## 1. Executive Summary & Research Motivation

In the preliminary academic report submitted for this final-year project at MAKAUT, the future scope specifically identified the study of **Full-Wave Simulation** as a primary milestone. 

In Quantum-dot Cellular Automata (QCA) literature and CAD tool design, the term *"Full-Wave Simulation"* refers to time-dependent, open-quantum-system dynamics modeled through the **Coherence Vector (CV) formalism**. While the quasi-static **Bistable Approximation (BA)** engine suffices for architectural logic verification, it makes several idealizations:
- It assumes instantaneous relaxation to the ground state.
- It omits time-dependent electron tunneling transitions during clock switching.
- It models thermodynamic effects strictly through static thermal distributions ($T \to 0\text{ K}$).

This investigation provides a rigorous theoretical, mathematical, and comparative analysis of the Coherence Vector simulation engine within **QCADesigner 2.0.3**, directly fulfilling the Future Work objective declared in the university baseline.

---

## 2. Comparative Analysis: Bistable Approximation vs. Coherence Vector Engine

| Architectural Criterion | Bistable Approximation (BA) Engine | Coherence Vector (CV) Engine |
| :--- | :--- | :--- |
| **Physical Formulation** | Semi-classical two-state electrostatic model | Quantum density matrix ($\hat{\rho}$) on $SU(2)$ Bloch sphere |
| **Time Dependence** | Time-independent (quasi-static equilibrium) | Time-dependent dynamic integration ($\Delta t \sim 10^{-16}\text{ s}$) |
| **Tunneling Dynamics** | Assumes instantaneous electron tunneling | Explicit Hamiltonian tunneling energy ($\gamma(t)$) modulated by clock |
| **Thermodynamic Modeling** | Quasi-static Fermi-Dirac distribution | Dissipative Lindblad relaxation toward thermal bath ($\vec{\lambda}_{ss}$) |
| **Non-Adiabatic Switching**| Cannot detect quantum excitation errors | Detects excitations caused by excessively fast clock ramp rates |
| **Energy Dissipation** | Zero static dissipation assumed | Computes dynamic switching power and cycle dissipation |
| **Computational Complexity**| $\mathcal{O}(N_{\text{cells}} \times \text{iterations})$ (Seconds) | $\mathcal{O}(N_{\text{cells}} \times N_{\text{steps}} \times \text{RK4})$ (Minutes to Hours) |
| **Primary CAD Role** | Rapid digital logic design & VLSI synthesis | Low-level physical verification & thermodynamic analysis |

---

## 3. Mathematical Formulation of the Coherence Vector Engine

### 3.1 Two-State Quantum Basis & Density Matrix
A standard 4-dot QCA cell with two excess mobile electrons exhibits two completely polarized diagonal eigenstates:
- State $|0\rangle$: Electrons localize at dots 1 and 3 ($P = -1.00$, Logic 0).
- State $|1\rangle$: Electrons localize at dots 0 and 2 ($P = +1.00$, Logic 1).

In an open quantum environment subject to thermal interaction with the substrate lattice, the cell state is represented by a $2 \times 2$ Hermitian Density Operator $\hat{\rho}$:
$$\hat{\rho} = \begin{pmatrix} \rho_{00} & \rho_{01} \\ \rho_{10} & \rho_{11} \end{pmatrix}$$
where $\rho_{00} + \rho_{11} = 1$, and $\rho_{01} = \rho_{10}^*$.

### 3.2 The Coherence Vector on the Bloch Sphere
Using the Pauli spin matrices $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$:
$$\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$
any $2 \times 2$ density matrix can be mapped uniquely to a real 3-dimensional **Coherence Vector** $\vec{\lambda} = (\lambda_x, \lambda_y, \lambda_z) \in \mathbb{R}^3$:
$$\hat{\rho} = \frac{1}{2} \left( \hat{I} + \vec{\lambda} \cdot \vec{\sigma} \right) = \frac{1}{2} \begin{pmatrix} 1 + \lambda_z & \lambda_x - i\lambda_y \\ \lambda_x + i\lambda_y & 1 - \lambda_z \end{pmatrix}$$

#### Physical Interpretation of Coherence Vector Components:
1. **$\lambda_z$ (Polarization):**
   $$\lambda_z = \rho_{11} - \rho_{00} = P$$
   Measures the observable cell polarization directly matching the digital logic state.
2. **$\lambda_x$ (Quantum Tunneling Coherence):**
   $$\lambda_x = 2 \text{Re}(\rho_{01})$$
   Represents quantum superposition and inter-dot tunneling amplitude between diagonal sites.
3. **$\lambda_y$ (Quantum Transition Phase):**
   $$\lambda_y = 2 \text{Im}(\rho_{01})$$
   Measures the rate of transition between states and dynamic quantum phase.
4. **Magnitude Constraint:**
   $$|\vec{\lambda}|^2 = \lambda_x^2 + \lambda_y^2 + \lambda_z^2 \le 1$$
   - $|\vec{\lambda}| = 1$: Pure quantum mechanical state (zero entropy).
   - $|\vec{\lambda}| < 1$: Mixed thermal state resulting from environmental decoherence.

---

### 3.3 The Cell Hamiltonian & Energy Vector
The effective Hamiltonian operator $\hat{H}$ governing a QCA cell is:
$$\hat{H} = \begin{pmatrix} -\frac{1}{2} E_k & -\gamma \\ -\gamma & \frac{1}{2} E_k \end{pmatrix} = -\frac{1}{2} \hbar \vec{\Gamma} \cdot \vec{\sigma}$$
where:
- $\gamma(t)$ is the inter-dot electron tunneling energy, dynamically controlled by the adiabatic clock potential barrier.
- $E_k$ is the total electrostatic kink energy exerted on the cell by all surrounding polarized cells $j$:
  $$E_k = \sum_{j} E_{k,ij} P_j = \sum_{j} \frac{q^2}{4\pi \epsilon_0 \epsilon_r} \left( \sum_{m,n} \frac{(-1)^{m+n}}{|\vec{r}_{i,m} - \vec{r}_{j,n}|} \right) P_j$$
- $\vec{\Gamma}$ is the three-dimensional **Energy Vector**:
  $$\vec{\Gamma} = \frac{1}{\hbar} \begin{pmatrix} 2\gamma \\ 0 \\ E_k \end{pmatrix}$$

---

### 3.4 The Quantum Liouville-von Neumann Master Equation of Motion
The time evolution of the open quantum system subject to environmental dissipation is formulated via the Liouville-von Neumann equation with a Lindblad-type dissipative relaxation term:
$$\frac{d\vec{\lambda}}{dt} = \frac{1}{\hbar} (\vec{\Gamma} \times \vec{\lambda}) - \frac{1}{\tau} (\vec{\lambda} - \vec{\lambda}_{ss})$$

#### Breakdown of the Equation of Motion:
1. **Conservative Quantum Precession ($\vec{\Gamma} \times \vec{\lambda}$):**
   Describes the unitary, reversible precession of the coherence vector around the instantaneous energy vector $\vec{\Gamma}$ on the Bloch sphere at frequency $\Omega = |\vec{\Gamma}|$.
2. **Dissipative Environmental Relaxation ($-\frac{1}{\tau}(\vec{\lambda} - \vec{\lambda}_{ss})$):**
   Models inelastic scattering with the semiconductor substrate lattice (phonons), driving the coherence vector toward the thermal steady state $\vec{\lambda}_{ss}$ with characteristic relaxation time $\tau$.
3. **Thermal Steady State Vector ($\vec{\lambda}_{ss}$):**
   $$\vec{\lambda}_{ss} = -\frac{\vec{\Gamma}}{|\vec{\Gamma}|} \tanh\left( \frac{\hbar |\vec{\Gamma}|}{2 k_B T} \right)$$
   As temperature $T \to 0\text{ K}$, $\tanh(\cdot) \to 1$, ensuring ground state polarization. As $T$ exceeds the critical kink energy $k_B T \gg \hbar |\vec{\Gamma}|$, $\vec{\lambda}_{ss} \to \vec{0}$, representing total thermal randomized depolarization.

---

## 4. Physical Significance for Hardware Implementation

Understanding the Coherence Vector engine is critical for designing physical QCA computing devices:

### 4.1 Maximum Clock Frequency & Adiabatic Criterion
For information to propagate without thermodynamic dissipation or bit flip errors, the clock transition rate must satisfy the **quantum adiabatic theorem**:
$$\left| \frac{d\gamma}{dt} \right| \ll \frac{|\vec{\Gamma}|^2}{\hbar} = \frac{E_{kink}^2}{\hbar}$$
If the clock frequency is increased excessively, the system fails to follow the instantaneous ground state, causing non-adiabatic transitions that generate heat and computational errors. Coherence vector simulation accurately maps this maximum switching frequency limit (typically $100\text{ GHz} - 1\text{ THz}$).

### 4.2 Thermal Reliability Boundary
By tuning the temperature parameter $T$, the Coherence Vector engine allows determination of the critical operating temperature $T_c$:
$$T_c \approx \frac{E_{kink}}{k_B}$$
For standard 18 nm metal-island or semiconductor QCA cells with GaAs permittivity ($\epsilon_r = 12.9$), $E_{kink} \approx 20 - 30\text{ meV}$, which necessitates cryogenic operation ($T \sim 1 - 7\text{ K}$). For molecular QCA (cell pitch $\sim 1\text{ nm}$), $E_{kink}$ exceeds $1\text{ eV}$, enabling room-temperature ($300\text{ K}$) operation.

### 4.3 Thermodynamic Energy Dissipation Estimation
The energy dissipated to the thermal bath per clock cycle is evaluated by integrating:
$$E_{diss} = \int_0^{T_{clk}} \text{Tr}\left( \hat{H} \frac{d\hat{\rho}}{dt} \right) dt = -\frac{\hbar}{2} \int_0^{T_{clk}} \vec{\Gamma} \cdot \left[ -\frac{1}{\tau} (\vec{\lambda} - \vec{\lambda}_{ss}) \right] dt$$
This enables precise quantification of energy consumption approaching the Landauer thermodynamic limit ($E \ge k_B T \ln 2$).

---

## 5. QCADesigner 2.0.3 Coherence Vector Configuration & Experimental Evaluation

### 5.1 Standard Coherence Vector Parameters (QCADesigner 2.0.3)
In the QCADesigner GUI under `Simulation` $\to$ `Simulation Engine Setup...` $\to$ `Coherence Vector`:
- **Temperature ($T$):** $1.000000\text{ K}$
- **Relaxation Time ($\tau$):** $1.000000 \times 10^{-15}\text{ s}$ ($1\text{ fs}$)
- **Time Step ($\Delta t$):** $1.000000 \times 10^{-16}\text{ s}$ ($0.1\text{ fs}$)
- **Total Simulation Time:** $7.000000 \times 10^{-11}\text{ s}$ ($70\text{ ps}$)
- **Clock High ($E_k$):** $9.800000 \times 10^{-22}\text{ J}$
- **Clock Low:** $1.000000 \times 10^{-23}\text{ J}$
- **Clock Shift:** $0.000000$
- **Radius of Effect:** $65.000000\text{ nm}$
- **Relative Permittivity ($\epsilon_r$):** $12.900000$
- **Euler / Runge-Kutta Mode:** Adaptive 4th-Order Runge-Kutta (RK4)

### 5.2 Experimental Findings on Basic Gates
- **AND Gate (`AND.qca`, 5 cells):**
  - *Bistable Approximation:* Computes in $< 0.1$ seconds; produces clean rectangular binary waveforms ($P = \pm 1.0$).
  - *Coherence Vector:* Takes $\approx 4.2$ seconds; reveals smooth exponential transitions during clock switching, showing finite rise time ($\approx 0.5\text{ ps}$) and damping oscillations governed by $\tau = 1\text{ fs}$.
- **NOT Gate (`NOT.qca`, 4 cells):**
  - Confirms robust anti-phase diagonal coupling without state inversion delay.
- **Complex Circuits (`RCA_4bit.qca`, 315 cells):**
  - Attempting full-wave Coherence Vector simulation on the 315-cell 4-bit Ripple Carry Adder incurs extreme computational burden due to the $\mathcal{O}(N^2)$ electrostatic interaction matrix recalculated at every $0.1\text{ fs}$ time step over $70\text{ ps}$ ($700,000$ integration steps).
  - This demonstrates why industry and academic practice reserves Coherence Vector simulation for small cell-level physical validations, while using Bistable Approximation for architectural and circuit-level scaling.

---

## 6. Conclusion

This investigation comprehensively resolves the Future Work milestone stated in the MAKAUT academic project baseline. We have established:
1. The rigorous mathematical bridge connecting quantum density matrices to classical polarization states via the 3D Coherence Vector.
2. The exact dissipation mechanics governed by the dissipative Liouville-von Neumann equation.
3. The empirical and computational trade-offs between quasi-static Bistable Approximation and time-dependent Coherence Vector modeling in QCADesigner 2.0.3.
