# 개발 시 주의사항
CATLAS 백엔드 개발 시 유의해야 할 사항을 정리하는 문서입니다. 개발의 편의성을 위해 최소한의 규칙을 정해놓는 것이니 가능한 한 지켜주시기 부탁드립니다.

## 1. 작업은 이슈 기반으로!
현재 저장소의 작업 흐름을 브랜치 별로 정리하자면 다음과 같습니다:
|종류|설명|
|:---:|:---:|
|`main`|외부인에게 공식적으로 제공되는 **안정적인** 브랜치|
|`dev`|기본적으로 작업이 진행되는 **뿌리** 브랜치|

작업해야하는 사항이 생기면 그에 대한 이슈를 생성한 후, `이슈태그#이슈번호`의 형태를 가진 이름의 브랜치를 생성하여 작업합니다. 해당 브랜치가 문제없음이 확인되면 `dev` 브랜치에 합쳐집니다.

## 2. Python `venv` 사용!
모두가 동등한 개발환경에서 작업할 수 있게 하기 위해, 가상환경 패키지 중 하나인 `venv` 기능을 사용합니다. 특정한 Python 패키지가 없다는 등의 환경 문제가 있다면 가상환경 밖에서 작업하고 있지는 않은지 확인 바랍니다. 추후에 가상환경을 설정할 때 필요한 `requirements.txt`를 작업하도록 하겠습니다.

`Windows`에서 작업하고 계신 분들 중 가상환경에 들어갈 수 없는 분들은 [링크](https://hatchling13.github.io/windows-powershell-execution-policy/)를 참조하시기 바랍니다.

### 환경 세팅 방법
```
아래 방법은 Windows 기준입니다:

git clone https://github.com/GNU-CS/catlas-backend  # GitHub에서 저장소 clone해오기
cd catlas-backend                                   # 저장소로 들어가기
python3 -m venv env                                 # 가상환경 만들기
./env/Scripts/activate                              # 가상환경 진입하기
pip install -r requirements.txt                     # 의존성 설치하기
git switch dev                                      # git branch 변경하기
```

---

*나머지 필요한 사항은 추후 작업됩니다.*