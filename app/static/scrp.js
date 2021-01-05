

'use strict';


const delete_button=document.querySelector('.delete_button');
const warning_box=document.querySelector('.to_be_displayed');
const c_button=document.querySelector('.c_button');

for(let k=0; k<delete_button.length; k++){


    delete_button[k].addEventListener('click', function(){
    warning_box.classList.remove('appear');
});

}

   