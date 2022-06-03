function solution(s) {
    var answer = [];
    // 1. '{{', '}}'를 없애고, ',' 기준 split
    const first = s.replace('{{','').replace('}}','').split('},{');
    
    // 2. 각 문자열 원소를 배열 원소로 바꿔주어야 한다.
    const second = []
    for(let i=0; i < first.length; i++){
        second.push(first[i].split(','))
    }
    
    // 3. 원소 배열의 길이를 기준으로 오름차순 정렬
    second.sort((a,b)=>{
        if(a.length > b.length){
            return 1
        }
        else{
            return -1
        }
    })
    
    // 4. 하나씩 올라가면서 answer 답 추가
    answer.push(parseInt(second[0][0]))
    
    for(let j = 1; j < second.length ; j++){
        for(let k = 0; k < answer.length; k++){
            second[j] = second[j].filter(item => parseInt(item) !== answer[k])
        }                
        answer.push(parseInt(second[j][0]))        
    }
    return answer;
}
