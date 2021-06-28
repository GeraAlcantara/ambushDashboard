'use strict';

const menu = document.querySelector('#menu');
const sidebar = document.querySelector('#Navbar')

const NavtoggleClass = function () {
sidebar.classList.toggle('active')
    
}

menu.addEventListener('click', NavtoggleClass)

window.addEventListener('resize', function () {
    const windowScreen = this.screen.width;
    const windowWidth = this.window.innerWidth
    if (windowScreen < 1200 || windowWidth < 1200) {
        if (!sidebar.classList.contains('active')) {
            return
        }
        sidebar.classList.remove('active')
    } else if (windowScreen > 1200 || windowWidth > 1200) {
        if (sidebar.classList.contains('active')) {
            return
        }
        sidebar.classList.add('active')    
    }
    
})

