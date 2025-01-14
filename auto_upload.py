import os

# Git 명령어 실행 함수
def run_git_command(command):
    result = os.system(command)
    if result != 0:
        print(f"Command failed: {command}")
        exit(1)

# Git 작업 순서
print("Starting Git automation...")
run_git_command("git add .")  # 모든 변경 사항 추가
commit_message = input("Enter commit message: ")
run_git_command(f'git commit -m "{commit_message}"')  # 커밋
run_git_command("git push origin main")  # 변경 사항 푸시
print("All changes pushed to GitHub!")