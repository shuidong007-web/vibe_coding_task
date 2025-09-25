import datetime
import subprocess

def get_staged_files():
    """获取暂存区的文件列表"""
    try:
        result = subprocess.run(
            ['git', 'diff', '--staged', '--name-status'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip().split('\n')
    except subprocess.CalledProcessError:
        return []

def update_dev_log(staged_files):
    """更新研发日志"""
    if not staged_files or (len(staged_files) == 1 and staged_files[0] == ''):
        return

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    prd_updated = False
    code_updates = []

    for file_status in staged_files:
        if not file_status:
            continue
        parts = file_status.split(None, 1)
        if len(parts) == 2:
            status, file_path = parts
        else:
            # Handle cases where status might not be present or format is unexpected
            status = '?' # Unknown status
            file_path = file_status.strip()
            print(f"⚠️ 警告：无法解析文件状态行: {file_status}")
            continue # Skip this entry
        if 'prd.md' in file_path:
            prd_updated = True
        # Exclude the log file itself from the list of code updates
        if 'dev_log.md' not in file_path:
            code_updates.append(f"- `{status}`: {file_path}")

    if not code_updates and not prd_updated:
        return

    log_entry = f"\n### {now}\n"
    
    log_entry += "#### PRD 更新记录\n"
    if prd_updated:
        log_entry += "- `prd.md` 已更新。\n"
    else:
        log_entry += "- 本次无 PRD 更新。\n"
        
    log_entry += "\n#### 代码更新记录\n"
    if code_updates:
        log_entry += "\n".join(code_updates) + "\n"
    else:
        log_entry += "- 本次无代码更新。\n"

    log_entry += "\n#### 调试版本记录\n"
    log_entry += "- (请在此处手动填写版本信息)\n"
    log_entry += "\n---"

    with open('dev_log.md', 'a', encoding='utf-8') as f:
        f.write(log_entry)
    
    # Add the updated log file to the staging area
    subprocess.run(['git', 'add', 'dev_log.md'])

if __name__ == "__main__":
    files = get_staged_files()
    update_dev_log(files)