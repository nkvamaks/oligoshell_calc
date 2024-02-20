let formula = document.querySelector('.formula');
const formulaPattern = /(\d+|\.)/g;

formula.innerHTML = formula.innerHTML.replace(formulaPattern, '<sub>$1</sub>')