# 남극의 펭귄을 지켜라~!

[펭귄 얼음 깨기](https://www.koreaboardgames.com/boardgame/game_view.php?prd_idx=16685) 보드게임을 Python과 Pygame으로 구현했다.

## Table of Contents

- [Background](#background)
- [Quickstart](#quickstart)
- [Usage](#usage)
- [Technology Stack](#technology-stack)
- [Contributors](#contributors)

## Background

고등학교 3학년 1학기 알고리즘 과목 프로젝트로 진행되었다.

프로젝트 진행 당시에는 git을 활용하지 않았으므로, 사후에 프로젝트 백업했던 버전 순서대로 commit 했다.

추가로 exe 파일로 변환하는 내용을 commit 했다.

## Quickstart

*세 가지* 방법으로 실행 파일을 설치 및 실행할 수 있다.

Windows에서는 .exe 파일 실행을 포함한 모든 방법을 지원하며, Linux 및 MacOS에서는 .py 파일 실행만 가능하다.

### 1. Install .zip file

📁[exe 파일 다운로드](https://github.com/jseop-lim/penguin-trap-pygame/raw/main/penguin-trap-pygame.zip)

.exe 파일과 이미지 파일이 포함된 .zip 파일만 다운 받아서 실행한다.

1. `penguin-trap-pygame.zip` 파일의 압축을 푼다.
2. penguin-trap-pygame 디렉토리 내의 `penguin-trap.exe`를 실행한다.

> ⚠️ `penguin-trap.exe`와 `picture/` 디렉토리가 반드시 같은 경로 위에 존재해야 한다.

### 2. Download Git Repository

우선 레포지토리를 GitHub에서 다운 받는다.

```shell
git clone https://github.com/jseop-lim/penguin-trap-pygame.git
```

#### 2-1. Execute .exe file

레포지토리에 포함된 `penguin-trap.exe`를 실행한다.

#### 2-2. Execute .py file

>  Python과 pip이 미리 설치되어 있어야 한다.

프로젝트 경로로 이동하고 python venv 모듈을 이용하여 `env`라는 이름의 가상환경을 생성한다.

```shell
cd penguin-trap-pygame
python -m venv env
```

가상환경을 활성화한다.

```shell
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

pip을 업그레이드하고 필요한 패키지를 설치한다.

```shell
pip install --upgrade pip
pip install -r requirements.txt
```

main.py 파일을 실행한다.

```shell
python ./main.py
```

## Usage

### Play the game

`penguin-trap.exe`나 `main.py`를 실행하면 게임이 시작된다.

cmd 화면을 통해 게임을 플레이하는 인원수를 입력한다. 0/1/2만 허용되며 올바르지 않은 값이면 재입력 받는다.

2인보다 적은 경우 AI가 남은 인원을 대체한다.

```shell
플레이어 수 입력(-1은 종료):
```

### Build .exe file

Window 환경 기준으로, pyinstaller 패키지를 이용해 `penguin-trap.exe` 파일을 생성한다.

이미지 파일이 담긴 `picture` 디렉토리와 `penguin-trap.exe`이 같은 경로 상에 위치해야 exe 파일이 정상 실행된다.

```shell
env\Scripts\pyinstaller --clean --distpath=. main.spec
```

## Technology Stack

### Python packages

* Python 3.8
* Pygame 2.1.2
* Pyinstaller 5.1 - py 파일을 exe 파일로 변환

### Design Tool

* Adobe Photoshop

## Contributors

* 송용수([Dr19-coder](https://github.com/Dr19-coder)): 물리엔진 고안
* 임정섭([jseop-lim](https://github.com/jseop-lim)): 기획 및 디자인, 코딩
