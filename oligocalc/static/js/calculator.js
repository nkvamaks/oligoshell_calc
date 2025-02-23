function copyToClipboard(btn) {
  const text = btn.getAttribute('data-copy');
  navigator.clipboard.writeText(text)
    .then(() => {
      const originalHTML = btn.innerHTML;
      btn.innerHTML = '&emsp;<i class="bx bx-check-double"></i>';
      const originalTitle = btn.getAttribute('title');
      btn.setAttribute('title', 'Copied!');
      setTimeout(() => {
        btn.innerHTML = originalHTML;
        btn.setAttribute('title', originalTitle);
      }, 2000);
    })
    .catch(err => {
      console.error('Failed to copy text: ', err);
    });
}

function copyAllProperties(event) {
  event.preventDefault();
  const rows = document.querySelectorAll('#properties-table tr');
  let allText = '';

  rows.forEach(row => {
    const labelCell = row.querySelector('td:first-child');
    const valueCell = row.querySelector('td:nth-child(2)');
    if (labelCell && valueCell) {
      const copyTarget = valueCell.querySelector('.copy-target');
      const valueText = copyTarget
                        ? copyTarget.innerText.trim()
                        : valueCell.innerText.trim();
      allText += `${labelCell.innerText.trim()} ${valueText}\n`;
    }
  });

  navigator.clipboard.writeText(allText)
    .then(() => {
      const copyAllBtn = document.getElementById('copy-all-btn');
      const originalHTML = copyAllBtn.innerHTML;
      copyAllBtn.innerHTML = '<i class="bx bx-check-double"></i> Copied All!';
      setTimeout(() => {
        copyAllBtn.innerHTML = originalHTML;
      }, 2000);
    })
    .catch(err => {
      console.error('Failed to copy all text: ', err);
    });
}

document.getElementById('copy-all-btn').addEventListener('click', copyAllProperties);
