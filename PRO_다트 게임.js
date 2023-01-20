function solution(dartResult) {
  var answer = 0;
  let round = 1
  let scores = [...new Array(4)].map(e => 0)
  let num = ''
  const rule = {'S': 1, 'D': 2, 'T': 3}

  for (let i = 0; i < dartResult.length; i += 1) {
    
    // 숫자 판별
    if (!isNaN(dartResult[i])) {
          num += dartResult[i]
      } else {
          if (dartResult[i] !== '*' && dartResult[i] !== '#') {
              scores[round] += Number(num) ** (rule[dartResult[i]])
          } else if (dartResult[i] === '*') {
              scores[round] *= 2
              scores[round - 1] *= 2
          } else {
              scores[round] *= -1
          }
          
          if (i === dartResult.length - 1 || !isNaN(dartResult[i + 1])) {
              round += 1
              num = ''
          }
      }
  }
  
  answer = scores.reduce((a, c) => a + c, 0)
  
  return answer;
}


/**
 이전 풀이

 function solution(dartResult) {
    var answer = 0;
    let score = ''
    let scores = []
    
    for (i = 0; i < dartResult.length; i += 1) {
        if (!isNaN(dartResult[i])) {
            if (typeof score === 'number') {
                scores.push(score)
                score = ''
            } 
            score += dartResult[i]
        } else if (dartResult[i] === 'S') {
            score = parseInt(score)
        } else if (dartResult[i] === 'D') {
            score = parseInt(score) ** 2
        } else if (dartResult[i] === 'T') {
            score = parseInt(score) ** 3
        } else if (dartResult[i] === '#') {
            score = -score
        } else if (dartResult[i] === '*') {
            score *= 2
            
            if (scores.length > 0) {
                let preScore = scores.pop()
                scores.push(preScore * 2)
            }
        }
    }
    
    scores.push(score)
    
    for (i = 0; i < scores.length; i += 1) {
        answer += scores[i]
    }
    return answer;
}
 */