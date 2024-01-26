## 알고리즘 냠냠 🍕

### 완전 탐색

|                   문제 번호                    |     문제 이름      |  난이도  |
| :--------------------------------------------: | :----------------: | :------: |
|  [2309](https://www.acmicpc.net/problem/2309)  |    일곱 난쟁이     | 브론즈 1 |
|  [2231](https://www.acmicpc.net/problem/2231)  |       분해합       | 브론즈 2 |
|  [3085](https://www.acmicpc.net/problem/3085)  |     사탕 게임      |  실버 2  |
| [10448](https://www.acmicpc.net/problem/10448) |    유레카 이론     | 브론즈 1 |
|  [2503](https://www.acmicpc.net/problem/2503)  |     숫자 야구      |  실버 3  |
|  [1018](https://www.acmicpc.net/problem/1018)  | 체스판 다시 칠하기 |  실버 4  |
|  [1182](https://www.acmicpc.net/problem/1182)  |   부분 수열의 합   |  실버 2  |

### 탐욕적 기법

**언제 사용할까**

문제의 성질이 동일하게 보존되고, 같은 전략을 반복적으로 취할 수 있는 경우

**특징**

눈 앞의 가장 최선의 이익를 선택하는 것 </br>
-> 이러한 특징 때문에 local maximum과 global maximum을 구분하지 못하고, 최적해를 구하기가 어렵다.

**주의점**

그리디는 후퇴하지 않는다. 잘못된 선택을 했다고 해서 수를 무르지 않는다.

</br>

|                   문제 번호                    |            문제 이름            |  난이도  |
| :--------------------------------------------: | :-----------------------------: | :------: |
|  [4796](https://www.acmicpc.net/problem/4796)  |              캠핑               | 브론즈 1 |
|  [1449](https://www.acmicpc.net/problem/1449)  |           수리공 항승           |  실버 3  |
| [17509](https://www.acmicpc.net/problem/17509) | And the Winner Is... Ourselves! |  실버 5  |
| [11047](https://www.acmicpc.net/problem/11047) |             동전 0              |  실버 4  |
|  [1931](https://www.acmicpc.net/problem/1931)  |         ⭐ 회의실 배정          |  실버 1  |
| [11000](https://www.acmicpc.net/problem/11000) |         ⭐ 강의실 배정          |  골드 5  |
|  [1700](https://www.acmicpc.net/problem/1700)  |       ⭐ 멀티탭 스케줄링        |  골드 1  |
|  [2212](https://www.acmicpc.net/problem/2212)  |              센서               |  골드 5  |
| [13904](https://www.acmicpc.net/problem/13904) |             ⭐ 과제             |  골드 3  |
| [15478](https://www.acmicpc.net/problem/15478) |           Rest Stops            |  골드 5  |
|  [1493](https://www.acmicpc.net/problem/1493)  |           박스 채우기           |  미해결  |

</br>

### 분할 정복

**언제 사용할까**

문제가 작아질수록 해결이 쉬워지는 경우 </br>
-> 분할 정복은 재귀 호출과 조합이 좋다.

**특징**

말 그대로 분할과 정복으로 나누어 문제를 해결한다. </br>
분할 정복은 그냥 풀었을 때보다 이미 풀린 문제들을 합치는 것이 월등히 빠른 경우에 좋다. </br>
예) 병합 정렬, 이분 탐색, 거듭제곱 연산

|                  문제 번호                   |    문제 이름     | 난이도 |
| :------------------------------------------: | :--------------: | :----: |
| [1629](https://www.acmicpc.net/problem/1629) |     ⭐ 곱셈      | 실버 1 |
| [2630](https://www.acmicpc.net/problem/2630) | ⭐ 색종이 만들기 | 실버 2 |
| [1992](https://www.acmicpc.net/problem/1992) |    쿼드 트리     | 실버1  |
| [1780](https://www.acmicpc.net/problem/1780) |   종이의 개수    | 미해결 |
| [2104](https://www.acmicpc.net/problem/2104) | 부분배열 고르기  | 미해결 |
| [1725](https://www.acmicpc.net/problem/1725) |    히스토그램    | 미해결 |
| [1074](https://www.acmicpc.net/problem/1074) |        Z         | 미해결 |
| [2447](https://www.acmicpc.net/problem/2447) |    별 찍기 10    | 미해결 |
| [2339](https://www.acmicpc.net/problem/2339) |   석판 자르기    | 미해결 |
