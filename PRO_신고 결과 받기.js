function solution(id_list, report, k) {
  var answer = [];

  // 유저가 신고받은 횟수, 유저가 신고한 다른 유저
  const reportedNum = {}
  const whoReportWho = {}
  
  for (let i = 0; i < report.length; i += 1) {
      let reporter, reportee
      [reporter, reportee] = report[i].split(' ')
      let reported = false
      
      // 신고가 들어갔는지 판별
      if (whoReportWho[reporter] && !whoReportWho[reporter].includes(reportee)) {
          whoReportWho[reporter].push(reportee)
          reported = true
      } else if (!whoReportWho[reporter]) {
          whoReportWho[reporter] = [reportee]
          reported = true
      }
      
      // 신고 됐으면 횟수 카운트
      if (reported) {
        if (reportedNum[reportee]) {
            reportedNum[reportee] += 1
        } else {
            reportedNum[reportee] = 1
        }
      }
  }
  
  for (let i = 0; i < id_list.length; i += 1) {
      const curId = id_list[i]
      let result = 0
      
      // 신고한 유저가 정지되었는지 판별
      if (whoReportWho[curId]) {
        for (let j = 0; j < whoReportWho[curId].length; j += 1) {
            const reportedId = whoReportWho[curId][j]

            if (reportedNum[reportedId] >= k) {
                result += 1
            }
        }
      }
      
      answer.push(result)
  }
  
  return answer;
}