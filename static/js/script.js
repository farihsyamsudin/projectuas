AOS.init({
    duration: 1000,
    offset: 30,
    once: true
});

// Sidebar Handler
const sideBar = document.getElementById('sidebar-menu')
const ham = document.getElementById('hamButton')
const containerlp = document.getElementById('containerlp')
const navlp = document.getElementById('navlp')

const toggleSidebar = () =>{
    sideBar.classList.toggle('translate-x-[110%]')
    sideBar.classList.toggle('shadow-sidebar')
    containerlp.classList.toggle('blur-md')
    navlp.classList.toggle('blur-md')
    
}

// Login Handler
const input = document.getElementsByTagName('input')
const inputuname = input.namedItem('username')
const inputpass = input.namedItem('password')
const inputemail = input.namedItem('email')
const inputfname = input.namedItem('first_name')
const inputlname = input.namedItem('last_name')
const onchangehandle = () => {              
    if (inputuname.value != '') {
        document.getElementById('username').classList.add('hidden')
    } else{
        document.getElementById('username').classList.remove('hidden')
    }

    if (inputpass.value != '') {
        document.getElementById('password').classList.add('hidden')
    } else{
        document.getElementById('password').classList.remove('hidden')
    }

    if (inputemail.value != '') {
        document.getElementById('email').classList.add('hidden')
    } else{
        document.getElementById('email').classList.remove('hidden')
    }

    if (inputfname.value != '') {
        document.getElementById('fname').classList.add('hidden')
    } else{
        document.getElementById('fname').classList.remove('hidden')
    }

    if (inputlname.value != '') {
        document.getElementById('lname').classList.add('hidden')
    } else{
        document.getElementById('lname').classList.remove('hidden')
    }
}