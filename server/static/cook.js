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
        cook_selected.push(currentvalue);      //adding elements to array
        
    }else{
        document.getElementById(btn).classList.toggle("answerBtnsOn");
        document.getElementById(btn).className = "answerBtnsOff";
        arrayRemove(cook_selected,currentvalue); //removing elements to array
      }
      // console.log(ing_selected)
      document.getElementById("demoList").innerHTML = cook_selected;
  }
  
  
  function sendUserinfo(){
    let list = cook_selected
    // console.log(list)
    const request = new XMLHttpRequest()
    document.getElementById("test").innerHTML = list;
    request.open('POST', `/ProcessToolinfo/${JSON.stringify(list)}`)
    console.log("inside sendUserinfo")
    request.send()
  }
