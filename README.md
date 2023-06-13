# 자동화 기술 블로그

## Link
  https://1yoouoo.github.io/

## ChatGPT4 + Stackoverflow + python + jekyll

## 로직
1. cron를 이용해서 하루에 2번 스크립트 실행
2. 파이썬 파일 실행
  - StackAPI를 이용해서 실시간 조회수 높은 글 크롤링
  - openAI API로 md형식으로 글 생성 후 저장
3. 파이썬 파일 종료 후 git commit && push 실행
4. push 트리거로 github Actions 실행
5. 테스트 후 gh-page 배포



