# ia-codyssey

GitHub와 Codyssey를 연동하기 위해 생성한 Repository입니다.

## 1. 프로젝트 개요

### 1.1 프로젝트 목적

본 프로젝트는 Linux CLI, Docker, Git/GitHub를 활용하여 개발환경을 구축하고 컨테이너 기반 웹서버를 실행·관리하는 실습입니다.

### 1.2 주요 실습 내용

1. 터미널을 이용한 디렉터리 및 파일 관리
2. Linux 파일 권한 확인 및 변경
3. Docker 설치 및 실행환경 점검
4. Docker 이미지와 컨테이너 생성 및 관리
5. Python Flask 웹서버 개발
6. Dockerfile을 이용한 커스텀 이미지 제작
7. 포트 매핑을 통한 웹서버 접속
8. Docker Attach와 Exec 명령어 실습
9. 바인드 마운트를 이용한 파일 변경 반영
10. Docker Volume을 이용한 데이터 영속성 검증
11. 오류 발생 원인 분석 및 문제 해결
12. Git/GitHub를 이용한 버전관리 및 협업

---

## 2. 실행환경

### 2.1 운영체제 및 터미널

| 항목 | 실행환경 |
|---|---|
| OS | Windows Pro |
| Windows Build | 26100 |
| Shell | Windows PowerShell 5.1 |
| Terminal | Windows Terminal |
| Docker Desktop | 4.97.0 |
| Docker Engine | 29.9.2 |
| Docker Compose | v5.6.1 |
| Git | 2.56.0.windows.4 |
| Docker Context | desktop-linux |
| Container OS/Arch | linux/amd64 |

Windows 빌드 26100은 Windows 11 24H2 계열에 해당하지만, 실습 명령 출력에는 Windows 10 Pro로 표시되어 있습니다. 정확한 제품명은 추가 확인이 필요합니다.

### 2.2 운영체제 정보 확인

```powershell
Get-ComputerInfo | Select-Object WindowsProductName, WindowsBuildLabEx, WindowsEditionId
```

실행 결과:

```text
WindowsProductName : Windows 10 Pro
WindowsEditionId   : Professional
WindowsBuildLabEx  : 26100.1.amd64fre.ge_release.240331-1435
```

### 2.3 PowerShell 버전 확인

```powershell
$PSVersionTable.PSVersion
```

실행 결과:

```text
Major  Minor  Build  Revision
-----  -----  -----  --------
5      1      26100  9711
```

### 2.4 Docker 버전 확인

```powershell
docker --version
```

실행 결과:

```text
Docker version 29.9.2, build a82e528
```

Docker 클라이언트와 서버 정보 확인:

```powershell
docker version
```

주요 실행 결과:

```text
Client:
 Version: 29.9.2
 API version: 1.56
 OS/Arch: windows/amd64
 Context: desktop-linux

Server:
 Docker Desktop 4.97.0
 Engine Version: 29.9.2
 OS/Arch: linux/amd64
```

### 2.5 Docker Compose 버전 확인

```powershell
docker compose version
```

실행 결과:

```text
Docker Compose version v5.6.1
```

### 2.6 Git 버전 확인

```powershell
git --version
```

실행 결과:

```text
git version 2.56.0.windows.4
```

### 2.7 Docker 정보 및 이미지 확인

Docker 실행환경 확인:

```powershell
docker info
```

이미지 목록 확인:

```powershell
docker images
```

초기 확인 이미지:

```text
IMAGE          ID             DISK USAGE
nginx:latest   600f7cd45e27  243MB
```

실행 중이거나 종료된 컨테이너 확인:

```powershell
docker ps -a
```

---

## 3. Linux 파일 권한 이해

### 3.1 파일 권한의 종류

Linux는 파일과 디렉터리에 읽기, 쓰기, 실행 권한을 부여합니다.

| 권한 | 의미 | 숫자 |
|---|---|---|
| r | Read: 읽기 | 4 |
| w | Write: 쓰기 | 2 |
| x | Execute: 실행 | 1 |
| - | 권한 없음 | 0 |

권한 숫자는 각 권한 값을 합산하여 계산합니다.

