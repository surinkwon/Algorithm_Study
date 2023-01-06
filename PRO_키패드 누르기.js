function solution(numbers, hand) {
  var answer = '';
  let left = '*'
  let right = '#'
  
  // 키패드 좌표
  const key = {
      1: [0, 0], 2: [0, 1], 3: [0, 2], 
      4: [1, 0], 5: [1, 1], 6: [1, 2],
      7: [2, 0], 8: [2, 1], 9: [2, 2],
      '*': [3, 0], 0: [3, 1], '#': [3, 2]
  }
  
  for (let i = 0; i < numbers.length; i += 1) {
      const number = numbers[i]
      
      if (number % 3 === 1) {
          answer += 'L'
          left = number
      } else if (number !== 0 && number % 3 === 0) {
          answer += 'R'
          right = number
      } else {
        // 각각의 거리값
          const leftD = Math.abs(key[left][0]-key[number][0]) + Math.abs(key[left][1]-key[number][1])
          const rightD = Math.abs(key[right][0]-key[number][0]) + Math.abs(key[right][1]-key[number][1])
          
          // 거리값 비교 후 어떤 손으로 누를지 결정
          if (leftD > rightD) {
              answer += 'R'
              right = number
          } else if (leftD < rightD) {
              answer += 'L'
              left = number
          } else {
              if (hand === 'right') {
                  answer += 'R'
                  right = number
              } else {
                  answer += 'L'
                  left = number
              }
          }
      }
  }
  
  return answer;
}