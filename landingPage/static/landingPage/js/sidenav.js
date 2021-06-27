'use strict';

let menu = document.querySelector('#menu');
let sidebar = document.querySelector('.sidebar')


menu.addEventListener('click', function (event) {
    event.preventDefault();
    sidebar.classList.toggle('active')
    console.log(e);
})