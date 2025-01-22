const MAX_SEQ_LEN = 400; // Define the maximum allowed sequence length

const menuItems5 = document.querySelectorAll('#label5 > li .dropdown-item');
const menuItemsInt = document.querySelectorAll('#labelInt > li .dropdown-item');
const menuItems3 = document.querySelectorAll('#label3 > li .dropdown-item');

const nucleotide1Container = document.getElementById('nucleotide1Container');
const nucleotides = document.querySelectorAll('.calc-grid-container > div');
const degenerateContainer = document.getElementById('degenerateContainer');

let outputTextarea = document.getElementById('id_sequence');

const radioDNA = document.getElementById('id_btnradio_0');
const radioMIX = document.getElementById('id_btnradio_1');
const radioRNA = document.getElementById('id_btnradio_2');

function showDegenerate(){
    nucleotide1Container.classList.add('hide')
    degenerateContainer.classList.remove('hide')
    document.getElementById('nucleotidesBtn').classList.remove('active')
    document.getElementById('degenerateBtn').classList.add('active')
}

function showNucleotides(){
    degenerateContainer.classList.add('hide')
    nucleotide1Container.classList.remove('hide')
    document.getElementById('nucleotidesBtn').classList.add('active')
    document.getElementById('degenerateBtn').classList.remove('active')
}

menuItems5.forEach(function(item) {
    item.style.padding = '0.1rem 1.25rem';
    item.addEventListener('click', function() {
        let text;
        if (radioDNA.checked) {
            text = this.getAttribute('data-value-DNA');
        } else if (radioRNA.checked) {
            text = this.getAttribute('data-value-RNA');
        } else if (radioMIX.checked) {
            text = this.getAttribute('data-value-MIX');
            const firstChar = outputTextarea.value.charAt(0);
            if (outputTextarea.value.length !== 0 && firstChar !== ' ') {
                text = text + ' ';
            }
        }
        if (outputTextarea.value.length + text.length <= MAX_SEQ_LEN) {
            outputTextarea.value = text + outputTextarea.value;
        }
        outputTextarea.focus();
    });
});

menuItems3.forEach(function(item) {
    item.style.padding = '0.1rem 1.25rem';
    item.addEventListener('click', function() {
        let text;
        if (radioDNA.checked) {
            text = this.getAttribute('data-value-DNA');
        } else if (radioRNA.checked) {
            text = this.getAttribute('data-value-RNA');
        } else if (radioMIX.checked) {
            text = this.getAttribute('data-value-MIX');
            const lastChar = outputTextarea.value[outputTextarea.value.length - 1];
            if (outputTextarea.value.length !== 0 && lastChar !== ' ') {
                text = ' ' + text;
            }
        }
        if (outputTextarea.value.length + text.length <= MAX_SEQ_LEN) {
            outputTextarea.value = outputTextarea.value + text;
        }
        outputTextarea.focus();
    });
});

menuItemsInt.forEach(function(item) {
    item.style.padding = '0.1rem 1.25rem';
    item.addEventListener('click', function() {
        let text;
        if (radioDNA.checked) {
            text = this.getAttribute('data-value-DNA');
            insertAtCursor(outputTextarea, text, false);
        } else if (radioRNA.checked) {
            text = this.getAttribute('data-value-RNA');
            insertAtCursor(outputTextarea, text, false);
        } else if (radioMIX.checked) {
            text = this.getAttribute('data-value-MIX');
            insertAtCursor(outputTextarea, text, true);
        }
        outputTextarea.focus();
    });
});

nucleotides.forEach(function(item) {
    item.addEventListener('click', function() {
        let text;
        if (radioDNA.checked) {
            text = this.getAttribute('data-value-DNA');
            insertAtCursor(outputTextarea, text, false);
        } else if (radioRNA.checked) {
            text = this.getAttribute('data-value-RNA');
            insertAtCursor(outputTextarea, text, false);
        } else if (radioMIX.checked) {
            text = this.getAttribute('data-value-MIX');
            insertAtCursor(outputTextarea, text, true);
        }
        outputTextarea.focus();
    });
});

degenerateContainer.classList.add('hide');

function insertAtCursor(textarea, text, addSpaces) {
    let start = textarea.selectionStart;
    let end = textarea.selectionEnd;
    let before = textarea.value.substring(0, start);
    let after = textarea.value.substring(end, textarea.value.length);

    if (addSpaces) {
        if (text !== "" && start > 0 && before[start - 1] !== ' ') {
            text = ' ' + text;
        }
        if (text !== "" && end < textarea.value.length && after[0] !== ' ') {
            text = text + ' ';
        }
    }

    if (before.length + text.length + after.length <= MAX_SEQ_LEN) {
        textarea.value = before + text + after;
        textarea.selectionStart = textarea.selectionEnd = start + text.length;
    }
};