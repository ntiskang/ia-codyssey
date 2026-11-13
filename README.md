# OD Mission 1 — Docker·Linux·Git 실습

## 1. 실습 개요와 환경

- 호스트: Windows / PowerShell
- 컨테이너: Docker Desktop의 Linux 컨테이너
- 실습 프로젝트: `od-mission1`
- Flask 이미지: `flask-assignment`
- Flask 컨테이너: `flask-web`
- Flask 내부 포트: `5000`, 호스트 접속 포트: `8082`
- Docker 버전(기존 기록): `Docker version 29.9.2, build a82e528`

실행 환경 확인:

```powershell
docker --version
docker version
docker info
docker context ls
```

`docker version`의 Client/Server 항목과 `docker info`의 Server 항목으로 데몬 연결 상태를 확인합니다. Docker Desktop 자체 로그는 문제가 있을 때 별도 증거로 수집합니다.

**증거:** `evidence/03-docker-version.txt`, `evidence/03-docker-info.txt` [증거 추가 필요]

## 2. 디렉터리 생성·이동·삭제 

프로젝트 폴더를 만들고 이동한 뒤, 삭제 실습은 **별도의 임시 폴더**에서 수행합니다. 프로젝트 자체를 삭제하지 않습니다.

```powershell
mkdir od-mission1
cd od-mission1
Get-Location
New-Item -ItemType Directory -Path .\delete-test
Get-ChildItem
Remove-Item -Path .\delete-test -Recurse -Force
Test-Path .\delete-test
```

마지막 `Test-Path`의 실제 출력이 `False`이면 임시 폴더가 삭제되었다는 뜻입니다. 생성·이동·삭제 과정의 콘솔 출력과 캡처를 저장합니다. 이미 `od-mission1`에 있다면 `mkdir od-mission1`을 다시 실행하지 말고 현재 위치를 확인하세요.

**증거:** `evidence/01-directory-operations.txt`, `evidence/01-directory-operations.png` [증거 추가 필요]

## 3. Linux 파일 권한 
Linux/Alpine 컨테이너의 `sh`에서 다음을 실행합니다.

```sh
printf '#!/bin/sh\necho Permission-Test-Success\n' > test.sh
ls -l test.sh
chmod 755 test.sh
ls -l test.sh
./test.sh
```

`755`는 소유자에게 읽기·쓰기·실행(`rwx` = 7), 그룹과 기타 사용자에게 읽기·실행(`r-x` = 5)을 허용합니다. 스크립트를 실행할 수 있게 하면서 다른 사용자에게 수정 권한을 주지 않기 위해 선택했습니다. `4=읽기`, `2=쓰기`, `1=실행`입니다. 특수 권한 비트에는 setuid, setgid, sticky bit가 있으며 이번 기본 실습의 범위는 아닙니다.

**증거:** 변경 전후 `ls -l` 및 `Permission-Test-Success`가 표시된 `evidence/02-permissions.txt` [기존 기록 대조 필요]

## 4. Docker 정상 작동 확인 

```powershell
docker run --rm hello-world
```

실행 결과에 `Hello from Docker!` 메시지가 나타나는지 확인합니다. 이는 Docker 클라이언트가 데몬에 요청하고 데몬이 이미지를 내려받거나 찾아 컨테이너를 실행했다는 기본 점검입니다. **실제 콘솔 출력을 첨부해야 PASS 증거가 됩니다.**

**증거:** `evidence/04-hello-world.txt`, `evidence/04-hello-world.png` [증거 추가 필요]

## 5. 이미지와 컨테이너의 차이 

**이미지(image)**는 프로그램 코드·라이브러리·실행 설정을 담은 읽기 전용 실행 템플릿입니다. `docker build`는 Dockerfile의 지시를 바탕으로 이미지를 만듭니다. **컨테이너(container)**는 그 이미지를 기반으로 생성한 실행 인스턴스입니다. `docker run`은 컨테이너를 생성하고 시작하며, 실행 중 생성된 변경 내용은 컨테이너의 쓰기 가능 계층에 기록됩니다. 컨테이너를 삭제하면 그 계층도 사라지므로 보존할 데이터는 바인드 마운트나 볼륨에 저장합니다.

```powershell
docker images
docker ps
docker ps -a
```

기존 기록에는 `nginx:latest` 이미지(`600f7cd45e27`, `243MB`)가 있습니다. 실제 최신 목록과 다를 수 있습니다.

**정리 실습(임시 컨테이너와 이미지에 한정):**

```powershell
docker run -d --name cleanup-demo nginx:latest
docker ps -a --filter "name=cleanup-demo"
docker rm -f cleanup-demo
docker ps -a --filter "name=cleanup-demo"
```

이미지 삭제는 해당 이미지를 사용하는 다른 컨테이너가 없는지 확인한 뒤 진행합니다. `nginx:latest`를 다른 실습에서 사용 중이면 삭제하지 않습니다. 이미지 정리 예시는 `docker rmi <사용하지-않는-이미지-ID>`입니다.

