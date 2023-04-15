
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
// let timePassed = 0;'
let timePassed = 0;
let timeLeft = TIME_LIMIT;
let timerInterval = null;
let remainingPathColor = COLOR_CODES.info.color;
let ing_selected=Array();
let list = document.getElementById("selectedList");
const COUNTER_KEY = 'my-counter';


document.getElementById("app").innerHTML = `
<div class="base-timer">
  <svg class="base-timer__svg" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <g class="base-timer__circle">
      <circle class="base-timer__path-elapsed" cx="50" cy="50" r="45"></circle>
      <path
        id="base-timer-path-remaining"
        stroke-dasharray="283"
        class="base-timer__path-remaining ${remainingPathColor}"
        d="
          M 50, 50
          m -45, 0
          a 45,45 0 1,0 90,0
          a 45,45 0 1,0 -90,0
        "
      ></path>
    </g>
  </svg>
  <span id="base-timer-label" class="base-timer__label">${formatTime(
    timeLeft
  )}</span>
</div>
`;

startTimer();

function onTimesUp() {
  clearInterval(timerInterval);
}

function startTimer() {
  timerInterval = setInterval(() => {
    timePassed = timePassed += 1;
    timeLeft = TIME_LIMIT - timePassed;
    document.getElementById("base-timer-label").innerHTML = formatTime(
      timeLeft
    );
    setCircleDasharray();
    setRemainingPathColor(timeLeft);
    if ((timeLeft--) > 0) {
      window.sessionStorage.setItem(COUNTER_KEY, timeLeft);
    } else {
      window.sessionStorage.removeItem(COUNTER_KEY);}

    if (timeLeft === 0) {
      onTimesUp();
    }
  }, 1000);

}

function formatTime(time) {
  const minutes = Math.floor(time / 60);
  let seconds = time % 60;

  if (seconds < 10) {
    seconds = `0${seconds}`;
  }

  return `${minutes}:${seconds}`;
}

function setRemainingPathColor(timeLeft) {
  const { alert, warning, info } = COLOR_CODES;
  if (timeLeft <= alert.threshold) {
    document
      .getElementById("base-timer-path-remaining")
      .classList.remove(warning.color);
    document
      .getElementById("base-timer-path-remaining")
      .classList.add(alert.color);
  } else if (timeLeft <= warning.threshold) {
    document
      .getElementById("base-timer-path-remaining")
      .classList.remove(info.color);
    document
      .getElementById("base-timer-path-remaining")
      .classList.add(warning.color);
  }
}

function calculateTimeFraction() {
  const rawTimeFraction = timeLeft / TIME_LIMIT;
  return rawTimeFraction - (1 / TIME_LIMIT) * (1 - rawTimeFraction);
}

function setCircleDasharray() {
  const circleDasharray = `${(
    calculateTimeFraction() * FULL_DASH_ARRAY
  ).toFixed(0)} 283`;
  document
    .getElementById("base-timer-path-remaining")
    .setAttribute("stroke-dasharray", circleDasharray);
}

function arrayRemove(arr, value) {   
  for( var i = 0; i < ing_selected.length; i++){ 
    if ( arr[i] === value) {  
        arr.splice(i, 1); 
    }
  }
  return arr
}

function onoff(btn){
  classname = document.getElementById(btn).className;
  currentvalue = document.getElementById(btn).value;
  document.getElementById("base-timer-label").innerHTML = formatTime(
    timeLeft
  );
  if (timeLeft === 0) {
    document.getElementsByTagName(ingButton).disabled = true;
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

function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

function setRandomColor() {
  $("#colorpad").css("background-color", getRandomColor());
}

function sendUserinfo(){
  let list = ing_selected
  // console.log(list)
  const request = new XMLHttpRequest()
  document.getElementById("test").innerHTML = list;
  request.open('POST', `/ProcessUserinfo/${JSON.stringify(list)}`)
  console.log("inside sendUserinfo")
  request.send()
}