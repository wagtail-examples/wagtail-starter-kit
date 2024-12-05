function checkResponses(button) {
    const row = button.closest("tr");
    const cells = row.querySelectorAll("td");

    const adminButton = cells[1].querySelector("a");
    const frontendButton = cells[2].querySelector("a");
    const listingButton = cells[3].querySelector("a");

    let adminUrl;
    let frontUrl;
    let listingUrl;

    if(!adminButton && !frontendButton && !listingButton) {
        return;
    }

    if (adminButton) {
        adminButton.classList.remove("button-primary");
        adminButton.classList.remove("serious");
        adminButton.classList.add("button-secondary");
        adminUrl = adminButton.href;
    }

    if (frontendButton) {
        frontendButton.classList.remove("button-primary");
        frontendButton.classList.remove("serious");
        frontendButton.classList.add("button-secondary");
        frontUrl = frontendButton.href;
    }

    if (listingButton) {
        listingButton.classList.remove("button-primary");
        listingButton.classList.remove("serious");
        listingButton.classList.add("button-secondary");
        listingUrl = listingButton.href;
    }

    const checks = [
        {
            url: adminUrl,
            button: adminButton,
        },
        {
            url: frontUrl,
            button: frontendButton,
        },
        {
            url: listingUrl,
            button: listingButton,
        }
    ]

    checks.forEach(check => {
        if (check.url) {
            fetch(check.url)
                .then(response => {
                    if (response.ok) {
                        check.button.classList.add("button-primary");
                        check.button.classList.remove("button-secondary");
                    } else {
                        check.button.classList.add("serious");
                        check.button.classList.remove("button-secondary");
                    }
                })
                .catch(error => {
                    check.button.classList.add("serious");
                    check.button.classList.remove("button-secondary");
                });
        }
    });
}
