function modify (binary, n) {
  while (binary.length < n) {
      binary = '0' + binary
  }
  
  return binary
}

function solution(n, arr1, arr2) {
  var answer = [];
  
  for (let i = 0; i < n; i += 1) {
      // 이진수 변환 후 조정
      const first = modify(arr1[i].toString(2), n)
      const second = modify(arr2[i].toString(2), n)
      
      // 비밀지도 그리기
      let line = ''
      
      for (let j = 0; j < n; j += 1) {
          if (first[j] === '1' || second[j] === '1') {
              line += '#'
          } else {
              line += ' '
          }
      }
      
      answer.push(line)
  }
  
  return answer;
}


/** 
 * 
 * 이전 풀이
 // 2진수 변환 함수
function binary(n, len) {
    let rlt = ''
    
    while (n > 0) {
        rlt = String(n % 2) + rlt
        n = parseInt(n / 2)
    }
    
    while (rlt.length < len) {
        rlt = '0' + rlt
    }
    
    return rlt
}

function solution(n, arr1, arr2) {
    var answer = [];
    
    
    for (i = 0; i < n; i += 1) {
        let tmp = ''
        
        // 2진수 변환
        const first = binary(arr1[i], n)
        const second = binary(arr2[i], n)
        
        // 두 지도 비교
        for (j = 0; j < n; j += 1) {
            if (first[j] === '1' || second[j] === '1') {
                tmp += '#'
            } else {
                tmp += ' '
            }
        }
        
        // 지도 복원
        answer.push(tmp)
    }
    
    return answer;
}
*/