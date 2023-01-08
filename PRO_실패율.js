function solution(N, stages) {
  var answer = [];
  let failPercentages = []
  let stageNum = [...new Array(N+2)].map(e => 0)

  // 스테이지별 머무른 사람 수 체크
  for (let i = 0; i < stages.length; i += 1) {
      stageNum[stages[i]] += 1
  }
  
  // 실패율 계산
  for (let i = 1; i < N + 1; i += 1) {
      const failPercentage = stageNum[i] / stageNum.reduce((acc, cur, idx) => {
          if (idx >= i) {
              return acc + cur
          } else {
              return acc + 0
          }
      }, 0)
      
      failPercentages.push([i, failPercentage])
  }

  // 실패율 높은 순, 같으면 낮은 스테이지 순 정렬
  failPercentages.sort((a, b) => {
      if (a[1] == b[1]) {
          return a[0] - b[0]
      } else {
          return b[1] - a[1]
      }
  })
  
  answer = failPercentages.map(el => el[0])
  
  return answer;
}