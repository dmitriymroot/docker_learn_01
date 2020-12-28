#!/bin/bash
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

find /mnt/data/logs -type f -iname "*.log" -exec awk '/Failed password for invalid/ {print $1,$2,$9,$11}' {} \; >> /mnt/data/out/outputlogs
find /mnt/data/logs -type f -iname "*.log" -exec awk '/Invalid user/ {print $1,$2,$6,$8}' {} \; >> /mnt/data/out/outputlogs
find /mnt/data/logs -type f -iname "*.log" -exec awk '!/[Ii]nvalid/ {print $1,$2,$7,$9}' {} \; >> /mnt/data/out/outputlogs
sed -i -e 's/+03:00 / /g' -e 's/T/ /g' /mnt/data/out/outputlogs
find /mnt/data/logs -type f -iname "*.log" -exec truncate -s 0 {} \;



