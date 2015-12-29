#!/usr/bin/env python


import os
import time

def stop():
    file = open("/tmp/eap_bridge.pid","w+")
    
    for line in file:
        print "Killing PID: " + int(line);
        os.kill(int(line), signal.SIGTERM)

    file.write("");
    file.close();

def start():
    print "Starting"
    #os.system(" /root/hostap_modded/wpa_supplicant/eapol_test -c /root/hostap_modded/wpa_supplicant/peap.conf -a 192.168.1.1 -s password");
    pid = os.spawnv(os.P_NOWAIT,"/root/hostap_modded/wpa_supplicant/eapol_test",['/root/hostap_modded/wpa_supplicant/eapol_test', '-c', '/root/hostap_modded/wpa_supplicant/peap.conf', '-a', '192.168.1.1', '-s', 'password']);
    if pid:
        print "Saving PID" + pid
        file = open("/tmp/eap_bridge.pid", "a+");
        file.write(pid + "\n");

    file.close();

start();
