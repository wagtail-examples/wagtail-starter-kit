/**
 * Add a button to the actions column header to run all checks in the column
 */
document.addEventListener("DOMContentLoaded", function () {
  const actionsColumnHeaderCell = document.querySelector("th.check-actions");

  if (!actionsColumnHeaderCell) {
    return;
  }

  /**
   * Manipluate the Actions text to a a link ro run all checks in this column
   * by running the click event on the buttons
   */
  const actionsLink = document.createElement("a");
  actionsLink.href = "#";
  actionsLink.id = "run-all-checks";
  actionsLink.textContent = "(Run All)";

  actionsLink.addEventListener("click", function (event) {
    event.preventDefault();
    const checkButtons = document.querySelectorAll("button[data-check-action]");
    checkButtons.forEach((button) => {
      button.click();
    });
  });

  actionsColumnHeaderCell.appendChild(actionsLink);
});

/**
 * Copy the code from the button to the clipboard
 */
function copyToClipboard(button) {
  const originalCodeSpan = button.querySelector("span.code");
  originalCodeSpan.style.display = "none";

  const copyMessage = document.createElement("span");
  copyMessage.innerText = "Copied!";

  button.appendChild(copyMessage);
  button.setAttribute("disabled", true);

  navigator.clipboard.writeText(originalCodeSpan.innerText).then(() => {
    console.log("copied");
    setTimeout(() => {
      copyMessage.remove();
      originalCodeSpan.style.display = "inline";
      button.removeAttribute("disabled");
    }, 500);
  });
}

/**
 * Check the responses of the view buttons in the row
 */
function checkResponses(button) {
  const row = button.closest("tr");
  row.classList.remove("serious");
  const cells = row.querySelectorAll("td");

  const adminButton = cells[1].querySelector("a");
  const frontendButton = cells[2].querySelector("a");
  const listingButton = cells[3].querySelector("a");

  let adminUrl;
  let frontUrl;
  let listingUrl;

  if (!adminButton && !frontendButton && !listingButton) {
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
    },
  ];

  checks.forEach((check) => {
    if (check.url) {
      fetch(check.url)
        .then((response) => {
          if (response.ok) {
            check.button.classList.add("button-primary");
            check.button.classList.remove("button-secondary");
          } else {
            check.button.classList.add("serious");
            check.button.classList.remove("button-secondary");
            check.button.closest("tr").classList.add("serious");
          }
        })
        .catch((error) => {
          check.button.classList.add("serious");
          check.button.classList.remove("button-secondary");
        });
    }
  });
}
