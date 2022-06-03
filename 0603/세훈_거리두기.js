function solution(places) {
    var answer = [];
     for(let i = 0; i < 5; i++){        
        let result = 1
        for(let j =0 ; j <5 ; j++){ 
            
            let isP = false;
            let count = 0;
            let isX = false;
            
            const arr = [...places[i][j]];
            if(!arr.includes('P')){
                continue
            }  
            else{
                for(let k = 0; k < arr.length; k++){
                    if(isP){
                        if(arr[k] === 'P'){
                            if(isX === true || count >= 2){
                                isX = false
                                count = 0
                            }
                            else{
                                result = 0
                                return
                            }
                            
                        }
                        else if (arr[k] === 'X'){
                            isX = true
                        }
                        else {
                            count += 1
                        }
                    }
                    else{
                        if(arr[k] === 'P'){
                            isP = true
                        }
                        else {
                            continue
                        }
                    }
                }
            }
        }
        answer.push(result)
        
         
     }
    return answer;
}
