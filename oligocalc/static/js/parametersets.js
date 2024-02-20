const paramSet = document.querySelector('#id_param_set');
let dnaConc = document.querySelector('#id_dna_conc');
let mvConc = document.querySelector('#id_mv_conc');
let dvConc = document.querySelector('#id_dv_conc');
let dntpConc = document.querySelector('#id_dntp_conc');

paramSet.addEventListener('change', setParam);

function setParam() {
    if (paramSet.value == "Default") {
        dnaConc.value = 0.25;
        mvConc.value = 50;
        dvConc.value = 0;
        dntpConc.value = 0;
    };
    if (paramSet.value == "qPCR") {
        dnaConc.value = 0.2;
        mvConc.value = 50;
        dvConc.value = 3;
        dntpConc.value = 0.8;
    };
};