예를 들어 `rwx`는 다음과 같습니다.

```text
r = 4
w = 2
x = 1

4 + 2 + 1 = 7
```

### 3.2 사용자 구분

Linux 파일 권한은 세 종류의 사용자에게 각각 부여됩니다.

| 구분 | 설명 |
|---|---|
| Owner | 파일 소유자 |
| Group | 파일이 속한 그룹 사용자 |
| Others | 그 외 모든 사용자 |

### 3.3 755와 644의 해석

**755 권한**

```text
Owner  : rwx = 7
Group  : r-x = 5
Others : r-x = 5
```

표시 형태:

```text
-rwxr-xr-x
```

**644 권한**

```text
Owner  : rw- = 6
Group  : r-- = 4
Others : r-- = 4
```

표시 형태:

```text
-rw-r--r--
```

---

## 4. 프로젝트 디렉터리 생성

### 4.1 작업 디렉터리 생성

PowerShell에서 다음 명령어를 실행합니다.

```powershell
mkdir od-mission1
cd od-mission1

mkdir app
mkdir evidence
```

### 4.2 Flask 웹서버 파일 생성

```powershell
notepad app\app.py
```

### 4.3 프로젝트 디렉터리 구조

실습 당시 확인한 구조는 다음과 같습니다.

```text
od-mission1/
│
├── Dockerfile
├── requirements.txt
│
├── app/
│   ├── app.py
│   ├── Dockerfile.txt
│   └── requirements.txt
│
└── evidence/
```

`app/` 내부의 `Dockerfile.txt`와 `requirements.txt`는 실습 중 생성된 파일입니다. 실제 이미지 빌드에는 프로젝트 루트의 `Dockerfile`과 `requirements.txt`를 사용합니다.

디렉터리 구조 확인:

```powershell
tree /F
```

---

## 5. Python Flask 웹서버 작성

### 5.1 app.py

파일 위치:

```text
od-mission1/app/app.py
```

Python 코드:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Odyssey Docker Web Server Assignment</h1>
    <p>Hello! My Docker container is running.</p>
    <p>Port Mapping: 8080 -> 5000</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### 5.2 주요 코드 설명

| 코드 | 설명 |
|---|---|
| `from flask import Flask` | Flask 클래스 불러오기 |
| `Flask(__name__)` | Flask 애플리케이션 생성 |
| `@app.route("/")` | 루트 URL 요청 처리 |
| `def home()` | 웹페이지 내용 반환 |
| `host="0.0.0.0"` | 모든 네트워크 인터페이스에서 접속 허용 |
| `port=5000` | 컨테이너 내부 웹서버 포트 |

**참고:** HTML의 포트 매핑 문구는 최초 실습 기준입니다. 실제 호스트 포트를 8082나 8083으로 변경하면 화면의 안내 문구도 해당 포트에 맞게 수정해야 합니다.

---

## 6. Dockerfile 작성

### 6.1 requirements.txt

프로젝트 루트에 다음 파일을 생성합니다.

```text
Flask
```

### 6.2 Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

EXPOSE 5000

