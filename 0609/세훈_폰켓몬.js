const getCombinations = (array, selectNumber) => {
    const results = [];
    if(selectNumber === 1){
        return array.map((element) => [element]);
    }
    array.forEach((fixed, index, origin) => {
        const rest = origin.slice(index+1);
        const combinations = getCombinations(rest, selectNumber - 1);
        const attached = combinations.map((combination) => [fixed, ...combination]);
        results.push(...attached);
    });
    return results;
}

function solution(nums) {
    var answer = 0;
    const getcha = nums.length/2    
    const set = new Set(nums)  
    const n = [...set].length;// 중복 제거 갯수
    
    // 1. 조합 구하기 = 배열
    const comb = getCombinations(nums, getcha);
    let count = 0
    // 2.  filter
    if(n>=getcha){  
        for(let i =0; i < comb.length; i++){
            let s = [...new Set(comb[i])];
            console.log(s, s.length, getcha) /////////////////////////////////////
            if(s.length === getcha){
                count ++
            }
        }
    }
    else{
        for(let i =0; i < comb.length; i++){
            let s1 = [...new Set(comb[i])];
            console.log(s, s.length, getcha) /////////////////////////////////////
            if(s1.length === n){
                count++
            }
        }
    }
    console.log(count)
    return answer;
}
solution([3,1,2,3])
