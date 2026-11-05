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

3. 수행항목 체크리스트
   - 터미널:
   - 권한:
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
   - Docker:
     PS C:\Windows\System32> docker --version
Docker version 29.9.2, build a82e528
PS C:\Windows\System32> docker info
Client:
 Version:    29.9.2
 Context:    desktop-linux
 Debug Mode: false
 Plugins:
  agent: Docker AI Agent Runner (Docker Inc.)
    Version:  v1.152.0
    Path:     C:\Users\User\.docker\cli-plugins\docker-agent.exe
  ai: Docker AI Agent - Ask Gordon (Docker Inc.)
    Version:  v1.33.0
    Path:     C:\Users\User\.docker\cli-plugins\docker-ai.exe
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.38.1
    Path:     C:\Users\User\.docker\cli-plugins\docker-buildx.exe
  compose: Docker Compose (Docker Inc.)
    Version:  v5.6.1
    Path:     C:\Users\User\.docker\cli-plugins\docker-compose.exe
  debug: Get a shell into any image or container (Docker Inc.)
    Version:  0.49.0
    Path:     C:\Users\User\.docker\cli-plugins\docker-debug.exe
  desktop: Docker Desktop commands (Docker Inc.)
    Version:  4.97.0
    Path:     C:\Users\User\.docker\cli-plugins\docker-desktop.exe
  dhi: CLI for managing Docker Hardened Images (Docker Inc.)
    Version:  v0.0.9
    Path:     C:\Users\User\.docker\cli-plugins\docker-dhi.exe
  extension: Manages Docker extensions (Docker Inc.)
    Version:  v0.2.32
    Path:     C:\Users\User\.docker\cli-plugins\docker-extension.exe
  init: Creates Docker-related starter files for your project (Docker Inc.)
    Version:  v1.4.1
    Path:     C:\Users\User\.docker\cli-plugins\docker-init.exe
  mcp: Docker MCP Plugin (Docker Inc.)
    Version:  v0.44.2
    Path:     C:\Users\User\.docker\cli-plugins\docker-mcp.exe
  model: Docker Model Runner (Docker Inc.)
    Version:  v1.2.9
    Path:     C:\Users\User\.docker\cli-plugins\docker-model.exe
  offload: Docker Offload (Docker Inc.)
    Version:  v0.7.21
    Path:     C:\Users\User\.docker\cli-plugins\docker-offload.exe
  pass: Docker Pass Secrets Manager Plugin (beta) (Docker Inc.)
    Version:  v0.3.2
    Path:     C:\Users\User\.docker\cli-plugins\docker-pass.exe
  sandbox: "docker sandbox" is deprecated, use Docker Sandboxes instead (Docker Inc.)
    Version:  v0.13.0
    Path:     C:\Users\User\.docker\cli-plugins\docker-sandbox.exe
  scout: Docker Scout (Docker Inc.)
    Version:  v1.27.0
    Path:     C:\Users\User\.docker\cli-plugins\docker-scout.exe

Server:
 Containers: 7
  Running: 0
  Paused: 0
  Stopped: 7
 Images: 5
 Server Version: 29.9.2
 Storage Driver: overlayfs
  driver-type: io.containerd.snapshotter.v1
 Logging Driver: local
 Cgroup Driver: cgroupfs
 Cgroup Version: 2
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local splunk syslog
 CDI spec directories:
  /etc/cdi
  /var/run/cdi
 Discovered Devices:
  cdi: docker.com/gpu=webgpu
 Swarm: inactive
 Runtimes: io.containerd.runc.v2 nvidia runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: b7a25261e029d68978bbf290df0a62fc819b3c51
 runc version: v1.5.2-0-g29dd3dc2
 init version: de40ad0
 Security Options:
  seccomp
   Profile: builtin
  cgroupns
 Kernel Version: 6.18.54.1-microsoft-standard-WSL2
 Operating System: Docker Desktop
 OSType: linux
 Architecture: x86_64
 CPUs: 16
 Total Memory: 7.619GiB
 Name: docker-desktop
 ID: 6a175294-4d78-4aa1-a879-2d767e0fe02c
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 HTTP Proxy: http.docker.internal:3128
 HTTPS Proxy: http.docker.internal:3128
 No Proxy: hubproxy.docker.internal
 Labels:
  com.docker.desktop.address=npipe://\\.\pipe\docker_cli
 Experimental: false
 Insecure Registries:
  hubproxy.docker.internal:5555
  127.0.0.0/8
  ::1/128
 Live Restore Enabled: false
 Firewall Backend: iptables

PS C:\Windows\System32> docker images
                                                                                                          i Info →   U  In Use
IMAGE                  ID             DISK USAGE   CONTENT SIZE   EXTRA
alpine:latest          be2656061b53         13MB         3.94MB    U
busybox:latest         a46257e06c82       6.81MB         2.23MB
hello-world:latest     c567b231f656       25.9kB         9.49kB    U
my-web-server:latest   da33294fd7a8        241MB         63.9MB    U
nginx:latest           600f7cd45e27        243MB         66.8MB    U
PS C:\Windows\System32> docker ps -a
CONTAINER ID   IMAGE           COMMAND                   CREATED      STATUS                    PORTS                  NAMES
2cfb48c716f4   hello-world     "/hello"                  4 days ago   Exited (0) 4 days ago                            modest_moore
fc5738ed67f1   nginx           "/docker-entrypoint.…"   5 days ago   Exited (255) 4 days ago   0.0.0.0:8888->80/tcp   vol-test
d555583ae5bc   my-web-server   "/docker-entrypoint.…"   5 days ago   Exited (255) 4 days ago   0.0.0.0:8080->80/tcp   web-mission
a6da93a2c848   alpine          "sleep 100"               5 days ago   Exited (0) 5 days ago                            recursing_black
0fe926a12ed0   hello-world     "/hello"                  5 days ago   Exited (0) 5 days ago                            jolly_wilson
feb2ffb8a849   hello-world     "/hello"                  5 days ago   Exited (0) 5 days ago                            mystifying_cohen
1c2c2f9fd41b   nginx           "/docker-entrypoint.…"   6 days ago   Exited (255) 6 days ago   0.0.0.0:8080->80/tcp   web-mission-check
PS C:\Windows\System32> docker logs -help
unknown shorthand flag: 'e' in -elp

Usage:  docker logs [OPTIONS] CONTAINER

Run 'docker logs --help' for more information
PS C:\Windows\System32> docker logs --help
Usage:  docker logs [OPTIONS] CONTAINER

Fetch the logs of a container

Aliases:
  docker container logs, docker logs

Options:
      --details        Show extra details provided to logs
  -f, --follow         Follow log output
      --since string   Show logs since timestamp (e.g.
                       "2013-01-02T13:23:37Z") or relative (e.g. "42m"
                       for 42 minutes)
  -n, --tail string    Number of lines to show from the end of the logs
                       (default "all")
  -t, --timestamps     Show timestamps
      --until string   Show logs before a timestamp (e.g.
                       "2013-01-02T13:23:37Z") or relative (e.g. "42m"
                       for 42 minutes)
   - Dockerfile:
   - 포트:
   - 볼륨:
   - Git/GitHUb:
  
4. 검증방법(어떤 명령으로 무엇을 확인했는가) + 결과 위치 링크
5. 트러블 슈팅 2건 이상(문제->원인 가설-> 확인 -> 해결(대안)
   




