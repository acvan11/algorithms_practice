// Check if 2 arrays are the same or not
checkDuplicate1 = (arr1,arr2) => {
  if ((arr2.indexOf(arr1[0]) != -1) &&  (arr2.indexOf(arr1[1]) != -1) && (arr2.indexOf(arr1[2]) != -1)){
    return true
  }
  return false
}

checkDuplicate2 = (Bigarr, arr) => {
  result = false
  Bigarr.forEach( e => {
    if(checkDuplicate1(e,arr)){
      result = true
    }
  })
  return result
}

Bigarr = [
  [6,5,8],
  [5,6,1]
]
arr1 = [5,1,6]
arr2 = [6,2,5]

console.log(checkDuplicate2(Bigarr,arr1))
console.log(checkDuplicate2(Bigarr,arr2))