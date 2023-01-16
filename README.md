# Single-Reads-Assemble
<p>you should assemble two types of reads using the De Bruijn graph representation and the Eulerian path to obtain the original sequence from that representation.</p>
<b>Short reads with the same size</b>

Input : Your program should be able to read a file.
The first line would be: - the length of the sequences.
                         - Each read will take one.
Output : The program then outputs the assembled sequence to the screen.


<h1>Explain</h1>

<b>READS</b> 
<p>CTTA</p>
<p>ACCA</p>
<p>TACC</p>
<p>GGCT</p>
<p>GCTT</p>
<p>TTAC</p>

<b>GRAPH</b> 
<p>CTT --> TTA</p>
<p>ACC --> CCA(E)</p>
<p>TAC --> ACC</p>
<p>(S)GGC --> GCT</p>
<p>GCT --> CTT</p>
<p>TTA --> TAC</p>


<b>PATHS</b> 
<p>GGC -> GCT -> CCT -> TTA -> TAC -> ACC -> CCA</p>
<p>Get first 3 letters in first one and then get last letter in others</p>


<h2>the final result should be like</h2>
<p>Genome = GGCTTACCA</p>
