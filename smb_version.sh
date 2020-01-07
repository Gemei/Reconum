#!/bin/sh
#Author: rewardone
#Modified: varlynx
#Description:
# Requires root or enough permissions to use tcpdump
# Will listen for the first 7 packets of a null login
# and grab the SMB Version
#Notes:
# Will sometimes not capture or will print multiple
# lines. May need to run a second time for success.
if [ -z $1 ]; then echo "Usage: ./smbver.sh RHOST {RPORT} {OS Windows/Unix} " && exit; else rhost=$1; fi
if [ ! -z $2 ]; then rport=$2; else rport=139; fi
if [ ! -z $3 ]; then ros=$3; else ros="Unix"; fi
if [ $ros = "Unix" ]; then match1='samba'; match2='UnixSamba.*[0-9a-z]'; echo "Unix"; else match1='Windows'; match2='Windows.*[0-9a-z]'; echo "Windows"; fi
sudo tcpdump -s0 -n -i tap0 src $rhost and port $rport -A -c 7 2>/dev/null | grep -i $match1 | tr -d '.' | grep -oP $match2 | uniq | tr -d '\n' & echo -n "$rhost: " & echo "exit" | python ~/Tools/impacket/examples/smbclient.py $rhost -p $rport 1>/dev/null 2>/dev/null
sleep 1.5 && echo ""