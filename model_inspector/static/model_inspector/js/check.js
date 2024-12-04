document.addEventListener('DOMContentLoaded', function() {
    console.log('check.js loaded');
    rows = document.querySelectorAll('div#listing-results tbody tr');
    rows.forEach(function(row) {
        const cells = row.querySelectorAll('td');

        let admin_edit_url = null;
        let front_end_url = null;
        let listing_url = null;

        /**
         * If a cell has an abchor link, get the href attribute value
         */
        if (cells[1].querySelector('a')) {
            admin_edit_url = cells[1].querySelector('a').href
        }
        if (cells[2].querySelector('a')) {
            front_end_url = cells[2].querySelector('a').href;
        }

        if (cells[3].querySelector('a')) {
            listing_url = cells[3].querySelector('a').href;
        }

        const check = document.createElement('button');
        check.innerHTML = 'Check';
        check.setAttribute('class', 'button button-small button-secondary');

        check.addEventListener('click', function() {
            if (admin_edit_url) {
                fetch(admin_edit_url)
                    .then(response => {
                        if (response.ok) {
                            check.setAttribute('class', 'button button-small button-primary');
                            check.innerHTML = 'Success';
                        } else {
                            check.setAttribute('class', 'button button-small no');
                            check.innerHTML = 'Failed';
                        }
                    })
                    .catch(error => {
                        check.setAttribute('class', 'button button-small no');
                        check.innerHTML = 'Error';
                    });
            }

            if (front_end_url) {
                fetch(front_end_url)
                    .then(response => {
                        if (response.ok) {
                            check.setAttribute('class', 'button button-small button-primary');
                            check.innerHTML = 'Success';
                        } else {
                            check.setAttribute('class', 'button button-small no');
                            check.innerHTML = 'Failed';
                        }
                    })
                    .catch(error => {
                        check.setAttribute('class', 'button button-small no');
                        check.innerHTML = 'Error';
                    });
            }

            if (listing_url) {
                fetch(listing_url)
                    .then(response => {
                        if (response.ok) {
                            check.setAttribute('class', 'button button-small button-primary');
                            check.innerHTML = 'Success';
                        } else {
                            check.setAttribute('class', 'button button-small no');
                            check.innerHTML = 'Failed';
                        }
                    })
                    .catch(error => {
                        check.setAttribute('class', 'button button-small no');
                        check.innerHTML = 'Error';
                    });
            }
        });

        cells[0].insertAdjacentElement('afterbegin', check);
    });
});
