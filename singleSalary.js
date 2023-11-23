function findSingleSalary(salaries){
    let singleSalary=0
    for( let i=0;i<salaries.length;i++){
        for(let j=i+1; j<salaries.length;j++){
            if(salaries[i] == salaries[j]){
                break
            }
            else{
                singleSalary=salaries[i]
            }
        }
    }
    return singleSalary

}

let salaries = [25000,25000,19000,50,50]

console.log(findSingleSalary(salaries))