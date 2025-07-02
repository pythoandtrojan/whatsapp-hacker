import os
import sys
import time
from rich.console import Console
from rich.progress import Progress
from rich.panel import Panel

console = Console()

BANNER = """
[bold green]┌─────────────────────────────────────────────────────────┐
│ ███████╗██╗   ██╗██████╗ ███████╗██████╗ ██╗███████╗██████╗ │
│ ██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗██║██╔════╝██╔══██╗│
│ █████╗  ██║   ██║██████╔╝█████╗  ██████╔╝██║█████╗  ██║  ██║│
│ ██╔══╝  ██║   ██║██╔══██╗██╔══╝  ██╔══██╗██║██╔══╝  ██║  ██║│
│ ██║     ╚██████╔╝██║  ██║███████╗██║  ██║██║███████╗██████╔╝│
│ ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚═════╝ │
├─────────────────────────────────────────────────────────┤
│[white] WhatsApp Hacker Pro - Instalador de Dependências v1.0[/white] │
│[white]         (Para uso exclusivo no Termux)[/white]                │
└─────────────────────────────────────────────────────────┘[/bold green]
"""

def run_command(command, description):

    try:
        with console.status(f"[cyan]{description}..."):
            result = os.system(command)
            if result != 0:
                console.print(f"[red]Erro ao executar: {command}[/red]")
                return False
        return True
    except Exception as e:
        console.print(f"[red]Erro: {str(e)}[/red]")
        return False

def install_dependencies():

    console.print(BANNER)
    console.print("\n[bold]Iniciando instalação de dependências...[/bold]\n")
    
    steps = [
        ("pkg update -y && pkg upgrade -y", "Atualizando pacotes"),
        ("pkg install -y python", "Instalando Python"),
        ("pkg install -y git", "Instalando Git"),
        ("pkg install -y openssl", "Instalando OpenSSL"),
        ("pkg install -y clang", "Instalando Clang"),
        ("pkg install -y libffi", "Instalando libffi"),
        ("pip install --upgrade pip", "Atualizando pip"),
        ("pip install rich pycryptodome", "Instalando bibliotecas Python"),
        ("termux-setup-storage", "Configurando armazenamento")
    ]
    
    with Progress() as progress:
        task = progress.add_task("[cyan]Instalando...", total=len(steps))
        
        for cmd, desc in steps:
            progress.update(task, description=f"[cyan]{desc}...")
            if not run_command(cmd, desc):
                console.print(f"[red]Falha na etapa: {desc}[/red]")
                return False
            progress.advance(task)
            time.sleep(1)
    
    return True

def verify_installation():
    """Verifica se a instalação foi bem-sucedida"""
    console.print("\n[bold green]✓ Verificando instalação...[/bold green]")
    
    checks = [
        ("python --version", "Python"),
        ("pip --version", "Pip"),
        ("openssl version", "OpenSSL")
    ]
    
    all_ok = True
    for cmd, name in checks:
        try:
            result = os.popen(cmd).read().strip()
            if not result:
                console.print(f"[red]✗ {name} não está instalado[/red]")
                all_ok = False
            else:
                console.print(f"[green]✓ {name}: {result.split()[0]}[/green]")
        except:
            console.print(f"[red]✗ Falha ao verificar {name}[/red]")
            all_ok = False
    
    return all_ok

def main():
    if not install_dependencies():
        console.print("\n[bold red]✗ Instalação falhou! Verifique os erros acima.[/bold red]")
        sys.exit(1)
    
    if verify_installation():
        console.print("\n[bold green]✓ Todas dependências instaladas com sucesso![/bold green]")
        console.print("\n[bold]Execute o script principal com:[/bold]")
        console.print("[cyan]python whatsapp_hacker.py[/cyan]\n")
    else:
        console.print("\n[bold yellow]! Algumas dependências podem não ter sido instaladas corretamente[/bold yellow]")
        console.print("[yellow]Tente executar manualmente os comandos que falharam[/yellow]")

if __name__ == "__main__":
   
    if not os.path.exists("/data/data/com.termux/files/usr/bin"):
        console.print("[red]Erro: Este script deve ser executado no Termux![/red]")
        sys.exit(1)
    
    main()
