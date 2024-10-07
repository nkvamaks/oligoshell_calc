let formula = document.querySelector('.formula');
const formulaPattern = /(\d+|\.)/g;

if (formula !== null) {
formula.innerHTML = formula.innerHTML.replace(formulaPattern, '<sub>$1</sub>')
}
