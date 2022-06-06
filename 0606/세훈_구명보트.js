function solution(people, limit) {
    let answer = 0 ;
    let i = 0;
    let j = people.length -1
    people.sort((a,b)=>{return b-a})
    
    while(i<=j){       
        
        if(limit - people[i] >= people[j]){
            j --
            i ++  
        }
        else{
            i ++
        }
        
        answer +=1
    }    
    return answer;
}
