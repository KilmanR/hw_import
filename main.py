from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
from rich import print

if __name__ == '__main__':
    print(f"[bold cyan]{datetime.now()}[/bold cyan] Запуск [green]программы[/green]")
    calculate_salary()
    get_employees()
