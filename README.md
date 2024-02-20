<h4 class="mb-4"> About OligoShell Calculator: </h4>
<p>
This web application is aimed to calculate properties of natural, modified and therapeutic oligonucleotides.
</p>
<p>
<strong>It can calculate:</strong>
</p>
<ul>
    <li>
        <sup><strong>NEW!</strong></sup>
        Melting temperature of DNA oligonucleotide with DNA target
    </li>
    <li>
        Extinction coefficient (nearest neighbours model)
    </li>
    <li>
        Monoisotopic and average molecular weight and charge states
    </li>
    <li>
        Molecular formula of oligonucleotide
    </li>
    <li>
        Theoretical masses of fragments in MS/MS experiments
    </li>
</ul>
<p>
It can also quantify oligonucleotide based on user input of measured <strong>absorbanse at 260 nm</strong> and <strong>volume</strong> of oligonucleotide solution.
</p>
<p>
<strong>How to input a sequence:</strong>
</p>
<p>
    Sequences are 5'&rarr;3' left to right. You may choose one of two input styles: 'DNA' and 'Therapeutic.
    On default it is assumed that two nucleotides have phosphodiester linkage. Use ' * ' as a separator to designate phosphorothioate linkage.
</p>
<ul>
    <li>
        <strong>DNA input style</strong>
        <p>
            Four deoxynucleotides (A, C, G, T) as well as eleven degenerate deoxynucleotides (W, S, M, K, R, Y, B, D, H, V, N) can be used with a single letter code. All other nucleotides with different sugar moieties as well as modifications have several letter codes and should be surrounded by square brackets, e.g. [FAM] or [BHQ1].
        </p>
        <p>Examples:</p>
        <p>ACGTACGTGGCAGGCA</p>
        <p>[VIC]CCGGCGCGNTTSCGTC[MGB-ECLIPSE]</p>
        <p>[+Cm]*[+G]*[+T]*A*A*C*C*T*G*A*C*C*G*[+A]*[+G]*[+A]</p>
    </li>
    <li>
        <strong>Therapeutic input style</strong>
        <p>
            Every nucleotide, degenerate nucleotide or modification has a specific designation and should be separated with 'space' from the next nucleotide or phosphate entity.
        </p>
        <p>Examples:</p>
        <p>dA dC dG dT dA dC dG dT dG dG dC dA dG dG dC dA</p>
        <p>VIC dC dC dG dG dC dG dC dG dN dT dT dS dC dG dT dC MGB-ECLIPSE</p>
        <p>+Cm * +G * +T * dA * dA * dC * dC * dT * dG * dA * dC * dC * dG * +A * +G * +A</p>
    </li>
</ul>
<p><strong>Available alphabet:</strong></p>
<ul>
    <li>
        Deoxynucleotides: dA, dC, dG, dT, dU, dCm
    </li>
    <li>
        Degenerate deoxinucleotides: dW, dS, dM, dK, dR, dY, dB, dD, dH, dV, dN
    </li>
    <li>
        Ribonucleotides: rA, rC, rG, rU
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
    <sub>* <b>Cm</b> stands for 5-methylcytosine and <b>T</b> for 5-methyluracil</sub>
</ul>
<p><strong>Available modifications:</strong></p>
<ul>
    <li>
        5': ALKYNE, FAM, TET, HEX, JOE, VIC, TMR-ACH, R6G, R6G-ACH, ROX-CLK, TR-CLK, AF594-CLK, 
        CY3-ACH, CY5-CLK, CHOL-PRO, GALNAC-PRO
    </li>
    <li>
        3': BHQ1, BHQ2, MGB, MGB-ECLIPSE, ECLIPSE, CHOL-PRO, GALNAC-PRO, GALNAC3-ALN
    </li>
    <li>
        Internal: BHQ1, BHQ2, ECLIPSE, GALNAC-PRO
    </li>
</ul>

<p>
<b>OligoShell Calculator</b> is available online at <a href="http://www.oligoshell.com">www.oligoshell.com</a>
</p>