**증거:** `evidence/05-images-containers.txt`, `evidence/05-cleanup.txt` [증거 추가 필요]

## 6. 프로젝트 구조와 설계 이유

```text
od-mission1/
├── Dockerfile
├── requirements.txt
├── README.md
├── app/
│   └── app.py
├── bind-data/
│   └── message.txt
└── evidence/
    ├── 01-directory-operations.txt
    ├── 02-permissions.txt
    └── ...
```

`Dockerfile`과 `requirements.txt`는 빌드 컨텍스트의 루트에 두어 `docker build .`와 `COPY requirements.txt .`를 간단하게 유지합니다. 애플리케이션 코드는 `app/`에 모으고, 바인드 마운트 자료는 `bind-data/`, 제출 증거는 `evidence/`에 분리해 재현성과 검토 편의성을 높입니다. 위 트리는 **권장 구조**이며 실제 존재 여부는 `tree /F`로 확인해야 합니다.

## 7. Flask 이미지 빌드 

`Dockerfile`:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ .
EXPOSE 5000
CMD ["python3", "app.py"]
```

`requirements.txt`에는 Flask 앱에 필요한 의존성을 기록합니다. `app/app.py`는 `0.0.0.0:5000`에서 요청을 받도록 설정해야 합니다. `EXPOSE 5000`은 이미지의 사용 포트를 문서화하며, 호스트 포트를 자동 공개하지는 않습니다.

```powershell
docker build --progress=plain --no-cache -t flask-assignment . 2>&1 | Tee-Object -FilePath .\evidence\06-build-full.txt
docker images flask-assignment
```

`--progress=plain`은 상세 빌드 단계를 텍스트로 출력합니다. `Tee-Object`로 **실제 전체 로그**를 저장합니다. 로그 끝의 성공 여부를 확인하고 오류가 있다면 오류 메시지도 삭제하지 않습니다. PowerShell 파이프라인을 거친 종료 코드 확인은 환경에 따라 주의가 필요하므로 이미지 생성 여부도 함께 확인합니다.

**증거:** `evidence/06-build-full.txt`, `evidence/06-build-success.png` [증거 추가 필요]

## 8. 컨테이너 실행과 포트 접속 검증

### 실행 전 점검

- [ ] Docker Desktop 실행 및 `docker info` 성공
- [ ] `flask-assignment` 이미지 존재
- [ ] `flask-web`이라는 이름의 기존 컨테이너 유무 확인
- [ ] 호스트 `8082` 포트가 다른 프로세스에서 사용 중인지 확인
- [ ] `app.py`가 컨테이너 안에서 `0.0.0.0:5000`으로 수신하는지 확인

```powershell
docker ps -a --filter "name=flask-web"
Get-NetTCPConnection -LocalPort 8082 -ErrorAction SilentlyContinue
```

기존 `flask-web` 컨테이너가 있으면 로그와 필요한 데이터를 확인한 다음, 교체가 필요할 때만 삭제합니다.

```powershell
docker run -d --name flask-web -p 8082:5000 flask-assignment
docker ps --filter "name=flask-web"
docker logs flask-web
curl.exe -i http://localhost:8082/
```

`curl.exe -i` 출력에서 HTTP 상태 코드와 응답 본문을 확인합니다. 정상 접속이면 브라우저 `http://localhost:8082/` 화면도 캡처합니다. 응답 상태와 본문은 앱 구현에 따라 달라지므로 실제 결과를 기록해야 합니다.

**증거:** `evidence/07-http-response.txt`, `evidence/07-browser.png`, `evidence/07-container-logs.txt` [증거 추가 필요]

### 포트 포워딩과 네트워크 네임스페이스

`-p 8082:5000`은 **호스트의 8082 포트**로 들어온 연결을 **컨테이너의 5000 포트**로 전달합니다. Linux 컨테이너는 일반적으로 독립된 네트워크 네임스페이스를 사용하여 호스트와 별도의 네트워크 인터페이스·IP·포트 공간을 갖습니다. 포트 매핑은 이렇게 분리된 두 네트워크 공간 사이에 외부 접근 경로를 마련하는 기능입니다. 따라서 컨테이너 내부 `localhost:5000`과 호스트 `localhost:5000`은 같은 대상을 의미하지 않습니다.

## 9. 바인드 마운트와 Docker Volume 
### 바인드 마운트

```powershell
New-Item -ItemType Directory -Force .\bind-data
docker run --rm -it --mount "type=bind,source=$((Get-Location).Path)\bind-data,target=/data" alpine sh
```

PowerShell에서 `Get-Location`으로 얻은 **호스트 절대경로**를 Docker의 `source`에 전달합니다. 컨테이너 내부는 `/data`라는 **절대경로**를 사용합니다. README의 재현 명령은 작업 디렉터리를 명확히 하고, 상대경로는 프로젝트 내부 파일 탐색에만 쓰는 것을 권장합니다.

