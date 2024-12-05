document.addEventListener('DOMContentLoaded', function() {
    const actionsColumnHeaderCell = document.querySelector('th.check-actions');

    if (!actionsColumnHeaderCell) {
        return;
    }

    /**
     * Manipluate the Actions text to a a link ro run all checks in this column
     * by running the click event on the buttons
     */
    const actionsLink = document.createElement('a');
    actionsLink.href = '#';
    actionsLink.id = 'run-all-checks';
    actionsLink.textContent = '(Run All)';

    actionsLink.addEventListener('click', function(event) {
        event.preventDefault();
        const checkButtons = document.querySelectorAll('button[data-check-action]');
        checkButtons.forEach(button => {
            button.click();
        });
    });

    actionsColumnHeaderCell.appendChild(actionsLink);
});
