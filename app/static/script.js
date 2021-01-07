

'use strict';

//var someVarName = localStorage.getItem("someVarKey");

const thumbs_up_input=document.querySelectorAll('.thumbs_up_input');
const thumbs_down_input=document.querySelectorAll('.thumbs_down_input');

for(let k=0; k<thumbs_up_input.length; k++){

   
    var inpu=document.getElementById(thumbs_up_input[k].id);

    inpu.value=localStorage[thumbs_up_input[k].id] || 0;

}

for(let i=0; i<thumbs_down_input.length; i++){

   
    var downinput=document.getElementById(thumbs_down_input[i].id);

    downinput.value=localStorage[thumbs_down_input[i].id] || 0;

}

function clickCounter(id) {
    var node = document.getElementById(id);
    if (!node) {
        return console.error('Element #' + id + ' not found');
    }

    if (window.localStorage === undefined) {
        node.innerHTML = 'Sorry, your browser does not support web storage...';
    } else {
        var key = id;
        localStorage[key] = (++node.value || 0);
        node.value= localStorage[key] ;
        
    }
}

function clickCounters(id) {
    var node = document.getElementById(id);
    if (!node) {
        return console.error('Element #' + id + ' not found');
    }

    if (window.localStorage === undefined) {
        node.innerHTML = 'Sorry, your browser does not support web storage...';
    } else {
        var key = id;
        localStorage[key] = (++node.value || 0);
        node.value= localStorage[key] ;
        
    }
}