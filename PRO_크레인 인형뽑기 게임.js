function solution(board, moves) {
  var answer = 0;
  let stack = []
  
  for (let i = 0; i < moves.length; i += 1) {
      const lane = moves[i] - 1
      let r = board.length - 1
      
      // 맨 위에 있는 인형 찾기
      for (r; r > -1; r -= 1) {
          if (!board[r][lane]) {
              break
          }
      }
      
      // 인형 내려놓기
      if (r < board.length - 1) {
          if (stack[stack.length - 1] === board[r + 1][lane]) {
              answer += 2
              stack.pop()
          } else {
              stack.push(board[r + 1][lane])
          }
          board[r + 1][lane] = 0
      }
      
  }
  
  return answer;
}