
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
let list = document.getElementById("selectedList");
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

// function startTimer1() {
//   if(timePassed == null) {
//     // Set the time we're counting down to using the time allowed
//       // timePassed = new Date().getTime() + (time + 2) * 1000;
//       timePassed = 0
//       window.localStorage.setItem('timePassed', timePassed);
//     } 
//     else{timePassed=window.localStorage.getItem('timePassed')}
//     timerInterval = setInterval(() => {
//     timePassed = timePassed += 1;
//     console.log("HEREEEEEEEEE",timePassed)

//     timeLeft = TIME_LIMIT - timePassed;
//     document.getElementById("base-timer-label").innerHTML = formatTime(
//       timeLeft
//     );
//     setCircleDasharray();
//     setRemainingPathColor(timeLeft);
//     if ((timeLeft--) > 0) {
//       window.sessionStorage.setItem(COUNTER_KEY, timeLeft);
//     } else {
//       window.sessionStorage.removeItem(COUNTER_KEY);}
//     if (timeLeft === 0) {
//       onTimesUp();
//     }
//   }, 1000);

// }

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

// function formatTime(time) {
//   const minutes = Math.floor(time / 60);
//   let seconds = time % 60;

//   if (seconds < 10) {
//     seconds = `0${seconds}`;
//   }

//   return `${minutes}:${seconds}`;
// }

// function setRemainingPathColor(timeLeft) {
//   const { alert, warning, info } = COLOR_CODES;
//   if (timeLeft <= alert.threshold) {
//     document
//       .getElementById("base-timer-path-remaining")
//       .classList.remove(warning.color);
//     document
//       .getElementById("base-timer-path-remaining")
//       .classList.add(alert.color);
//   } else if (timeLeft <= warning.threshold) {
//     document
//       .getElementById("base-timer-path-remaining")
//       .classList.remove(info.color);
//     document
//       .getElementById("base-timer-path-remaining")
//       .classList.add(warning.color);
//   }
// }

// function calculateTimeFraction() {
//   const rawTimeFraction = timeLeft / TIME_LIMIT;
//   return rawTimeFraction - (1 / TIME_LIMIT) * (1 - rawTimeFraction);
// }

// function setCircleDasharray() {
//   const circleDasharray = `${(
//     calculateTimeFraction() * FULL_DASH_ARRAY
//   ).toFixed(0)} 283`;
//   document
//     .getElementById("base-timer-path-remaining")
//     .setAttribute("stroke-dasharray", circleDasharray);
// }

function arrayRemove(arr, value) {   
  for( var i = 0; i < ing_selected.length; i++){ 
    if ( arr[i] === value) {  
        arr.splice(i, 1); 
    }
  }
  return arr
}

function sendstatus(){
  var myBoolean = true;

  var xhr = new XMLHttpRequest();
  xhr.open("POST", "login.py", true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send(JSON.stringify({"myBoolean": myBoolean}));
}

function onoff(btn){
  classname = document.getElementById(btn).className;
  currentvalue = document.getElementById(btn).value;
  // document.getElementById("demo").innerHTML = formatTime(
  //   timeLeft
  // );
  counter = document.getElementById("timerclock").innerHTML
  if (counter == "TIMEOUT") {
    alert("TIME IS UP");
    window.location.href = "success";
    document.getElementsByTagName(ingButton).disabled = true;
    timeout=true;  
    module.exports = {timeout};
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



