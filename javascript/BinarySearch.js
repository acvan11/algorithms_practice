function binarySearch(sortedArray, targetValue){
  var min = 0; //Min index
  var max = sortedArray.length - 1; //Max index
  var guess; //Index I am guessing

  while(min <= max){
    //Set the guess index at the midpoint of the remaining indexes
    guess = Math.floor((min + max) / 2);

    if(sortedArray[guess] === targetValue){
      return guess; //Yay, I win
    }
    else if(sortedArray[guess] < targetValue){ 
      //sortedArray[guess] is less than target
      min = guess + 1
    }
    else { 
      //sortedArray[guess] is greater than target
      max = guess - 1;
    }
  }

  return -1;
}

var arr = [];
var target = 2;

for(var i = 1; i < 100000; i++){
  arr.push(i);
}

console.log(binarySearch(arr, target));
