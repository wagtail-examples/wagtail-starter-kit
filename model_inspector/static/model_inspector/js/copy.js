function copyToClipboard(button) {

    const originalCodeSpan = button.querySelector('span.code');
    originalCodeSpan.style.display = 'none';

    const copyMessage = document.createElement('span');
    copyMessage.innerText = 'Copied!';

    button.appendChild(copyMessage);
    button.setAttribute('disabled', true);

    navigator.clipboard.writeText(originalCodeSpan.innerText).then(() =>{
        console.log('copied');
        setTimeout(() => {
            copyMessage.remove();
            originalCodeSpan.style.display = 'inline';
            button.removeAttribute('disabled');
        }, 500);
    });
}
