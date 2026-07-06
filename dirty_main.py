from application.salary import *
from application.db.people import *
from datetime import datetime
from rich import print

if __name__ == '__main__':
    print(f"[bold cyan]{datetime.now()}[/bold cyan] Запуск [green]dirty_main[/green]")
    calculate_salary()
    get_employees()
