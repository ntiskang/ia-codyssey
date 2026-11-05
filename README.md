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
PS C:\Users\User> git --version
git version 2.56.0.windows.4
PS C:\Users\User>




