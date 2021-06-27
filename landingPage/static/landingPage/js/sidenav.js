'use strict';

let menu = document.querySelector('#menu');
let sidebar = document.querySelector('#Navbar')


menu.addEventListener('click', function (event) {
    event.preventDefault();
    sidebar.classList.toggle('active')
    
})

window.addEventListener('resize', function () {
    console.log('escuchando');
    let windowScreen = this.screen.width;
    let windowWidth = this.window.innerWidth
    console.log(windowScreen, windowWidth);
    if (windowScreen < 1200 || windowWidth < 1200) {
        if (!sidebar.classList.contains('active')) {
            return
        }
        console.log('has class');
        sidebar.classList.remove('active')
    } else if (windowScreen > 1200 || windowWidth > 1200) {
        if (sidebar.classList.contains('active')) {
            return
        }
        sidebar.classList.add('active')
        
    }
    
    
})

