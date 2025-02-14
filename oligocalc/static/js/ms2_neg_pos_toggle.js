document.addEventListener('DOMContentLoaded', function() {
    const btnNeg = document.getElementById('btn-neg');
    const btnPos = document.getElementById('btn-pos');
    const negTab = document.getElementById('navs-top-neg');
    const posTab = document.getElementById('navs-top-pos');

    const fragSchemeNeg = document.querySelector('button[data-bs-target="#frag-scheme-neg"]');
    const fragSchemePos = document.querySelector('button[data-bs-target="#frag-scheme-pos"]');
    const chargeStateNeg1 = document.querySelector('button[data-bs-target="#charge-state-minus-1"]');
    const chargeStatePos1 = document.querySelector('button[data-bs-target="#charge-state-plus-1"]');
    const fragSchemeNegPane = document.getElementById('frag-scheme-neg');
    const fragSchemePosPane = document.getElementById('frag-scheme-pos');
    const chargeStateNeg1Pane = document.getElementById('charge-state-minus-1');
    const chargeStatePos1Pane = document.getElementById('charge-state-plus-1');

    if (chargeStateNeg1 && chargeStatePos1 && chargeStateNeg1Pane && chargeStatePos1Pane) {
        chargeStateNeg1.classList.add('active');
        chargeStatePos1.classList.add('active');
        chargeStateNeg1Pane.classList.add('show', 'active');
        chargeStatePos1Pane.classList.add('show', 'active');

    }else if (fragSchemeNeg && fragSchemePos && fragSchemeNegPane && fragSchemePosPane) {
        fragSchemeNeg.classList.add('active');
        fragSchemePos.classList.add('active');
        fragSchemeNegPane.classList.add('show', 'active');
        fragSchemePosPane.classList.add('show', 'active');
    }

    if (btnNeg && btnPos) {
    btnNeg.addEventListener('click', function() {
            negTab.style.display = 'none';
            posTab.style.display = 'block';
            });

    btnPos.addEventListener('click', function() {
            posTab.style.display = 'none';
            negTab.style.display = 'block';
            });
    }
});