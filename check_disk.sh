#!/usr/bin/env bash
# simple cron script to check root partition usage and notify

THRESHOLD=85
CURRENT=$(df / | grep / | awk '{ print $5}' | sed 's/%//g')

if [ "$CURRENT" -gt "$THRESHOLD" ]; then
    echo "[CRITICAL] Disk space alert on $(hostname): Root filesystem is at ${CURRENT}%"
    # TODO: integrate with slack/discord webhook
fi
