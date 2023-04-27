
let cook_selected=Array();

function arrayRemove(arr, value) {
  for( var i = 0; i < cook_selected.length; i++){
    if ( arr[i] === value) {
        arr.splice(i, 1);
    }
  }
  return arr
}

function cook_onoff(btn, money){
    classname = document.getElementById(btn).className;
    currentvalue = document.getElementById(btn).value;
    // const {timeout} = require('./home.js');
    // if(timeout == true){
    //   alert("TIME IS UP");
    //   window.location.href = "success";
    //   document.getElementsByTagName(ingButton).disabled = true;
    // }
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
        cook_selected.push(currentvalue);      //adding elements to array
        
    }else{
        document.getElementById(btn).classList.toggle("answerBtnsOn");
        document.getElementById(btn).className = "answerBtnsOff";
        arrayRemove(cook_selected,currentvalue); //removing elements to array
      }
      // console.log(cook_selected)
      document.getElementById("demoList").innerHTML = cook_selected;
}
  
function sendToolinfo(){
    let list = cook_selected
    // console.log(list)
    const request = new XMLHttpRequest()
    document.getElementById("test").innerHTML = cook_selected;
    request.open('POST', `/ProcessToolinfo/${JSON.stringify(list)}`)
    console.log("inside sendToolinfo")
    request.send()
}

