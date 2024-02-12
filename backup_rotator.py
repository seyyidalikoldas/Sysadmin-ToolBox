import os
import time
import shutil
import tarfile
from datetime import datetime

# basic backup rotation script
def create_archive(source_dir, backup_dir):
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir, exist_ok=True)
        
    date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = f"backup_{date_str}.tar.gz"
    target_path = os.path.join(backup_dir, archive_name)
    
    print(f"[*] Compressing {source_dir} -> {target_path}")
    with tarfile.open(target_path, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
    return target_path

def cleanup_old_archives(backup_dir, retention_days=14):
    now = time.time()
    cutoff_seconds = retention_days * 86400
    
    if not os.path.exists(backup_dir):
        return
        
    for f in os.listdir(backup_dir):
        if not f.endswith(".tar.gz"):
            continue
        fp = os.path.join(backup_dir, f)
        if os.path.isfile(fp):
            file_age = now - os.path.getmtime(fp)
            if file_age > cutoff_seconds:
                print(f"[-] Removing expired backup: {f}")
                os.remove(fp)

if __name__ == "__main__":
    # example run
    print("Backup rotator ready.")
