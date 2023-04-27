
const FULL_DASH_ARRAY = 283;
const WARNING_THRESHOLD = 30;
const ALERT_THRESHOLD = 15;

const COLOR_CODES = {
  info: {
    color: "green"
  },
  warning: {
    color: "orange",
    threshold: WARNING_THRESHOLD
  },
  alert: {
    color: "red",
    threshold: ALERT_THRESHOLD
  }
};

const TIME_LIMIT = 30;
var timePassed = window.localStorage.getItem('timePassed');
// let timePassed = 0
let timeLeft = TIME_LIMIT;
let timerInterval = null;
let remainingPathColor = COLOR_CODES.info.color;
let ing_selected=Array();
const COUNTER_KEY = 'my-counter';

// document.getElementById("timerclock").innerHTML = `
// <div class="base-timer">
//   <svg class="base-timer__svg" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
//     <g class="base-timer__circle">
//       <circle class="base-timer__path-elapsed" cx="50" cy="50" r="45"></circle>
//       <path
//         id="base-timer-path-remaining"
//         stroke-dasharray="283"
//         class="base-timer__path-remaining ${remainingPathColor}"
//         d="
//           M 50, 50
//           m -45, 0
//           a 45,45 0 1,0 90,0
//           a 45,45 0 1,0 -90,0
//         "
//       ></path>
//     </g>
//   </svg>
//   <span id="base-timer-label" class="base-timer__label">${formatTime(
//     timeLeft
//   )}</span>
// </div>
// `;

startTimer();

function onTimesUp() {
  clearInterval(timerInterval);
}



function startTimer() {
  var time = 30; // This is the time allowed
  var saved_countdown = localStorage.getItem('saved_countdown');

  if(saved_countdown == null) {
      // Set the time we're counting down to using the time allowed
      var new_countdown = new Date().getTime() + (time + 2) * 1000;

      time = new_countdown;
      localStorage.setItem('saved_countdown', new_countdown);
  } else {
      time = saved_countdown;
  }

  var x = setInterval(() => {

  // Get today's date and time
  var now = new Date().getTime();

  // Find the distance between now and the allowed time
  var distance = time - now;

  // Time counter
  var counter = Math.floor((distance % (1000 * 60)) / 1000);

  // Output the result in an element with id="demo"
  document.getElementById("timerclock").innerHTML = "0:" + counter ;
      
  // If the count down is over, write some text 
  if (counter <= 0) {
      clearInterval(x);
      localStorage.removeItem('saved_countdown');
      document.getElementById("timerclock").innerHTML = "TIMEOUT";
  }
  }, 1000);
}



function arrayRemove(arr, value) {   
  for( var i = 0; i < ing_selected.length; i++){ 
    if ( arr[i] === value) {  
        arr.splice(i, 1); 
    }
  }
  return arr
}


function onoff(btn, money){
  classname = document.getElementById(btn).className;
  currentvalue = document.getElementById(btn).value;
  // document.getElementById("demo").innerHTML = formatTime(
  //   timeLeft
  // );
  counter = document.getElementById("timerclock").innerHTML
  if (counter == "TIMEOUT") {
    alert("TIME IS UP");
    if (money >= 20){
      window.location.href = "success";
    }
    else{
      window.location.href = "failed";
    }
    document.getElementsByTagName(ingButton).disabled = true;
    timeout=true;  
    // module.exports = {timeout};
    }

  //pickColor();
  if(classname == "answerBtnsOff"){
      document.getElementById(btn).classList.toggle("answerBtnsOff");
      document.getElementById(btn).className = "answerBtnsOn";
      // document.getElementById("demo").innerHTML = currentvalue;
      ing_selected.push(currentvalue);      //adding elements to array
      
  }else{
      document.getElementById(btn).classList.toggle("answerBtnsOn");
      document.getElementById(btn).className = "answerBtnsOff";
      arrayRemove(ing_selected,currentvalue); //removing elements to array
    }
    // console.log(ing_selected)
    document.getElementById("demoList").innerHTML = ing_selected;
}


function sendUserinfo(){
  let list = ing_selected
  const request = new XMLHttpRequest()
  document.getElementById("demoList").innerHTML = list;
  request.open('POST', `/ProcessUserinfo/${JSON.stringify(list)}`)
  console.log("inside sendUserinfo")
  request.send()
  }



