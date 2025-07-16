# sysadmin-toolbox

A small collection of maintenance, backup, and log monitoring scripts I use across internal Linux servers and office infrastructure.

### contents:
- `auth_log_watcher.py`: parses `/var/log/auth.log` or secure logs to aggregate repeated failed SSH/login attempts by IP.
- `backup_rotator.py`: creates timestamped tar archives and purges backups older than N days.
- `inactive_users.py`: audits user access logs to identify stale or unused accounts for de-provisioning.
- `check_disk.sh`: bash script to alert when root filesystem usage crosses threshold.

### run test:
```bash
python run.py
```
