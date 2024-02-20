document.querySelector("#close-menu").addEventListener('click', () => {
    document.querySelector("#menu-bar").style.display = 'none';
})

document.querySelector("#menu-title").addEventListener('click', () => {
    document.querySelector("#menu-bar").style.display = 'flex';
})