### Docker 관리 볼륨과 영속성

```powershell
docker volume create assignment-volume
docker run -d --name volume-test -v assignment-volume:/data alpine sleep 3600
docker exec volume-test sh -c 'echo Persistent-Docker-Volume-Data > /data/result.txt'
docker exec volume-test cat /data/result.txt
docker rm -f volume-test
docker run --rm -v assignment-volume:/data alpine cat /data/result.txt
```

컨테이너를 삭제하고 새 컨테이너에 같은 볼륨을 연결했을 때 데이터가 남아 있으면 **컨테이너 수명과 데이터 수명이 분리됨**을 확인할 수 있습니다.

### 백업·복구 원칙

볼륨은 컨테이너 삭제에 대비한 **영속 저장소**이지, 그 자체로 백업은 아닙니다. 중요한 데이터는 주기적으로 별도의 호스트 디스크나 안전한 외부 저장소에 백업하고, 복구 시험을 수행해야 합니다. 백업 전에는 가능하면 해당 데이터를 쓰는 애플리케이션을 정지하거나 일관성 있는 스냅샷을 사용합니다. 백업 파일의 날짜·크기·복구 확인 결과를 함께 기록합니다. 이번 평가 항목에서는 구체적인 백업 명령보다 이 운영 원칙을 문서화합니다.

**증거:** `evidence/08-volume-persistence.txt`, `evidence/08-backup-policy.md` [기존 실행 기록 대조 및 보완 필요]

## 10. Git·GitHub 제출 확인 

```powershell
git init
git status
git remote -v
```

원격 저장소가 **아직 없을 때만** 다음 명령어를 실행합니다.

```powershell
git remote add origin <REPOSITORY_URL>
```

이미 `origin`이 존재하고 URL을 수정해야 한다면 `git remote set-url origin <REPOSITORY_URL>`을 사용합니다.

```powershell
git add README.md Dockerfile requirements.txt app evidence
git commit -m "Document Docker mission evidence"
git branch -M main
git push -u origin main
git remote -v
git log -1 --oneline
```

`evidence/`가 존재해야 `git add`에 포함할 수 있습니다. 원격 저장소에 기존 커밋이 있다면 무조건 `push`하지 말고 먼저 원격 이력을 확인하고 통합합니다. `git push`가 성공한 뒤 실제 출력과 GitHub의 해당 커밋 URL을 증거로 남깁니다. 비밀번호·토큰·개인정보가 담긴 로그는 업로드 전에 가립니다.

**증거:** `evidence/09-git-remote.txt`, `evidence/09-git-push.txt`, 실제 GitHub 커밋 링크 [증거 추가 필요]

## 11. 트러블슈팅과 진단

| 증상 | 확인 방법 | 대응 방법 |
|---|---|---|
| 호스트 포트 충돌 | `docker ps`, `Get-NetTCPConnection -LocalPort 8082` | 기존 컨테이너·프로세스를 확인한 뒤 포트 변경 또는 불필요한 점유 해제 |
| 컨테이너 이름 충돌 | `docker ps -a --filter "name=flask-web"` | 기존 컨테이너 보존 필요성을 확인한 후 삭제·이름 변경 |
| Docker 데몬 연결 실패 | `docker info`, Docker Desktop 상태 | Docker Desktop 시작 및 Linux 컨테이너 엔진 상태 확인 |
| Flask 컨테이너 종료 | `docker ps -a`, `docker logs flask-web` | 앱 오류·의존성·실행 명령 점검 |
| 볼륨 파일 없음 | `docker inspect volume-test`, 컨테이너 내부 `ls -l /data` | 볼륨 이름·마운트 대상·파일 생성 명령 재확인 |

Windows에서 포트 소유 프로세스를 확인하는 방법:

```powershell
netstat -ano | findstr :8082
Get-NetTCPConnection -LocalPort 8082 -ErrorAction SilentlyContinue
# PID를 확인한 뒤 필요한 경우:
Get-Process -Id <PID>
```

`<PID>`는 실제 숫자로 바꿉니다. Linux 호스트에서는 `ss -ltnp` 또는 `sudo lsof -i :8082`로 점유 상태를 확인할 수 있습니다.

문제마다 **가설 → 확인 명령 → 원본 출력 → 조치 → 재검증** 순서로 기록합니다. 기존 오류 로그를 요약할 때도 원본 전체를 `evidence/`에 보관하고 아래처럼 상대 링크를 연결합니다.

- [Docker 빌드 전체 로그](evidence/06-build-full.txt)
- [HTTP 접속 결과](evidence/07-http-response.txt)
- [Git 원격 저장소 확인](evidence/09-git-remote.txt)
- [Git Push 결과](evidence/09-git-push.txt)

위 링크는 **파일을 실제로 생성·추가해야 유효**합니다.

