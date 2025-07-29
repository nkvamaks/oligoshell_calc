<h2 class="mb-4"> About OligoShell Calculator: </h2>

<details>
<summary><b>Local Installation and Usage</b></summary>
<br/>
<ol>
  <li>
    <strong>Clone the repository from the <code>joss</code> branch</strong><br>
    <pre><code>git clone -b joss --single-branch https://github.com/nkvamaks/oligoshell_calc.git
cd oligoshell_calc</code></pre>
  </li>

  <li>
    <strong>Create a virtual environment</strong><br>
    <pre><code>python3 -m venv venv</code></pre>
  </li>

  <li>
    <strong>Activate the virtual environment</strong><br>
    <pre><code>source ./venv/bin/activate</code></pre>
  </li>

  <li>
    <strong>Install required packages</strong><br>
    <pre><code>pip3 install -r requirements.txt</code></pre>
  </li>

  <li>
    <strong>Run migrations</strong><br>
    <pre><code>python3 manage.py makemigrations
python3 manage.py migrate</code></pre>
  </li>

  <li>
    <strong>Run the development server</strong><br>
    <pre><code>python3 manage.py runserver</code></pre>
  </li>

  <li>
    <strong>Open the application in your browser</strong><br>
    <pre><code>http://localhost:8000</code></pre>
  </li>
</ol>
</details>

<br/>
<p>
OligoShell Calculator is a comprehensive web application designed for calculating various properties of natural (DNA, RNA), 
modified, therapeutic oligonucleotides, as well as phosphorodiamidate morpholino oligos (PMO), 
thiomorpholino oligos (TMO), morpholino oligos (MO), and different chimeras with available nucleic acids. Our tool offers 
advanced features that meet the needs of researchers and professionals in the fields of nucleic acid chemistry and molecular biology.
</p>
<p>
<strong>Key Features:</strong>
</p>
<ul>
    <li>
        <sup><strong>NEW!</strong></sup>
        Calculate properties of phosphorodiamidate morpholino oligos (PMO), thiomorpholino oligos (TMO), morpholino oligos (MO), and various chimeric oligonucleotides.
    </li>
    <li>
        Compose oligonucleotides with different backbones including phosphodiester, phosphorothioate, phosphorodithioate, mesyl phosphoramidate, and dimethylamino phosphoramidate.
    </li>
    <li>
        Calculate melting temperatures of MGB-modified oligonucleotide probes, similar to Primer Express 3.0 software.
    </li>
    <li>
        Determine melting temperatures of DNA oligonucleotides with DNA targets.
    </li>
    <li>
        Compute extinction coefficients using nearest neighbors model.
    </li>
    <li>
        Obtain monoisotopic and average molecular weights and charge states.
    </li>
    <li>
        Generate molecular formulas for oligonucleotides.
    </li>
    <li>
        Predict theoretical masses of fragments in MS/MS experiments.
    </li>
    <li>
        Quantify oligonucleotides based on user input of measured absorbance at 260 nm and volume of the oligonucleotide solution.
    </li>
</ul>
<p>
    <strong>Sequence Input Guidelines:</strong>
</p>
<p>
    Sequences must be entered from 5' to 3'. You can choose whether your oligonucleotide is primarily <strong>DNA</strong>, <strong>RNA</strong>, or <strong>Therapeutic</strong>. For sequences containing phosphorothioate linkages, use an asterisk (*) as a separator.
</p>
<ul>
    <li>
        <strong>DNA / RNA Input</strong>
        <p>
            Use single-letter codes for standard nucleotides (A, C, G, T/U) and degenerate nucleotides (W, S, M, K, R, Y, B, D, H, V, N). These single-letter codes represent deoxy-nucleotides for <strong>DNA</strong> and ribo-nucleotides for <strong>RNA</strong>.
            For other nucleotides or modifications, use their designated multi-letter codes enclosed in square brackets, e.g., [+Cm], [FAM], or [GALNAC-PRO].
        </p>
    </li>
    <li>
        <strong>Therapeutic Input</strong>
        <p>
            Enter each nucleotide, degenerate nucleotide, or modification using its specific designation. Separate each entity (nucleotide, modification, or phosphate backbone) with a space.
        </p>
    </li>
    <li>
        To facilitate input, use dropdown menus with modifications of nucleotides from the 'keyboard'.
    </li>
</ul>

<p><strong>Examples:</strong></p>
<ul>
    <li><strong>DNA:</strong> ACGTACGTGGCAGGCA</li>
    <li><strong>DNA:</strong> [VIC]CCGGCGCGNTTSCGTC[MGB-ECLIPSE]</li>
    <li><strong>RNA:</strong> [po]ACGUGGCUSGACUGVUUGAUNG</li>
    <li><strong>RNA:</strong> GUGCGAAGGGACGGUGCGGAGAGGAGAGCAC[GALNAC3-ALN]</li>
    <li><strong>Therapeutic:</strong> +A +Cm +G dT dA dC dG dT dG dG dC dA dG +G +Cm +A</li>
    <li><strong>Therapeutic:</strong> +Cm * +G * +T * dA * dA * dC * dC * dT * dG * dA * dC * dC * dG * +A * +G * +A</li>
    <li><strong>Therapeutic (PMO): </strong>morC # morC # morT # morC # morC # morG # morG # morT # morT # morC # morT</li>
</ul>
<p><strong>Available Nucleotides:</strong></p>
<ul>
    <li>
        Deoxynucleotides: dA, dC, dG, dT, dU, dCm
    </li>
    <li>
        Degenerate deoxynucleotides: dW, dS, dM, dK, dR, dY, dB, dD, dH, dV, dN
    </li>
    <li>
        Ribonucleotides: rA, rC, rG, rU
    </li>
    <li>
        Degenerate ribonucleotides: rW, rS, rM, rK, rR, rY, rB, rD, rH, rV, rN
    </li>
    <li>
        2'-OMe nucleotides: mA, mC, mG, mU
    </li>
    <li>
        2'-F nucleotides: fA, fC, fG, fU
    </li>
    <li>
        2'-MOE nucleotides: moeA, moeCm, moeG, moeT
    </li>
    <li>
        LNA nucleotides: +A, +Cm, +G, +T
    </li>
    <li>
        Constrained ethyl (cEt) nucleotides: cetA, cetC, cetG, cetU
    </li>
    <li>
        Morpholino nucleosides: morA, morC, morG, morT
    </li>
    <sub>* <b>Cm</b> stands for 5-methylcytosine and <b>T</b> for 5-methyluracil</sub>
</ul>
<br/>

<h2>Available Tools:</h2>
<br/>

<h3>siRNA Scan & Score</h3>
<p>
    siRNA Scan & Score is a web-based tool for designing and evaluating siRNA candidates based on sequence input. 
    It identifies all possible 19- and 21-mer siRNAs from a given mRNA target and computes multiple scoring metrics 
    including predicted on-target efficacy and off-target potential using independently implemented or published algorithms.
    The tool provides ranked output, interactive filtering, and detailed scoring breakdowns to support researchers 
    in selecting potent and specific siRNA sequences for experimental use.
</p>
<br/>

<h3>TaqMan Finder</h3>
<p>
    This tool simplifies the process of finding matching primers and probes for TaqMan assays within your specified target sequence. By providing the exact (single isotope) masses of both primers and the probe, chemical modifications of the probe, length of the amplicon, and the reference sequence (RefSeq), you can easily identify compatible components of your assay.
</p>

<br/>
<p>
Experience full functionality of the <strong>OligoShell Calculator</strong> online at <a href="https://www.oligoshell.com">www.oligoshell.com</a>
</p>