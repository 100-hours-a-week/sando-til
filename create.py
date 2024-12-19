import os
from datetime import datetime, timedelta

def create_daily_markdown_files(directory, start_date, end_date, template_path):
    # 템플릿 파일 내용 읽기
    if os.path.exists(template_path):
        with open(template_path, 'r', encoding='utf-8') as template_file:
            template_content = template_file.read()
    else:
        print(f"Template file not found: {template_path}")
        return

    # 지정된 기간 동안의 날짜를 생성
    current_date = start_date
    while current_date <= end_date:
        file_name = f"{current_date.strftime('%Y-%m-%d')}.md"
        file_path = os.path.join(directory, file_name)

        # 디렉토리가 존재하지 않으면 생성
        if not os.path.exists(directory):
            os.makedirs(directory)

        # 파일이 존재하지 않으면 생성
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as file:
                # 템플릿 내용에 날짜를 치환하여 작성
                file_content = template_content.replace("{{date}}", current_date.strftime('%Y-%m-%d'))
                file.write(file_content)
            print(f"Created: {file_path}")
        else:
            print(f"File already exists: {file_path}")

        # 다음 날짜로 이동
        current_date += timedelta(days=1)

# 예제 사용법
directory = "./december"
start_date = datetime(2024, 12, 1)  # 시작 날짜
end_date = datetime(2024, 12, 31)    # 종료 날짜
template_path = "./template/yyyy-mm-dd.md"  # 템플릿 파일 경로
create_daily_markdown_files(directory, start_date, end_date, template_path)