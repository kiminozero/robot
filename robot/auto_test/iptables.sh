#!/bin/bash

IPTABLES=/sbin/iptables
echo "1" > /proc/sys/net/ipv4/ip_forward

$IPTABLES -t nat -F POSTROUTING
$IPTABLES -t nat -F PREROUTING
$IPTABLES -t nat -F OUTPUT
$IPTABLES -F
$IPTABLES -X
$IPTABLES -P INPUT ACCEPT
$IPTABLES -P OUTPUT ACCEPT
$IPTABLES -P FORWARD ACCEPT
$IPTABLES -A INPUT -p icmp --icmp-type timestamp-request -j DROP
$IPTABLES -A INPUT -p icmp --icmp-type timestamp-reply -j DROP
$IPTABLES -A INPUT -p icmp -j ACCEPT
$IPTABLES -A INPUT -i lo -p all -j ACCEPT
$IPTABLES -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
$IPTABLES -A INPUT -p tcp --dport 22 -j ACCEPT
$IPTABLES -A INPUT -p tcp --dport 80 -j ACCEPT
$IPTABLES -A FORWARD -p TCP ! --syn -m state --state NEW -j DROP
$IPTABLES -A FORWARD -f -m limit --limit 100/s --limit-burst 100 -j ACCEPT

$IPTABLES -A FORWARD -p tcp --destination-port 3000 -j ACCEPT 
$IPTABLES -t nat -A PREROUTING -j REDIRECT -p tcp --destination-port 3000 --to-ports 80

/etc/rc.d/init.d/iptables save
/etc/rc.d/init.d/iptables restart

