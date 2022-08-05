# [D2] 두 개의 숫자열 - 1959 

[문제 링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpoFaAS4DFAUq) 

### 성능 요약

메모리: 58,256 KB, 시간: 148 ms, 코드길이: 895 Bytes

### 풀이방식
만약 문자열의 길이가 다르다면, 큰 문자열에 작은 문자열을 처음부터 끝까지 하나씩 대응하여 계산해야된다.
따라서 N,M을 비교하여 N이 큰경우, M이 큰경우에 대한 대응 곱셈을 한다.
범위의 경우 큰개수-작은개수-1로 range를 해야 알맞고, 이중 for문을 통하여 큰 문자열에서 대응을 시작하는 위치를 갱신하는 for문과 짧은 리스트의 idx값인 for문 구조로 계산한다. 만약 이 합이 max보다 크다면 계속 max를 갱신한다. 
만약 두 길이가 같다면, 처음부터 끝까지 대응하여 곱셈하고 이것이 최대값이 된다.

### 풀이간 문제점
처음 범위설정에 대해서 좀 오류가 있었음. range가 -1이 된다는 사실을 기억하자.



> 출처: SW Expert Academy, https://swexpertacademy.com/main/code/problem/problemList.do
