from rich import print as rprint
from datetime import datetime
import traceback

def error(*body):
    print("\033[0;31;40m│\033[0m",end="")
    msg = ""
    flag = False
    for i in body:
        if "Error" not in str(type(i)): 
            msg += str(i) + " "
        else: flag = True
    rprint("[[bold green]" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "[/bold green]] [bold red]SccER[/bold red] [[bold red]error[/bold red]] > [bold yellow]" + msg + "[/bold yellow]")
    if flag: traceback.print_exc()

def success(*body):
    print("\033[0;31;40m│\033[0m",end="")
    msg = ""
    for i in body:
        msg += str(i) + " "
    rprint("[[bold green]" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "[/bold green]] [bold red]SccER[/bold red] [[bold green]success[/bold green]] > " + msg)

def info(*body, ):
    print("\033[0;31;40m│\033[0m",end="")
    msg = ""
    for i in body:
        msg += str(i) + " "    
    rprint("[[bold green]" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "[/bold green]] [bold red]SccER[/bold red] [[bold blue]info[/bold blue]] > " + msg)

def banner(*body):
    rprint("[bold yellow]  ________  ________  ________  _______   ________      [/bold yellow]")
    rprint("[bold yellow] |\   ____\|\   ____\|\   ____\|\  ___ \ |\   __  \     [/bold yellow]")
    rprint("[bold yellow] \ \  \___|\ \  \___|\ \  \___|\ \   __/|\ \  \|\  \    [/bold yellow]")
    rprint("[bold yellow]  \ \_____  \ \  \    \ \  \    \ \  \_|/_\ \   _  _\   [/bold yellow]")
    rprint("[bold yellow]   \|____|\  \ \  \____\ \  \____\ \  \_|\ \ \  \\  \|  [/bold yellow]")
    rprint("[bold yellow]     ____\_\  \ \_______\ \_______\ \_______\ \__\\ _\  [/bold yellow]")
    rprint("[bold yellow]    |\_________\|_______|\|_______|\|_______|\|__|\|__| [/bold yellow]")
    rprint("[bold yellow]    \|_________|                                        [/bold yellow]")
    rprint("[bold yellow]                                                        [/bold yellow]")
    rprint("[bold yellow]                                       joe1sn           [/bold yellow]")