// The following 2 funtions change the body 
// background-color based on the image that is 
// being hovered over

function backgroundChange(id){

    body = document.getElementById('body');

    if (id == "grid-1"){
        body.classList.add('color-1');
    }
    else if (id == "grid-2") {
        body.classList.add('color-2');
    }
    else if (id == "grid-3") {
        body.classList.add('color-3');
    }
}

function backgroundRemove(id){

    gridItem = document.getElementById(id);
    body = document.getElementById('body');

    if (id == "grid-1"){
        body.classList.remove('color-1');
    }
    else if (id == "grid-2") {
        body.classList.remove('color-2');
    }
    else if (id == "grid-3") {
        body.classList.remove('color-3');
    }
}

// The overlay() function displays a button to 'add to cart' 
// over the images in the New Products section grid. The
// normal() function removes it

function overlay(id) {
    switch (id) {
        case 'np1':
            button = document.getElementById('npb1')
            break;
        case 'np2':
            button = document.getElementById('npb2')
            break;
        case 'np3':
            button = document.getElementById('npb3')
            break;
        case 'np4':
            button = document.getElementById('npb4')
            break;
        case 'np5':
            button = document.getElementById('npb5')
            break;
        case 'np6':
            button = document.getElementById('npb6')
            break;
        default:
            break;
    }

    button.style.display = 'block'
}

function normal(id) {

    switch (id) {
        case 'np1':
            button = document.getElementById('npb1')
            break;
        case 'np2':
            button = document.getElementById('npb2')
            break;
        case 'np3':
            button = document.getElementById('npb3')
            break;
        case 'np4':
            button = document.getElementById('npb4')
            break;
        case 'np5':
            button = document.getElementById('npb5')
            break;
        case 'np6':
            button = document.getElementById('npb6')
            break;
        default:
            break;
    }

    button.style.display = 'none'
}