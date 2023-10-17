#!/bin/sh

logger "$0 - locking screen after sleep."
xautolock -locknow &> /dev/null
sleep 3 
systemctl suspend
