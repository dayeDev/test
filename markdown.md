## 날짜: 2/10(월) | 변수와 자료형

[강의]
자바스크립트의 기본 문법 
1. 변수란? 
2. 자료형과 연산자 보너스 트랙- 호이스팅

[과제]
- 변수와 자료형 문제

---
## 문제1
 아래에 step 들을 참고하여 변수 a와 b의 값을 바꾸시오

```javascript=
let a = 30
let b = 50
console.log(a,b) // 30,50 

let Temp = a
a = b 
b = Temp
console.log(a,b) //  50,30 
```

## 문제2
다음 연산자들의 결과값을 예측한후 console.log()를 통해 확인해 보시오
```javascript=
 console.log(20 + 30)  // 50
 console.log(“20” + “30”)  // 2030
 console.log(“Hello” + " " + 2021)  // Hello 2021
 console.log(1 + 2 * 3)  // 7
 console.log((1 + 3) ** 2)  // 16
 console.log(1 / 0)  // Infinity
 console.log(6 % 2)  // 0
 console.log(7.5 % 2)  // 1.5
 console.log(5 == 5)  // true
 console.log(5 === 5)  // true
 console.log(5 == “5”)  // true
 console.log(5 === “5”)  // false
 console.log(5 != 5.0)  // false
 console.log(5 !== 5.0)  // false
 console.log(“true” === true)  // false
 console.log(5 <= 5.0)  // true
 console.log(5 >= 5)  // true
 console.log(true || true)  // true
 console.log(true || false)  // true
 console.log(true && true)  // true
 console.log(true && false)  // false
 console.log(!true)  // false
 console.log(!false)  // true
```

### 오답노트
>5. `**`연산자는 거듭제곱 `(1+3)**2`는 4의 제곱 => `16`
>6. `1/0`자바스크립트에서 나누기 연산자가 0이면 => `Infinity`반환

### 배운 점
`==`와 `===`의 차이:
>`==`는 값만 비교, `===`는 값과 타입 모두 비교





