#!/bin/bash

# 1. Get current date
DATE=$(date '+%Y-%m-%d')
LOG_FILE="process_log_${DATE}.log"
HIGH_MEM_LOG="high_mem_processes.log"

# 2. Log Running Processes
echo "[✔] Logging running processes..."
tasklist > "$LOG_FILE"

# 3. Get total memory (in KB)
echo "[✔] Getting total memory..."
TOTAL_MEM_KB=$(powershell -Command "(Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory / 1KB" | awk '{printf "%.0f", $1}')

# 4. Check for high memory usage (>30%)
echo "[✔] Checking for high memory usage (>30%)..."
HIGH_MEM_COUNT=0
> "$HIGH_MEM_LOG"

tasklist /FO CSV | tail -n +2 | while IFS=, read -r image pid session_name session_num mem_usage
do
  mem_kb=$(echo "$mem_usage" | tr -d '"' | sed 's/ K//' | tr -d ',')

  if [[ "$mem_kb" =~ ^[0-9]+$ ]]; then
    percent=$((mem_kb * 100 / TOTAL_MEM_KB))
    if [ "$percent" -gt 30 ]; then
      echo "⚠️  HIGH MEMORY: $image (PID: $pid) using ${percent}% of memory"
      echo "$image,$pid,$mem_kb KB (${percent}%)" >> "$HIGH_MEM_LOG"
      HIGH_MEM_COUNT=$((HIGH_MEM_COUNT + 1))
    fi
  fi
done

# 5. Disk Usage (C: drive)
echo "[✔] Checking disk usage on C:..."
DISK_USAGE=$(powershell -Command "((Get-PSDrive C).Used / ((Get-PSDrive C).Used + (Get-PSDrive C).Free)) * 100" | awk '{printf "%.0f", $1}')
echo "Disk usage on C: is ${DISK_USAGE}%"

# 6. Summary
TOTAL_PROC=$(tasklist | grep -c ".exe")

echo ""
echo "========= SYSTEM SUMMARY ========="
echo "Total Running Processes : $TOTAL_PROC"
echo "Processes >30% Memory   : $HIGH_MEM_COUNT"
echo "Disk Usage on C:        : ${DISK_USAGE}%"
echo "=================================="
