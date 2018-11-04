
difference = arr => {
	var arr2 = []
	for (let i = 0;i < arr.length; i++){
		arr2 = arr2.concat(arr[i])
	}

	result = {}
	for(let i = 0; i<arr2.length; i++){
		if (!(arr2[i] in result)){
			result[arr2[i]] = 1
		}else{
			result[arr2[i]]++
		}
	}

	result2 = []
	for(let i in result){
		if (result[i] ===1){
			result2.push(i)
		}
	}
	console.log(result2)
}

arr = [[1,2,3],[2,3,4,9],[2,4,5]]
difference(arr)