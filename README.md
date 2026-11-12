# ia-codyssey
Github와 Codyssey를 연동해기 위해 만들어진 Repository

1. 프로젝트 개요: 미션 요약
 - 리눅스 CLI(터미널), Docker(컨테이너), GIt/GitHub(버전관리 및 협업) 사용
 - 터미널로 작업 디렉토리와 권한을 정리한 뒤 Docker를 설치 및 점검하고 컨테이너를 실행/관리
 - 간단한 웹서버를 Dockerfile로 컨테이너화하고 포트 매핑으로 접속을 확인하며, 바인드 마운트/볼륨으로 변경 반영과 데이터 영속성을 직접 검증

2. 실행환경
   - OS/Shell/Terminal:
   - S C:\Users\User> Get-ComputerInfo | Select-Object

WindowsBuildLabEx                                       : 26100.1.amd64fre.ge_release.240331-1435
WindowsCurrentVersion                                   : 6.3
WindowsEditionId                                        : Professional
WindowsInstallationType                                 : Client
WindowsInstallDateFromRegistry                          : 2026-10-14 오전 8:29:51
WindowsProductId                                        : 00330-54091-78055-AAOEM
WindowsProductName                                      : Windows 10 Pro

PS C:\Users\User> $PSVersionTable.PSVersion

Major  Minor  Build  Revision
-----  -----  -----  --------
5      1      26100  9711

PS C:\Users\User> $env:WT_SESSION
9b0e8c52-6a75-470e-bd05-fae6d4404f84

PS C:\Users\User> docker --version
Docker version 29.9.2, build a82e528

PS C:\Users\User> docker version
Client:
 Version:           29.9.2
 API version:       1.56
 Go version:        go1.26.10
 Git commit:        a82e528
 Built:             Tue Oct 20 19:44:07 2026
 OS/Arch:           windows/amd64
 Context:           desktop-linux

Server: Docker Desktop 4.97.0 (244584)
 Engine:
  Version:          29.9.2
  API version:      1.56 (minimum version 1.40)
  Go version:       go1.26.10
  Git commit:       0367cbe
  Built:            Tue Oct 20 18:45:02 2026
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          v2.4.2
  GitCommit:        b7a25261e029d68978bbf290df0a62fc819b3c51
 runc:
  Version:          1.5.2
  GitCommit:        v1.5.2-0-g29dd3dc2
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0

PS C:\Users\User> docker compose version
Docker Compose version v5.6.1

Git버전 확인
   PS> C:\Users\User> git --version
      git version 2.56.0.windows.4

Docker버전 확인
   PS> docker --version
     Docker version 29.9.2, build a82e528

Docker정보 확인 
     PS> docker info
         Client:
         Version:    29.9.2
         Context:    desktop-linux
Images확인
      PS> docker images
     IMAGE                  ID             DISK USAGE   CONTENT SIZE   EXTRA
     nginx:latest           600f7cd45e27        243MB         66.8MB    U

미실행 컨테이너 포함 컨테이너 확인
     PS>docker ps -a

3. 권한 변경 실습
     r / w / x의 의미
     r	Read	4	파일 내용을 읽을 수 있음
     w	Write	2	파일 내용을 수정할 수 있음
     x	Execute	1	파일을 실행할 수 있음
     0	해당 권한 없음

     각 권한의 숫자를 더하면 권한 값, 예를 들어 rwx는 4+2+1=7.
     755와 644의 해석 규칙
     파일 권한은 세 종류의 사용자에게 각각 부여.
       - Owner (소유자): 파일을 소유한 사용자
       - Group (그룹): 파일이 속한 그룹의 사용자
       - Others (기타): 그 외의 모든 사용자
 
4. 디렉토리 생성 및 웹실행 파일(python flask) 만들기
   mkdir od-mission1
   cd od-mission1
   mkdir app
   mkdir evidence
   notepad app\app.py

5. 파이선 웹실행 파일 내용

   from flask import Flask
   app = Flask(__name__)
   @app.route("/")
   def home():
     return """
     <h1>Odessey Docker Web Server Assignment</h1>
     <p>Hello! My Docker container is running.</p>
     <p>Port Mapping: 8080 -> 5000</p>
     """
  if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5000)

