let numbers = []
let target=7
numbers.indexOf
function firstAndLast(numbers,target){
    let positions= [-1,-1]
    if(numbers.indexOf(target)!=-1){
        positions[0]= numbers.indexOf(target)
            if(numbers[numbers.indexOf(target)+1]== target){
                //this if statement is used to find if the secound value after the first occurance of the target are the same, that is equals to the target
                positions[1]=numbers.indexOf(target)+1
            }
    }
    return positions

}

console.log(firstAndLast(numbers,target))