

# ------------------------------------------------------------------------------------------------------------------- #

import sys
import os
from rich import print

def print_help():
    print("[bold cyan]DEXO[/bold cyan]")
    print()
    print("[bold]USAGE[/bold]:")
    print("To create a new project, ")
    print("> dexo { project_name }")
    print()
    print("Visit: [link=https://github.com/kavinbharathii/webdev]github[/link] for more info!")
    print()

# ------------------------------------------------------------------------------------------------------------------- #

def main():
        
    try:
        project_name = sys.argv[1]
        os.chdir(os.getcwd())
    except:
        print_help()
        exit()

    if project_name == "-h" or project_name == "--help":
        print_help()
        exit()

    try:
        os.mkdir(project_name)
        print(f"Project: [bold blue]{project_name}[/bold blue]")
        print()
    except OSError:
        print(f"[bold red]Error[/bold red]: Project [bold blue]{project_name}[/bold blue] already exists")
        exit()

    # ------------------------------------------------- create html file ------------------------------------------------- #
    with open(f'{project_name}/index.html', 'w') as html:
        html.write(
            f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>{project_name.capitalize()}</title>
</head>
<body>
    <div id="dev">
        <h1>{project_name.capitalize()} created successfully!</h1>
    </div>

    <script src="app.js"></script>
</body>
</html>
    '''
        )
        html.close()

    print("> [red]index.html[/red]")

    # ------------------------------------------------- create css file ------------------------------------------------- #
    with open(f'{project_name}/style.css', 'w') as css:
        css.write(
    '''
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: monospace, sans-serif;
}

:root {
    --bg-color : #121212;
    --fg-color: #9B37FF;
}

body,
main {
    background-color: var(--bg-color);
    color: var(--fg-color);
}

#dev {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100vw;
    height: 100vh;
}

    '''
        )
        css.close()

    print("> [cyan]style.css[/cyan]")

    # ------------------------------------------------- create js file ------------------------------------------------- #
    with open(f'{project_name}/app.js', 'w') as js:
        js.write(
    f'''
console.log('{project_name.capitalize()} successfully!')
const dev = document.getElementById('dev')
    '''
        )
        js.close()

    print(f"> [yellow]app.js[/yellow]")


    # ------------------------------------------------- create README file ------------------------------------------------- #
    with open(f'{project_name}/README.md', 'w') as readme:
        readme.write(
    f'''
###{project_name.capitalize()}

<!-- {project_name} README -->
Author: 
Version: 1.0.0
Description: {project_name}
    '''
        )
        readme.close()

    print(f"> [white]readme.md[/white]")

    print()
    print(f"[bold blue]{project_name}[/bold blue] created successfully")
    # ------------------------------------------------------------------------------------------------------------------- #