6. Dockerfile 생성
   FROM python:3.12-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   COPY app/ .
   EXPOSE 5000
   CMD ["python", "app.py"]

8. 포트: 포트 매핑 
   docker run -d -p 8080:5000 flask-app 
   호스트 컴퓨터 포트: Docker 내부 포트, 실행할 Docker이미지
   
9. Attach 실습
    우분투 이미지로 test-exit 컨테이너 생성 
        ps>docker run --name test-exit ubuntu
    기존 프로세스에 연결
        ps>docker attach test-keep
    ubuntu명령 프롬프트로 변경
        ps>root@a1b2c3d4:/#
           </>bash
              pwd
              ls
              exit
10. Exec 실습
     종료된 컨테이너 다시 실행 
          ps>docker start test-keep
     exec실행
          ps>docker exec -it test-keep bash
     컨테이너 내부에서 ubuntu명령 실행
          </>bash
             pwd
             ls
             exit
     프로세스는 종료됐지만 컨테이너는 그대로 살아 있음 확인
          ps>docker ps  
           NAMES       STATUS
           test-keep   Up 2 minutes

11. 기존 Dockerfile 기반 커스텀 이미지 제작 실습
    목표: 현재 작업 중인 od-misson1 프로젝트의 Dockerfile을 활용하여 Flask 웹서버가 포함된 커스텀 Docker 이미지 제작
    (1) 현 디렉토리 구조확인
      PS>tree /F
     
C:.
│  Dockerfile
│  requirements.txt
├─app
│      app.py
│      Dockerfile.txt
│      requirements.txt
└─evidence

    (2) Custom이미지 제작
      ps>docker build -t flask-custom:v1 .
    (3) 생성 이미지 확인
      ps> docker images
                                                                                                                                 i Info →   U  In Use
IMAGE                     ID             DISK USAGE   CONTENT SIZE   EXTRA
flask-assignment:latest   fd734c6f548e        198MB         48.3MB
flask-custom:v1           a8e1b37e2eb5        198MB         48.3MB
flask-web:latest          ea0696aaa1a9        198MB         48.3MB
mysql:latest              3819b2b23835       1.08GB          304MB
nginx:latest              165ddde8751e        243MB         66.8MB    U
python:latest             8c9a3bf2d6de       1.65GB          437MB
ubuntu:latest             6a06111c3b0a        163MB         45.9MB

     (4) 커스텀 이미지로 다른 포트에  컨테이너 생성
        ps>docker run -d --name flask-custom-web -p 8083:5000 flask-custom:v1

14. Docker 파일 권한 확인·변경
    (1) 권한변경 실습용 컨테이너 생성
        ps>docker run -dit --name permission-test ubuntu bash
    (2) 컨테이너 접속
        ps>docker exec -it permission-test bash
    (3) 셸 스크립트 파일 test.sh 생성 및 권한 변경 내용 출력
        root@ca3abf26dab2:/tmp# cd /tmp
        printf '#!/bin/sh\necho Permission-Test-Success\n' > test.sh
        chmod 644 test.sh
        ls -l test.sh
        -rw-r--r-- 1 root root 39 Nov 12 02:30 test.sh
    (4) 실행 권한 부여
        ps>tmp# chmod 755 test.sh
    (5) 변경된 권한 확인
        ps>tmp# ls -l test.sh
          -rwxr-xr-x 1 root root 39 Nov 12 02:30 test.sh
    (6) test.sh파일 직접 실행
        ps>tmp# ./test.sh
        Permission-Test-Success

