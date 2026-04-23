import re

def count_logs(logs: list[str]) -> dict[str,int]:
    logs_dict = {"INFO":0, "WARNING":0,"ERROR":0, "duplicates":0}
    seen_logs = set()
    pattern = re.compile(r"(ERROR|INFO|WARNING)")
    for log in logs:       
        match = pattern.search(log)
        if match:
            if log in seen_logs:
                logs_dict['duplicates'] += 1
            else:
                level = match.group(0)
                logs_dict[level] += 1
        seen_logs.add(log)    
            
    return logs_dict