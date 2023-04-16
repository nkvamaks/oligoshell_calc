# OligoShell Calculator
<p>
It is a separate part of OligoShell web application aimed to calculate properties of natural, modified and therapeutic oligonucleotides without saving results in database.
</p>
<p>
Now it calculates:
</p>
<ul>
    <li>
        Extinction coefficient (nearest neighbours model)
    </li>
    <li>
        Monoisotopic and average molecular weight, and charge states
    </li>
    <li>
        Theoretical masses of fragments in MS/MS experiments
    </li>
</ul>
<p>
It also can quantify oligonucleotide based on user input of measured <strong>absorbanse at 260 nm</strong>, <strong>volume</strong> and <strong>dilution factor</strong> of oligonucleotide solution.
</p>
<p><strong>How to input a sequence:</strong></p>
<p>
Sequences are 5'-->3' left to right. Every nucleotide has a specific designation and should be separated by 'space' from the next nucleotide or phosphate entity. Case-sensitive.
</p>
<p><strong>Alphabet available now:</strong></p>
<ul>
    <li>
        Deoxynucleotides: dA, dC, dG, dT, dU, dCm
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
<p>
On default it is assumed that two nucleotides separated with space have phosphodiester linkage. Use ' * ' as a separator to designate phosphorothioate linkage.
</p>
<p>
Examples:
</p>
<p>
+A * +Cm * +T * +G * dT * mG * dG * dG * dC * dC * dT * dT * dA * dA * +A * +Cm * +T * +G  
</p>
<p>
mU * fA * mG fA mU fC mU fU mU fU mG fG mC fC mU fA mU * dC * dT
</p>
<p>
<b>OligoShell Calculator</b> is available online at <a href="http://www.oligoshell.com">www.oligoshell.com</a>
</p>