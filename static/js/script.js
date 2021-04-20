/*jshint esversion: 6 */

let animation = document.querySelector('.animation');
let animationText = animation.textContent;
let animationTextSplit = animationText.split("");

animation.textContent = "";

for (let i = 0; i < animationTextSplit.length; i++) {
    animation.innerHTML += "<span>" + animationTextSplit[i] + "</span>";
}

let char = 0;
let timer = setInterval(onTick, 50);

function onTick() {
    let span = animation.querySelectorAll('span')[char];
    span.classList.add('red-animation');
    char++;
    if(char === animationTextSplit.length) {
        complete();
        return;
    }
}

function complete() {
    clearInterval(timer);
    timer = null;
}