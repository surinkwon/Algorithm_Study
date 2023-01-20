function solution(d, budget) {
  let totalDepartment = 0
  
  d.sort((a, b) => a - b)
  
  for (let i = 0; i < d.length; i += 1) {
      if (d[i] <= budget) {
          budget -= d[i]
          totalDepartment += 1
      } else {
          break
      }
  }
  
  return totalDepartment;
}

/*
이전 풀이

function solution(d, budget) {
    
    d.sort((a, b) => {
        return a - b
    })
    
    let maxDepartment = 0
    
    for (i = 0; i < d.length; i += 1) {
        if (budget - d[i] < 0) {
            break
        } else {
            maxDepartment += 1
            budget -= d[i]
        }
    }
    
    return maxDepartment;
}
*/
