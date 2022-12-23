function solution(survey, choices) {
  var answer = '';
  
  // 성격 유형 점수
  const personality = {
      'R': 0, 'T': 0,
      'C': 0, 'F': 0,
      'J': 0, 'M': 0,
      'A': 0, 'N': 0
  }
  
  // 성격 유형 비교 군
  const compare = ['RT', 'CF', 'JM', 'AN']
  
  // 점수 계산
  for (let i = 0; i < survey.length; i += 1) {
      if (choices[i] < 4) {
          personality[survey[i][0]] += 4 - choices[i]
      } else if (choices[i] > 4) {
          personality[survey[i][1]] += choices[i] - 4
      }
  }
  
  // 성격 유형 도출
  for (let i = 0; i < compare.length; i += 1) {
      if (personality[compare[i][0]] >= personality[compare[i][1]]) {
          answer += compare[i][0]
      } else {
          answer += compare[i][1]
      }
  }
  
  return answer;
}