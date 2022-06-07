function sum(arr){
    return arr.reduce((a,b)=> a+b)
}
function recur(arr, answer, target, i){
    if(i > arr.length){
        return
    }
    
    if(sum(arr) === target){
        answer +=1 
        return
    }
    else {
        i += 1        
        recur(arr, answer, target, i)
    }
    
    arr[i] = -arr[i]
    
    if(sum(arr) === target){
        answer +=1 
        return
    }
    else {
        i += 1        
        recur(arr, answer, target, i)
    }
    
}

function solution(numbers, target) {
    var answer = 0;
    let i = 0    
    recur(numbers, answer, target, i)    
    return answer;
}
