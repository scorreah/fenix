/* Show account menu */
let account = document.querySelector('#account-icon');
let desktopmenu = document.querySelector('.desktop-menu');

account.onclick = () => {
    console.log('hola');
    desktopmenu.classList.toggle('open');
};

window.onscroll = () => {
    desktopmenu.classList.remove('open');
};