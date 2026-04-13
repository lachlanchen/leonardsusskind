# Math Bank
## Core Equations
- \( |0\rangle,\ |1\rangle \). [transcript-backed]
- \( |001011\cdots\rangle \). [transcript-backed]
- \( N_s = 2^n \). [transcript-backed]
- \( n = \log_2 N_s \). [transcript-backed]
- \( \log_2 6 \). [transcript-backed]
- \( A = (A_1,A_2,A_3,A_4) \). [transcript-backed]
- \( \begin{pmatrix} A_1\\ A_2\\ A_3\\ A_4 \end{pmatrix} \). [transcript-backed]
- \( BA = B_1A_1 + B_2A_2 + B_3A_3 + B_4A_4 \). [transcript-backed]
- \( M = (M_{ij}) \). [transcript-backed]
- \( (MA)_1 = M_{11}A_1 + M_{12}A_2 + M_{13}A_3 + M_{14}A_4 \). [transcript-backed]
- \( (MA)_2 = M_{21}A_1 + M_{22}A_2 + M_{23}A_3 + M_{24}A_4 \). [transcript-backed]
- \( e_1 = \begin{pmatrix}1\\0\\0\\0\\ \vdots \end{pmatrix},\ e_2 = \begin{pmatrix}0\\1\\0\\0\\ \vdots \end{pmatrix},\ \ldots \). [standard reconstruction]
- \( P\begin{pmatrix}A\\B\\C\\D\end{pmatrix} = \begin{pmatrix}D\\A\\B\\C\end{pmatrix} \), with \( P = \begin{pmatrix} 0&0&0&1\\ 1&0&0&0\\ 0&1&0&0\\ 0&0&1&0 \end{pmatrix} \). [standard reconstruction]
- \( V' = MV \). [transcript-backed]
- \( V'' = MV' = M^2V \). [transcript-backed]
- \( \text{unitarity} \). [visible]
- \( \begin{pmatrix} m_{11} & m_{12}\\ m_{21} & m_{22} \end{pmatrix} \). [visible]
- \( \begin{pmatrix} m_{11} & m_{12}\\ m_{21} & m_{22} \end{pmatrix} \begin{pmatrix} n_{11} & n_{12}\\ n_{21} & n_{22} \end{pmatrix} \). [standard reconstruction]
- \( C_{11} = m_{11}n_{11} + m_{12}n_{21} \). [transcript-backed]
- \( C_{12} = m_{11}n_{12} + m_{12}n_{22} \). [transcript-backed]
- \( C_{21} = m_{21}n_{11} + m_{22}n_{21} \). [standard reconstruction]
- \( C_{22} = m_{21}n_{12} + m_{22}n_{22} \). [standard reconstruction]
- \( C_{ij} = \sum_k M_{ik}N_{kj} \). [standard reconstruction]
- \( (BM)_j = \sum_i B_i M_{ij} \). [standard reconstruction]
- \( M^{-1} \text{ exists} \). [transcript-backed]
- \( M^{-1}M = MM^{-1} = I \). [standard reconstruction]

## Definitions And Objects
- Bit: a yes/no question, or any two-valued piece of information.
- Classical bit: a two-state system whose quantum aspects are being ignored or suppressed.
- Quantum bit: the quantum analog of the two-valued classical system; promised, not yet developed in this lecture.
- Ket: the bracketed object \( |\cdot\rangle \); introduced already for classical states because it will matter later.
- Multibit configuration: a string of binary values inside a ket, e.g. \( |001011\rangle \).
- Number of states \(N_s\): the count of distinct configurations of the system.
- Configuration: the state of a system at a given instant of time.
- State space: the abstract collection of all configurations, drawn as points in a logical space rather than points in ordinary space.
- Update rule / law of motion: the rule that takes one configuration to the next configuration.
- Deterministic law: from a given present state, the next state is uniquely fixed.
- Reversible law: each state has a unique future and a unique past.
- Unitarity: named here as the quantum analog of uniqueness of past and future; no matrix criterion is yet given in the lecture.
- Row vector: a finite ordered list such as \( (A_1,A_2,A_3,A_4) \).
- Column vector: the same data written vertically.
- Inner product: row times column, producing a scalar.
- Matrix: a square array of numbers acting on a vector to give another vector.
- One-hot state vector: a classical configuration encoded by a column with one \(1\) and all other entries \(0\).
- Matrix inverse: the operator that takes an updated state back to the previous one, when it exists.

## Derivation Steps
State counting for bits:
1. One bit has \(2\) possible states.
2. Two bits have \(2\times 2 = 2^2\) states.
3. By the same pattern, \(n\) bits have \(2^n\) states.
4. This is recorded as \(N_s = 2^n\).
5. Inverting gives \(n = \log_2 N_s\).

Generalized information content:
1. Start from the rule “bits of information = logarithm base two of the number of states.”
2. Apply it first to systems with \(N_s = 2^n\), recovering an integer \(n\).
3. Apply it next to a die with \(N_s=6\).
4. Obtain \(\log_2 6\), showing that the information measure need not be an integer.
5. Keep the definition, not the integrality, as the main point.

Representing continuous data by bits:
1. Choose a finite accuracy for the quantity of interest.
2. Write the resulting approximated number in base two.
3. For a field, divide space into cells.
4. Record the approximated value in each cell as a binary string.
5. Concatenate the cell data into one long binary description.

Representing particle occupancy by bits:
1. Discretize space into cells.
2. Ask for each cell: occupied or empty?
3. Write \(1\) for occupied and \(0\) for empty.
4. Read the full occupancy pattern as a long binary string.
5. Treat that string as the configuration of the system.

Reversibility from the state-space diagrams:
1. Draw each configuration as a point.
2. Draw one outgoing arrow from each point to encode the next state.
3. If two distinct states flow into one state, the future is still defined but the past is not recoverable.
4. That means information has been lost.
5. Fundamental classical physics rejects such information-losing laws at the fine-grained level.
6. Acceptable classical laws therefore have unique future and unique past.

Matrix-times-vector rule:
1. Take the first row of \(M\).
2. Multiply it by the column vector \(A\) using the inner-product rule.
3. Put that scalar in the first output slot.
4. Repeat with the second row for the second output slot.
5. Continue row by row until the new column vector is complete.

Classical update as a permutation matrix:
1. Encode a configuration by a one-hot column vector.
2. Choose a matrix that moves the single \(1\) one slot with wrap-around.
3. Act on a basis vector to move from one configuration to the next.
4. Act on a general column \( (A,B,C,D)^T \) to shift entries cyclically.
5. Interpret repeated action as repeated time evolution.

Matrix-matrix multiplication from repeated updating:
1. Write one update as \(V' = MV\).
2. Write the next update as \(V'' = MV'\).
3. Substitute \(V' = MV\).
4. Obtain \(V'' = M^2V\).
5. Conclude that multiplying matrices composes successive updates.
6. Read each entry of the product by row-column multiplication.

Row-vector times matrix:
1. Keep the input row vector fixed.
2. Multiply it by the first column of the matrix to get the first output entry.
3. Multiply it by the second column to get the second output entry.
4. Continue across the matrix.
5. The result is another row vector.

## Notation Choices
- Use \(n\) for number of bits and \(N_s\) for number of states, matching the lecture.
- Keep classical two-state labels as \( |0\rangle \) and \( |1\rangle \), since Susskind explicitly introduces Dirac notation before qubits.
- For multibit classical configurations, keep ket strings such as \( |001011\rangle \) without adding tensor-product notation yet.
- Use \(A_i\) for generic vector components and \(B_i\) for a second row vector in the inner-product discussion.
- Read matrix indices as \(M_{ij}\) with \(i=\) row and \(j=\) column.
- Treat vector and matrix entries as real numbers in this lecture; complex numbers, daggers, and conjugation are deferred.
- Use \(V, V', V''\) for states related by updating in the abstract matrix discussion.
- For classical configuration-space basis states, use one-hot column vectors \(e_i\) as the clean note-writing convention; explain that this is the linear-algebra encoding of “a one somewhere and zeros elsewhere.”
- For the cyclic update matrix, fix one convention once and state it explicitly; the lecture itself flips the direction live on the board.
- Use “reversibility” and “uniqueness of past and future” for the classical discussion; reserve “unitarity” for the quantum analog only.
- Do not introduce \(U^\dagger U = I\) in the lecture prose itself unless clearly marked as a later formalization, because the lecture has not reached that criterion yet.

## Uncertain Mathematics
- The five-state update matrix is not cleanly completed on the board; Susskind abandons it and switches to four dimensions.
- The direction of the cyclic shift is unstable in the live derivation: he first gets the orientation wrong, then corrects it. Any explicit permutation matrix in the notes is a chosen convention, not a literal board transcription.
- The compact formulas \(C_{ij}=\sum_k M_{ik}N_{kj}\) and \((BM)_j=\sum_i B_iM_{ij}\) are faithful condensations, but the sigma notation itself is editorial.
- `lecture_01_figure_04.png` supports the presence of a matrix acting on a vector, not exact micro-legible entries.
- `lecture_01_figure_05.png` clearly supports the left matrix and the column-by-column interpretation of the right matrix, but not every subscript nor the final written output entries.
- The reversibility condition is stated conceptually first and only later phrased in terms of matrix inverses during questions. Do not front-load the inverse language too early in the chapter.
- The lecture names unitarity but does not yet define it as a unitary matrix condition. Do not import \(U^\dagger U=I\) into Lecture 1 as if it had already been derived.
- The distinction between time reversibility and time-reversal symmetry is handled informally and should remain cautious in the final notes.
- The classical discussion of infinite precision and infinitely many bits is qualitative; do not formalize it into stronger mathematical claims than the lecture makes.
- The garbled orbital/configuration segment supports only the secure claims: configuration is the state at an instant, space and time may be discretized, and dynamics is an update rule.