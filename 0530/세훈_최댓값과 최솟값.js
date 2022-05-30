function solution(s) {
    const arr = s.split(" ");
        
    let maxi = Number(arr[0]);
    let mini = Number(arr[0]);
    
    arr.map(item => {
        if(maxi < item){
            maxi = Number(item)
        }
        if(mini > item){
            mini = Number(item)
        }
        
    })
    
    var answer = `${mini} ${maxi}`;
    return answer;
}
