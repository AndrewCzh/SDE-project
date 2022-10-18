const btn = document.getElementById('btn');

let index = 0;

const colos = ['red', 'white'];

btn.addEventListener('click', function onClick() {
  btn.style.backgroundColor = colos[index];
  btn.style.color = 'white';

  index = index % 2 == 0 ? 1 : 0;
});