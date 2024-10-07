const fetchButton = document.getElementById('fetchButton');
const errorDiv = document.getElementById('errorFetchSeq');
let fastaOutput = document.getElementById('output')

fetchButton.addEventListener("click", function(event) {
    fetchFastaSequences();
});

async function fetchFastaSequences() {
    event.preventDefault();
    errorDiv.textContent = ''; // Clear previous error message
    const accInput = document.getElementById('accInput').value.trim();
    if (!accInput) {
        errorDiv.textContent = 'Please enter accession number.';
        return;
    }

    const base = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/';
    const efetchUrl = `${base}efetch.fcgi?db=nuccore&id=${accInput}&rettype=fasta&retmode=text`;
    const response = await fetch(efetchUrl);
    if (!response.ok) {
        errorDiv.textContent = `Error fetching RefSeq ${accInput}. Please check RefSeq number and try again.`;
    return;
        }

    // Display the FASTA sequence
    const fasta = await response.text();
    fastaOutput.value = fasta;
}
