function solution(s) {
    var answer = '';
    let temp = '';
    const numbers = ['0','1','2','3','4','5','6','7','8','9']
    const dict = {'zero' : 0, 'one':1, 'two':2, 'three' : 3, 'four' :4, 'five': 5, 'six': 6, 'seven':7, 'eight' : 8 , 'nine' : 9}
    
    for(let i=0; i < s.length; i++){  
        if(numbers.includes(s[i])){ 
            answer += s[i]
        }
        else{
            temp += s[i]
        }
        
        if(Object.keys(dict).includes(temp)){
                answer += dict[temp]
                temp =''    
        }
    }
    console.log(answer)
    return answer*1;
}
