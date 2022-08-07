# [Silver I] Z - 1074 

[문제 링크](https://www.acmicpc.net/problem/1074) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

분할 정복(divide_and_conquer), 재귀(recursion)

### 문제 설명

<p>한수는 크기가 2<sup>N</sup> × 2<sup>N</sup>인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.</p>

<p style="text-align:center"><img alt="" src="https://upload.acmicpc.net/21c73b56-5a91-43aa-b71f-9b74925c0adc/-/preview/" style="width: 100px; height: 99px;"></p>

<p>N > 1인 경우, 배열을 크기가 2<sup>N-1</sup> × 2<sup>N-1</sup>로 4등분 한 후에 재귀적으로 순서대로 방문한다.</p>

<p>다음 예는 2<sup>2</sup> × 2<sup>2</sup> 크기의 배열을 방문한 순서이다.</p>

<p style="text-align:center"><img alt="" src="https://upload.acmicpc.net/adc7cfae-e84d-4d5c-af8e-ee011f8fff8f/-/preview/" style="width: 250px; height: 252px;"></p>

<p>N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.</p>

<p>다음은 N=3일 때의 예이다.</p>

<p style="text-align:center"><img alt="" src="https://upload.acmicpc.net/d3e84bb7-9424-4764-ad3a-811e7fcbd53f/-/preview/" style="width: 533px; height: 535px;"></p>

### 입력 

 <p>첫째 줄에 정수 N, r, c가 주어진다.</p>

### 출력 

 <p>r행 c열을 몇 번째로 방문했는지 출력한다.</p>


### 풀이방식
기본 방식대로 모든지역을 검색하는것은 너무 느리기때문에 시간이 초과한다.
따라서 행렬을 4사분면으로 나누어 조건에 따라 1/4씩 줄여가고, 마지막에 z 방향으로 위치를 찾도록한다.

이를 위해 1,2,3,4 분면으로 행렬을 나누면 row/2와 col/2일때 총 4가지 경우의수에 의해 사분면 위치가 정해진다.
따라서 해당 사분면만큼만 검색하는것으로 바꾸기위해 해당 사분면의 시작지점과 사분면 이동으로 인해 row와 col값을 재조정한다.
반복적으로 위 작업을 수행하다가 마지막 2*2사이즈일때 z방향으로 검색하여 몇번째인지 확인한다.


### 풀이 아이디어
시간복잡도를 줄이기위해 어떻게 시간을 줄일까하다가 2*2를 z로 돌듯이 커다란 N*N 또한 z로 돈다는 사실을 생각했다.
그렇다면 일일히 검색하지 않고 검색해야하는 위치를 1/4,1/4,1/4 씩 줄여나간다면 빠른 검색이 가능할것이라고 생각했다.
