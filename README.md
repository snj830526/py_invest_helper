# 사용방법
process_watcher.py 를 실행 하면 됩니다.<br>

>  프로젝트 root 폴더에 아래의 내용으로 config.json 파일을 생성 해 주세요<br>
> {<br>
  "access_key": "업비트 access_key",<br>
  "secret_key": "업비트 secret_key",<br>
  "site_url": "https://api.upbit.com",<br>
  "slack_bot_token": "메시지 수신용 봇 토큰",<br>
  "slack_user_token": "본인 슬랙 사용자 토큰",<br>
  "slack_name": "메시지 수신용 봇 토큰",<br>
  "slack_token": "슬랙 메시지 발송용 봇 토큰",<br>
  "slack_channel": "메시지 받을 슬랙 채널명",<br>
  "main_script_path": "main.py가 설치 된 전체 경로"<br>
}