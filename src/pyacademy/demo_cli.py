import time
from rich.console import Console
import questionary

console = Console()

console.print("Questionary est une lib qui permet de faciliter l'intération utilisateur.")
console.print("Pour commencer, questionary permet une simple saisie de texte")
value = questionary.text("Une question attendant un texte").ask()

console.print(f'Vous avez sais [red]{value}[/red]')
console.print("Ah oui… L'affichage est réalisé ici avec [bold]Rich[/bold] qui permet la mise en valeur du texte.")

console.print()
console.print("Pour la saisie spécifique d'entiers par exemple, la conversion se fait comme pour un input.")
try:
    value = int(questionary.text("Une question attendant un entier").ask())
    console.print(f'Vous avez sais [red]{value}[/red]')
except ValueError:
    console.print(f"Vous avez fait les malins à ne pas saisir un entier et évidemment, c'est géré par une exception.")

console.print()
console.print("La saisie de texte permet aussi de proposer une valeur par défaut")
value = questionary.text("À qui dire bonjour ?", default="World").ask()
console.print(f'Hello [red]{value}[/red]')

console.print()
console.print("Questionary permet aussi la saisie de mots de passe")
value = questionary.password("Quel est votre mot de passe fictif ?").ask()
console.print(f'Vous avez saisi : [red]{value}[/red]. Évidemment, un vrai mot de passe ne soit pas être affiché…')

console.print()
console.print("Questionary permet aussi de faire de la complétion lorsque vous devez préciser un chemin vers un fichier ou un répertoire")
console.print("Vous pouvez utiliser la touche tabulation pour déclencher la complétion.")
value = questionary.path("Chemin vers le fichier ?").ask()
console.print(f'Vous avez saisi : [red]{value}[/red]')

console.print()
console.print("Questionary propose aussi un choix parmi des options")
value = questionary.select("Vous préférez ?",
                           choices=["Python", 'Rust', 'PHP', 'Javascript']).ask()
console.print(f"Vous avez choisi [red]{value}[/red]")

console.print()
console.print("Mais vous avez aussi la possibilité de choisir plusieurs options.")
value = questionary.checkbox("Vous préférez ?",
                           choices=["Python", 'Rust', 'PHP', 'Javascript']).ask()
console.print(f"Vous avez choisi [red]{value}[/red]")

with console.status("[bold blue]Super, maintenant on compile vos saisies...[/bold blue]",
                    spinner="aesthetic") as status:
    time.sleep(2)
    status.update(f"[bold blue]Encore un petit instant…[/bold blue]")
    time.sleep(2)
    status.update(f"[bold red]Oho mais qu'avons nous là ?[/bold red]")
    time.sleep(2)
    status.update(f"[bold green]Ah non, c'est bon[/bold green]")
    time.sleep(2)


console.print("Voilà, c'était une dernière démo pour Rich.")

console.print()
value = questionary.confirm("Alors, c'est des libs cool, non ?").ask()
if value:
    console.print("Héhé, j'en étais sûr que ça vous plairait.")
else:
    console.print("Pfff… Restez sur les input alors…")
