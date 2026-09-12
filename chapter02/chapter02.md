# Chapter 02 제출 답안. VS Code에서 시작하는 데이터 분석 환경

> 최종 파일은 개인 GitHub 저장소의 `chapter02/chapter02.md`로 저장하는 것을 권장합니다.

## 0. 제출 정보

- 이름: 황지원
- GitHub ID: Jiwon0712
- 개인 저장소: `llm-data-analysis-study`
- 작성일: 2026.09
- 운영체제: Windows

### 최종 제출 URL

```text
https://github.com/Jiwon0712/llm-data-analysis-study/blob/main/chapter02/chapter02.md
```

---

## 1. Python과 Git 환경 확인

### 실행 내용

```text
python --version 또는 py --version
git --version
```

### 실행 결과

```text
여기에 실제 결과를 작성하세요.

Python 3.13.15
git version 2.55.0.windows.5
```

### Evidence

![Python과 Git 버전](images/step01_versions.png)

### 결과 관찰

버전과 실행 가능 여부를 사실 위주로 작성하세요.

Python 3.13.15 버전, git version 2.55.0.windows.5 결과가 나왔다. 
코드는 오류 없이 실행되었다. 

### 나의 해석과 판단

현재 환경이 수업 실습에 적합한지 판단하고 이유를 작성하세요.

Python 3.13.15와 Git 2.55.0은 모두 최신 안정 버전이고, 버전 정보 2개 모두 오류 없이 출력되었으므로 정상적으로 설치 및 경로 설정이 완료된 상태이다. 실습에 적합하다고 판단된다.

### 업무·분석적 의미

프로젝트 시작 전에 버전과 도구 상태를 확인하는 이유를 작성하세요.

버전 정보를 기록해두면, 차후 문제가 발생하였을 때 실행 환경 차이 때문인지, 명령어 문제인지 구분할 수 있다. 또한 팀원들 혹은 강의자료상의 환경과 버전이 다를 경우 대응할 수 있다. 

### 한계와 추가 확인 사항

아직 확인하지 못한 항목을 작성하세요.

- 가상환경(venv 등) 생성 및 활성화 여부
- 주요 라이브러리(pandas, numpy 등)의 설치 및 버전 호환성
- pip 버전 및 패키지 관리자 정상 작동 여부
- VS code와 python 인터프리 연동 여부
---

## 2. 저장소와 `.venv` 준비

### 수행 내용

- [x] 공식 Public 저장소 clone
- [x] 프로젝트 루트 확인
- [x] `.venv` 생성
- [x] `.venv` 활성화
- [x] `requirements.txt` 설치

### 핵심 실행 결과

```text
현재 프로젝트 경로: c:\Users\관리자\llm-data-analysis-study\notebooks
터미널 Python 실행 파일: C:\Users\관리자\llm-data-analysis-study\.venv\Scripts\python.exe
가상환경 활성화 여부: 활성화됨 — 터미널 프롬프트에 (.venv) 표시
패키지 설치 결과: pip install -r requirements.txt 실행 결과 에러 없이 정상 종료. 이미 설치됨.
```

### Evidence

![가상환경과 Python 경로](images/step02_venv.png)

### 결과 관찰

현재 `python`이 어떤 실행 파일을 가리키는지 작성하세요.

현재 python은 .venv\Scripts\python.exe 을 가리키고 있다. 


### 나의 해석과 판단

시스템 Python과 프로젝트 `.venv`를 분리하는 것이 왜 필요한지 자신의 말로 작성하세요.

프로젝트 전용으로 격리된 환경을 이용하는 것이 중요하다. 시스템 python을 사용하면 다른 프로젝트에서 설치한 버전과 충돌하거나, requirements.txt에 명시된 버전과 달라서 오류가 발생할 수 있다. 격리된 환경인 .venv를 이용하면 다른 프로젝트에 영향을 주지 않고 실습을 진행할 수 있어 오류의 원인을 코드에서만 찾아도 되어 좋다. 

### 업무·분석적 의미

다른 사람이 같은 프로젝트를 재실행할 때 가상환경이 주는 이점을 작성하세요.

requirements.txt에 명시된 패키지와 버전을 설치하면 내 pc와 동일한 조건으로 코드를 실행할 수 있어서 오류를 줄일 수 있다. 또 여러 프로젝트를 동시에 하는 경우, 각각 독립된 가상환경을 사용하면 패키지 버전 충돌이 일어나지 않아 각자 필요한 버전을 쓰면 된다. 새로운 팀원이 들어왔을 때 가상환경을 생성하고requirements.txt를 설치하는 것만으로 동일한 개발 환경을 빠르게 구출할 수 있다.  