CMD ["python", "app.py"]
```

### 6.3 Dockerfile 명령어 설명

| 명령어 | 설명 |
|---|---|
| FROM | 기반 이미지 지정 |
| WORKDIR | 컨테이너 작업 디렉터리 설정 |
| COPY | 호스트 파일을 이미지 내부로 복사 |
| RUN | 이미지 빌드 중 명령 실행 |
| EXPOSE | 컨테이너에서 사용할 포트 문서화 |
| CMD | 컨테이너 시작 시 실행할 기본 명령 |

`--no-cache-dir`은 pip가 다운로드한 패키지의 캐시를 저장하지 않도록 하는 옵션입니다. Docker 이미지 크기를 줄이는 데 도움이 됩니다.

---

## 7. Docker 이미지 빌드 및 실행

### 7.1 Docker 이미지 생성

```powershell
docker build -t flask-assignment .
```

명령어 설명:

- `docker build`: Docker 이미지 빌드
- `-t`: 이미지 이름 및 태그 지정
- `flask-assignment`: 생성할 이미지 이름
- `.`: 현재 디렉터리를 빌드 컨텍스트로 지정

### 7.2 Docker 컨테이너 실행

최초 실습 명령:

```powershell
docker run -d -p 8080:5000 flask-assignment
```

포트 매핑 형식:

```text
호스트 포트 : 컨테이너 포트
```

예를 들어:

```text
8080:5000
```

이는 Windows 컴퓨터의 8080 포트로 들어오는 요청을 컨테이너 내부 5000 포트로 전달한다는 의미입니다.

### 7.3 포트 충돌 후 변경

8080 포트를 Nginx가 사용하고 있어 8082 포트로 변경했습니다.

```powershell
docker run -d --name flask-web -p 8082:5000 flask-assignment
```

웹브라우저 접속 주소:

```text
http://localhost:8082
```

---

## 8. Docker Attach 실습

### 8.1 Ubuntu 컨테이너 생성

```powershell
docker run --name test-exit ubuntu
```

Ubuntu 이미지의 기본 프로세스가 종료되면 컨테이너도 종료됩니다.

### 8.2 실행 상태를 유지하는 컨테이너 생성

```powershell
docker run -dit --name test-keep ubuntu bash
```

옵션 설명:

| 옵션 | 의미 |
|---|---|
| -d | 백그라운드 실행 |
| -i | 표준 입력 유지 |
| -t | 가상 터미널 할당 |
| --name | 컨테이너 이름 지정 |

### 8.3 Attach 명령 실행

```powershell
docker attach test-keep
```

컨테이너 내부에서:

```bash
pwd
ls
```

`docker attach`는 컨테이너의 기존 메인 프로세스에 터미널을 연결합니다.

**주의:** Attach 상태에서 `exit`를 실행하여 메인 Bash 프로세스가 종료되면 컨테이너도 종료될 수 있습니다.

컨테이너를 계속 실행한 상태로 분리하려면 기본 분리 키인 `Ctrl+P`, `Ctrl+Q`를 사용합니다.

---

## 9. Docker Exec 실습

### 9.1 종료된 컨테이너 재시작

```powershell
docker start test-keep
```

### 9.2 컨테이너 내부에 새로운 Bash 실행

```powershell
docker exec -it test-keep bash
```

컨테이너 내부 명령:

```bash
pwd
ls
exit
```

### 9.3 컨테이너 상태 확인

```powershell
docker ps
```

실행 결과 예시:

```text
NAMES       STATUS
test-keep   Up 2 minutes
```

`docker exec`로 실행한 Bash를 종료해도 컨테이너의 메인 프로세스가 계속 실행 중이면 컨테이너는 유지됩니다.

### 9.4 Attach와 Exec 비교

| 구분 | Attach | Exec |
|---|---|---|
| 연결 대상 | 기존 메인 프로세스 | 새로 실행하는 프로세스 |
| 주요 용도 | 메인 프로세스 입출력 연결 | 컨테이너 내부 명령 실행 |
| `exit` 영향 | 메인 프로세스 종료 가능 | Exec로 시작한 셸만 종료 |
| 활용 | 실행 프로세스 관찰 | 점검 및 유지보수 |

---

## 10. 커스텀 Docker 이미지 제작

### 10.1 실습 목표

기존 Dockerfile을 활용하여 Flask 웹서버가 포함된 커스텀 이미지를 제작합니다.

### 10.2 디렉터리 구조 확인

```powershell
tree /F
```

### 10.3 커스텀 이미지 빌드

```powershell
docker build -t flask-custom:v1 .
```

이미지 이름:

```text
flask-custom
```

태그:

```text
v1
```

### 10.4 생성된 이미지 확인

```powershell
docker images
```

실행 결과:

```text
IMAGE                     ID             DISK USAGE
flask-assignment:latest   fd734c6f548e   198MB
flask-custom:v1           a8e1b37e2eb5   198MB
flask-web:latest          ea0696aaa1a9   198MB
mysql:latest              3819b2b23835  1.08GB
nginx:latest              165ddde8751e  243MB
python:latest             8c9a3bf2d6de  1.65GB
ubuntu:latest             6a06111c3b0a  163MB
```

### 10.5 커스텀 이미지로 컨테이너 실행

```powershell
docker run -d --name flask-custom-web -p 8083:5000 flask-custom:v1
```

접속 주소:

```text
http://localhost:8083
```

---

## 11. Docker 파일 권한 확인 및 변경

### 11.1 실습용 컨테이너 생성

```powershell
docker run -dit --name permission-test ubuntu bash
```

### 11.2 컨테이너 접속

```powershell
docker exec -it permission-test bash
```

### 11.3 실습용 스크립트 생성

```bash
cd /tmp

