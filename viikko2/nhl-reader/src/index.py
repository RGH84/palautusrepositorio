from rich.table import Table
from rich.console import Console
from rich import box
from rich.panel import Panel
from player_reader import PlayerReader
from player_stats import PlayerStats

console = Console()

def main():
    console.print(Panel("[bold cyan]NHL statistics by nationality[/bold cyan]", expand=False))
    console.print()

    seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]
    season = console.input(f"Select season [{'/'.join(seasons)}]: ")

    if season not in seasons:
        console.print("[bold red]Invalid season format. Please restart and select a valid season.[/bold red]")
        return

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    while True:
        nationalities = ["AUT", "CZE", "AUS", "SWE", "GER", "DEN", "SUI", "SVK", "NOR", "RUS", "CAN", "LAT", "BLR", "SLO", "USA", "FIN", "GBR"]
        console.print()
        nationality = console.input(f"[bold yellow]Select nationality[/bold yellow] [{'/'.join(nationalities)}/exit]: ")

        if nationality.lower() == "exit":
            console.print("[bold green]Exiting program. Thank you![/bold green]")
            break

        if nationality not in nationalities:
            console.print("[bold red]Invalid nationality. Please try again.[/bold red]")
            continue

        players = stats.top_scorers_by_nationality(nationality)
        if not players:
            console.print(f"[bold magenta]No players found for nationality: {nationality} in season {season}[/bold magenta]")
            continue

        table = Table(title=f"Top scorers of {nationality} season {season}", box=box.ROUNDED, style="cyan")
        table.add_column("Name", justify="left", style="bold white")
        table.add_column("Team", justify="center", style="bold green")
        table.add_column("Goals", justify="right", style="bold magenta")
        table.add_column("Assists", justify="right", style="bold magenta")
        table.add_column("Points", justify="right", style="bold yellow")

        for player in players:
            table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                str(player.points)
            )

        console.print(table)
        console.print()

if __name__ == "__main__":
    main()