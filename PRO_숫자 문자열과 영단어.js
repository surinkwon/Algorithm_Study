function solution(s) {
  let answer = ''
  const stringNums = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
                     'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
                     'nine': '9', 'zero': '0', '1': '1', '2': '2', '3': '3', 
                      '4': '4', '5': '5', '6': '6',
                     '7': '7', '8': '8', '9': '9', '0': '0'}
  
  let num = ''
  
  for (let i = 0; i < s.length; i += 1) {
      num += s[i]
      
      if (stringNums[num]) {
          answer += stringNums[num]
          num = ''
      }
  }
  
  return Number(answer);
}