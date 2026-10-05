(() => {
  const button = document.getElementById('copy-citation');
  const code = document.getElementById('bibtex');
  const status = document.getElementById('copy-status');
  if (!button || !code || !status) return;
  button.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(code.textContent);
      status.textContent = 'BibTeX copied.';
    } catch {
      const selection = window.getSelection();
      const range = document.createRange();
      range.selectNodeContents(code);
      selection.removeAllRanges();
      selection.addRange(range);
      status.textContent = 'Use your browser’s Copy command, or download the BibTeX file.';
    }
  });
})();