### 한계와 추가 확인 사항

회사/기관 PC 정책, Python 버전 차이 등 현재 환경의 제약을 작성하세요.

현재 3.13.15로 최신 버전인데, 강의 자료나 일부 라이브러리가 이보다 낮은 버전(예: 3.10, 3.11) 기준으로 작성되었을 경우 문법 차이나 미지원 패키지 문제가 발생할 가능성이 있다.
---

## 3. VS Code 인터프리터와 Jupyter 커널 연결

### 확인 결과

```text
VS Code Python 인터프리터: .venv (3.13.15.final.0)
Notebook sys.executable: C:\Users\관리자\llm-data-analysis-study\.venv\Scripts\python.exe
Notebook Path.cwd(): C:\Users\관리자\llm-data-analysis-study\notebooks
```

### Evidence

![VS Code 인터프리터와 Notebook 커널](images/step03_kernel.png)

### 결과 관찰

터미널 Python과 Notebook Python이 같은 `.venv`인지 작성하세요.

### 나의 해석과 판단

둘이 다를 경우 어떤 문제가 발생할 수 있는지 작성하세요.

### 업무·분석적 의미

`ModuleNotFoundError` 같은 환경 오류를 줄이는 데 어떤 도움이 되는지 작성하세요.

### 한계와 추가 확인 사항

커널 이름만 보고 판단하면 안 되는 이유 등 추가 확인 사항을 작성하세요.

---

## 4. 샘플 데이터와 Notebook 실행 검증

### 확인 결과

```text
DATA_DIR 존재 여부:
customers.csv 존재 여부:
customers.shape:
주요 컬럼:
```

### Evidence

![customers 데이터 정상 로드](images/step04_customers.png)

### 결과 관찰

`customers.head()`, shape, 컬럼 결과에서 직접 확인한 사실을 작성하세요.

### 나의 해석과 판단

이 단계까지 성공했다면 어떤 구성 요소가 정상 연결되었다고 판단할 수 있는지 작성하세요.

### 업무·분석적 의미

분석 전에 최소 스모크 테스트를 하는 이유를 작성하세요.

### 한계와 추가 확인 사항

현재는 환경 연결만 확인했으며 데이터 품질은 아직 검증하지 않았다는 점을 작성하세요.

---

## 5. 오류 해결 기록

실습 중 오류가 있었다면 작성합니다. 오류가 없었다면 `해당 없음`이라고 적습니다.

### 오류 메시지

```text
민감정보를 제거한 실제 오류
```

### 원인 후보

1.
2.
3.

### 내가 확인한 순서

1.
2.
3.

### 해결 방법

```text
실제로 적용한 해결 방법
```

### Evidence

![오류 해결 결과](images/step05_troubleshooting.png)

### 나의 해석과 판단

왜 해당 원인이 가장 가능성이 높다고 판단했는지 작성하세요.

### 한계와 추가 확인 사항

보안 정책 변경, 무분별한 삭제처럼 시도하지 않은 조치와 이유를 작성하세요.

---

## 6. Secret 보호 확인

- [ ] `.env`는 Git 추적 대상이 아닙니다.
- [ ] 실제 API Key를 코드에 작성하지 않았습니다.
- [ ] 캡처 화면에 Token/비밀번호가 없습니다.
- [ ] `.venv`를 Git에 올리지 않습니다.

### Evidence

필요한 경우 `git status`, `.gitignore` 확인 화면을 첨부합니다.

![Secret 보호 확인](images/step06_security.png)

### 나의 해석과 판단

환경 파일과 비밀정보를 분리해야 하는 이유를 작성하세요.

---

## 7. Chapter 02 최종 회고

### 가장 중요했다고 생각한 환경 설정 1가지

```text
작성하세요.
```

### 그 이유

```text
작성하세요.
```

### 다음 Chapter에서 재사용할 환경 체크 3가지

1.
2.
3.

### 현재 환경의 한계 또는 주의점

```text
작성하세요.
```

---

## 최종 제출 체크

- [ ] 핵심 Evidence 4~7장을 첨부했습니다.
- [ ] 단순 캡처가 아니라 관찰과 판단을 작성했습니다.
- [ ] Secret/개인정보가 없습니다.
- [ ] GitHub에서 이미지가 정상 표시됩니다.
- [ ] 개인 저장소에 `chapter02/chapter02.md`를 업로드했습니다.
- [ ] 저장소 URL이 아니라 최종 파일 URL을 제출합니다.