15. Docker 바인드 마운트 생성 실습
    (1)  디렉터리를 만들고, 텍스트 파일에 내용을 저장한 다음, 저장된 내용 확인
         ps>New-Item -ItemType Directory -Force bind-data
         ps>Set-Content -Path .\bind-data\message.txt -Value "Before: Hello from Windows"
         ps>Get-Content .\bind-data\message.txt
         Before: Hello from Windows
    (2) Docker 바인드 마운트와 연결(현재 Windows 디렉터리의 bind-data를 컨테이너 내부 /data에 연결)
        ps> docker run --rm -it --mount "type=bind,source=$((Get-Location).Path)\bind-data,target=/data" alpine sh
    (3) 컨테이너 안에서 파일 내용 출력
        / # cat /data/message.txt
        Before: Hello from Windows    
    (4) 컨테이너 안에서 파일 내용 변경
        / # echo "After: Hello from Docker" > /data/message.txt
          Before: Hello from Windows
        / # echo "After: Hello from Docker" > /data/message.txt
    (5) 컨테이너 종료하고 파일 변경 여부 확인
        / # exit
        ps> Get-Content .\bind-data\message.txt
        After: Hello from Docker

16.볼륨 영속성 검증
    (1) Docker 볼륨 생성
       ps>docker volume create assignment-volume
       assignment-volum
    (2) 생성된 볼륨 목록 확인
       ps>docker volume ls
       DRIVER    VOLUME NAME
       local     assignment-volume
    (3) 볼륨 상세정보 확인
       ps> docker volume inspect assignment-volume
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
     (4) 볼륨을 연결한 컨테이너 생성
        ps> docker run -d --name volume-test --mount type=volume,source=assignment-volume,target=/data ubuntu sleep infinity
        e50ea319e4957dbb968a0623dbd7d99e747833d77e482cd009714ba42aec10eb
     (5) 연결상태 확인
        ps>docker inspect volume-test --format '{{json .Mounts}}'
        [{"Type":"volume","Name":"assignment-volume","Source":"/var/lib/docker/volumes/assignment-volume/_data","Destination":"/data","Driver":"local","Mode":"z","RW":true,"Propagation":""}]
     (6) 컨테이너 내부에 데이터 저장
        ps> docker exec volume-test sh -c "echo Persistent-Docker-Volume-Data > /data/result.txt"
     (7) 파일 내용 확인
        ps> docker exec volume-test cat /data/result.txt
        Persistent-Docker-Volume-Data
     (8) 볼륨에 파일이 저장되었는지 확인
        ps> docker exec volume-test ls -l /data
        total 4
        -rw-r--r-- 1 root root 30 Nov 12 04:43 result.txt
     (9) 컨테이너 삭제
        ps> docker rm -f volume-test
        volume-test
     (10) 볼륨 존재 확인
        PS> docker volume ls
        DRIVER    VOLUME NAME
        local     assignment-volume
     (11) 새로운 컨테이너 생성
        ps>docker run -d --name volume-test-new --mount type=volume,source=assignment-volume,target=/data ubuntu sleep infinity
     (12) 기존 파일 내용 확인
       ps>docker exec volume-test-new cat /data/result.txt
       Persistent-Docker-Volume-Data
       컨테이너를 삭제했지만 기존 데이터는 그대로 남아 있음 확인.

17. 트러블 슈팅 2건 이상(문제->원인 가설-> 확인 -> 해결(대안)
   Port Mapping: 8080 -> 5000으로 했을 때 docker: Error response from daemon: failed to set up container networking: driver failed programming external connectivity on endpoint flask-web
   원인: 8080포트를 이미 다른 컨테이너(nginx)가 사용하고 있어서 에러 발생.
   조치: 실패한 컨테이너를 삭제하고 다른 포트 8082로 변경
         ps>docker rm flask-web
         ps>docker run -d --name flask-web -p 8082:5000 flask-assignment
   결과: 에러 없이 컨테이너 생성

   컨테이너가 생성되자마자 종료되는 경우
       docker run --name test-exit ubuntu
   원인: 프로세스가 진행되지 않으면 입력이 없으므로 컨테이너도 종료
   조치:bach 입출력 프로세스가 컨테이너 안에서 실행되도록 대화형 터미널 옵션 설정
        ps>docker run -dit --name test-keep ubuntu bash
   결과: Bash가 종료되지 않고 실행 상태를 유지하므로 컨테이너도 유지
   
   
   
     




