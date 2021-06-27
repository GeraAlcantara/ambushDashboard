'use strict';

let menu = document.querySelector('#menu');
let sidebar = document.querySelector('.sidebar')

console.log(menu, sidebar);

menu.addEventListener('click', function (e) {
    sidebar.classList.toggle('active')
    console.log(e);
})