printf '#!/bin/sh\necho Permission-Test-Success\n' > test.sh
```

### 11.4 파일 권한을 644로 설정

```bash
chmod 644 test.sh
ls -l test.sh
```

실행 결과:

```text
-rw-r--r-- 1 root root 39 Nov 12 02:30 test.sh
```

### 11.5 실행 권한 부여

```bash
chmod 755 test.sh
```

### 11.6 변경된 권한 확인

```bash
ls -l test.sh
```

실행 결과:

```text
-rwxr-xr-x 1 root root 39 Nov 12 02:30 test.sh
```

### 11.7 스크립트 실행

```bash
./test.sh
```

실행 결과:

```text
Permission-Test-Success
```

**검증 결과:** 파일 권한을 644에서 755로 변경한 뒤 스크립트를 직접 실행할 수 있음을 확인했습니다.

---

## 12. Docker 바인드 마운트 실습

### 12.1 실습 목적

Windows 호스트 디렉터리와 Docker 컨테이너 디렉터리를 연결하고, 컨테이너에서 변경한 파일 내용이 호스트에도 반영되는지 확인합니다.

### 12.2 디렉터리 및 파일 생성

PowerShell에서:

```powershell
New-Item -ItemType Directory -Force bind-data

Set-Content -Path .\bind-data\message.txt -Value "Before: Hello from Windows"
```

파일 내용 확인:

```powershell
Get-Content .\bind-data\message.txt
```

실행 결과:

```text
Before: Hello from Windows
```

### 12.3 바인드 마운트 연결

```powershell
docker run --rm -it --mount "type=bind,source=$((Get-Location).Path)\bind-data,target=/data" alpine sh
```

명령어 설명:

| 항목 | 의미 |
|---|---|
| --rm | 컨테이너 종료 시 자동 삭제 |
| -it | 대화형 터미널 실행 |
| type=bind | 바인드 마운트 지정 |
| source | Windows 호스트 디렉터리 |
| target | 컨테이너 내부 연결 경로 |
| alpine | 사용할 이미지 |
| sh | 실행할 셸 |

### 12.4 컨테이너에서 파일 확인

```sh
cat /data/message.txt
```

실행 결과:

```text
Before: Hello from Windows
```

### 12.5 컨테이너에서 파일 수정

```sh
echo "After: Hello from Docker" > /data/message.txt
```

### 12.6 컨테이너 종료

```sh
exit
```

### 12.7 Windows에서 변경 내용 확인

```powershell
Get-Content .\bind-data\message.txt
```

실행 결과:

```text
After: Hello from Docker
```

**검증 결과:** Docker 컨테이너에서 수정한 파일 내용이 Windows 호스트 파일에도 반영됨을 확인했습니다.

---

## 13. Docker Volume 영속성 검증

### 13.1 실습 목적

Docker Volume을 생성한 뒤 컨테이너를 삭제하고 새 컨테이너를 생성해도 기존 데이터가 유지되는지 확인합니다.

### 13.2 Docker Volume 생성

```powershell
docker volume create assignment-volume
```

실행 결과:

```text
assignment-volume
```

### 13.3 볼륨 목록 확인

```powershell
docker volume ls
```

실행 결과:

```text
DRIVER    VOLUME NAME
local     assignment-volume
```

### 13.4 볼륨 상세정보 확인

```powershell
docker volume inspect assignment-volume
```

실행 결과:

```json
[
  {
    "CreatedAt": "2026-11-12T04:34:37Z",
    "Driver": "local",
    "Labels": null,
    "Mountpoint": "/var/lib/docker/volumes/assignment-volume/_data",
    "Name": "assignment-volume",
    "Options": null,
    "Scope": "local"
  }
]
```

### 13.5 볼륨을 연결한 컨테이너 생성

```powershell
docker run -d --name volume-test --mount type=volume,source=assignment-volume,target=/data ubuntu sleep infinity
```

실행 결과:

```text
e50ea319e4957dbb968a0623dbd7d99e747833d77e482cd009714ba42aec10eb
```

### 13.6 마운트 연결 상태 확인

```powershell
docker inspect volume-test --format '{{json .Mounts}}'
```

주요 확인 내용:

```json
{
  "Type": "volume",
  "Name": "assignment-volume",
  "Destination": "/data",
  "RW": true
}
```

### 13.7 컨테이너 내부에 데이터 저장

```powershell
docker exec volume-test sh -c "echo Persistent-Docker-Volume-Data > /data/result.txt"
```

### 13.8 저장된 파일 내용 확인

```powershell
docker exec volume-test cat /data/result.txt
```

실행 결과:

```text
Persistent-Docker-Volume-Data
```

### 13.9 볼륨 내부 파일 확인

```powershell
docker exec volume-test ls -l /data
```

실행 결과:

```text
total 4
-rw-r--r-- 1 root root 30 Nov 12 04:43 result.txt
```

### 13.10 기존 컨테이너 삭제

```powershell
docker rm -f volume-test
```

실행 결과:

```text
volume-test
```

### 13.11 볼륨 유지 여부 확인

```powershell
docker volume ls
```

실행 결과:

```text
DRIVER    VOLUME NAME
local     assignment-volume
```

### 13.12 새로운 컨테이너 생성

```powershell
docker run -d --name volume-test-new --mount type=volume,source=assignment-volume,target=/data ubuntu sleep infinity
```

### 13.13 기존 데이터 확인

```powershell
docker exec volume-test-new cat /data/result.txt
```

실행 결과:

```text
Persistent-Docker-Volume-Data
```

**검증 결과:** 기존 컨테이너를 삭제한 뒤 동일한 Docker Volume을 새 컨테이너에 연결해도 저장된 데이터가 유지됨을 확인했습니다.

---

## 14. 트러블슈팅

### 14.1 문제 1: Docker 포트 충돌

**문제 상황**

Flask 컨테이너를 8080 포트로 실행하려 했으나 오류가 발생했습니다.

```powershell
docker run -d --name flask-web -p 8080:5000 flask-assignment
```

오류 메시지:

```text
docker: Error response from daemon:
failed to set up container networking:
driver failed programming external connectivity
on endpoint flask-web
```

**원인 가설**

8080 포트를 다른 컨테이너가 사용하고 있을 가능성이 있다고 판단했습니다.

**확인 방법**

```powershell
docker ps
```

기존 Nginx 컨테이너가 8080 포트를 사용하고 있음을 확인했습니다.

**해결 방법**

실패한 컨테이너를 삭제했습니다.

```powershell
docker rm flask-web
```

호스트 포트를 8082로 변경하여 다시 실행했습니다.

```powershell
docker run -d --name flask-web -p 8082:5000 flask-assignment
```

**해결 결과**

포트 충돌 없이 컨테이너가 생성되었습니다.

접속 주소:

```text
http://localhost:8082
```

### 14.2 문제 2: Ubuntu 컨테이너 즉시 종료

**문제 상황**

다음 명령어로 컨테이너를 생성했으나 실행 직후 종료되었습니다.

```powershell
docker run --name test-exit ubuntu
```

**원인 가설**

컨테이너의 메인 프로세스가 종료되어 컨테이너도 종료되었을 것으로 판단했습니다.

**확인 방법**

```powershell
docker ps -a
```

컨테이너 상태가 `Exited`인지 확인했습니다.

**해결 방법**

Bash를 대화형 터미널과 함께 실행하고 입력 스트림을 유지하도록 설정했습니다.

```powershell
docker run -dit --name test-keep ubuntu bash
```

**해결 결과**

Bash 프로세스가 실행 상태를 유지하여 컨테이너도 계속 실행되었습니다.

```powershell
docker ps
```

실행 결과:

```text
NAMES       STATUS
test-keep   Up 2 minutes
```

---

## 15. 실습 결과 요약

| 실습 항목 | 수행 내용 | 결과 |
|---|---|---|
| 개발환경 확인 | Windows, Docker, Git 버전 확인 | 완료 |
| 파일 권한 관리 | chmod 644 → 755 | 완료 |
| 디렉터리 생성 | 프로젝트 구조 생성 | 완료 |
| Flask 웹서버 | Python 웹 애플리케이션 작성 | 완료 |
| Dockerfile | Flask 실행 이미지 정의 | 완료 |
| Docker 이미지 | 커스텀 이미지 빌드 | 완료 |
| 포트 매핑 | 8082, 8083 포트 사용 | 컨테이너 생성 확인 |
| Docker Attach | 기존 프로세스 연결 | 실습 |
| Docker Exec | 실행 중 컨테이너에 명령 실행 | 완료 |
| 바인드 마운트 | 호스트·컨테이너 파일 변경 공유 | 검증 완료 |
| Docker Volume | 컨테이너 삭제 후 데이터 유지 | 검증 완료 |
| 트러블슈팅 | 포트 충돌, 컨테이너 종료 문제 | 2건 해결 |
| Git/GitHub | 버전 확인 | Commit/Push 증거 추가 필요 |

---

## 16. Git/GitHub 버전관리

본 Repository는 GitHub와 Codyssey 연동 및 실습 결과 관리를 위해 사용합니다.

### 16.1 Git 저장소 초기화

```powershell
git init
```

### 16.2 파일 추가

```powershell
git add .
```

### 16.3 커밋 생성

```powershell
git commit -m "Add Docker mission files and documentation"
```

### 16.4 GitHub 원격 저장소 연결

```powershell
git remote add origin <REPOSITORY_URL>
```

`<REPOSITORY_URL>`은 실제 GitHub 저장소 주소로 변경합니다.

### 16.5 GitHub에 업로드

```powershell
git branch -M main
git push -u origin main
```

이미 GitHub 저장소에 기존 커밋이 있는 경우에는 먼저 원격 저장소 이력을 확인하고 통합해야 할 수 있습니다.

위 명령어는 향후 수행할 Git/GitHub 작업 절차이며, 실제 실행 완료 여부는 아직 확인되지 않았습니다.

---

## 17. 실습 증거자료 관리

실습 결과를 `evidence/` 디렉터리에 저장합니다.

권장 증거자료:

| 파일명 | 증거 내용 |
|---|---|
| environment.png | Docker 및 Git 버전 |
| docker-images.png | Docker 이미지 목록 |
| docker-ps.png | 컨테이너 상태 |
| flask-web.png | 웹브라우저 접속 화면 |
| permission.png | chmod 변경 전후 |
| bind-mount.png | 파일 변경 반영 |
| volume-persistence.png | 데이터 영속성 검증 |
| troubleshooting.png | 오류 및 해결 결과 |

실제 생성한 스크린샷만 저장하며, 위 파일명은 권장 예시입니다.

---

## 18. 결론

이번 실습을 통해 Docker 기반 웹 애플리케이션 실행환경을 구축하고 이미지 생성, 컨테이너 실행, 포트 매핑, 파일 권한 변경, 데이터 저장 및 영속성 관리 방법을 학습했습니다.

특히 바인드 마운트 실습에서는 Windows와 컨테이너 사이의 파일 변경 반영을 확인했으며, Docker Volume 실습에서는 컨테이너를 삭제해도 데이터가 유지된다는 사실을 직접 검증했습니다.

또한 포트 충돌과 컨테이너 즉시 종료 문제를 해결하면서 Docker 실행 오류를 분석하고 적절한 명령어로 문제를 해결하는 경험을 쌓았습니다.

향후 GitHub 저장소에 실습 파일과 증거자료를 업로드하고 Codyssey와 연동하여 프로젝트 결과를 관리할 예정입니다.
