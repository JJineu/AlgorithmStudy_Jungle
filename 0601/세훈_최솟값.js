function solution(A,B){
    answer = 0;
    const arr = A.sort((a,b) => {return b-a})
    const brr = B.sort((a,b) => {return a-b})
    
    for(let i = 0; i < A.length; i++){
        answer += (arr[i] * brr[i])
    }
    // console.log(arr, brr)
    // console.log(answer)
    return answer;
}
