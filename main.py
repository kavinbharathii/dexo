
# ------------------------------------------------------------------------------------------------------------------- #

import sys
import os
import rich

# ------------------------------------------------------------------------------------------------------------------- #

project_name = sys.argv[1]
rich.print(f"[blue]Creating[/blue]: [bold green]{project_name}[/bold green]")
os.chdir(os.getcwd())

try:
    os.mkdir(project_name)
except OSError:
    rich.print(f"[bold red]Error[/bold red]: [bold blue]Project {project_name} already exists[/bold blue]")
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
</body>
</html>
'''
    )
    html.close()

rich.print(f"[blue]Created[/blue]: [bold red]index.html[/bold red]")

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

rich.print(f"[blue]Created[/blue]: [bold blue]style.css[/bold blue]")

# ------------------------------------------------- create js file ------------------------------------------------- #
with open(f'{project_name}/app.js', 'w') as js:
    js.write(
f'''
console.log('{project_name.capitalize()} successfully!')
const dev = document.getElementById('dev')
'''
    )
    js.close()

rich.print(f"[blue]Created[/blue]: [bold yellow]app.js[/bold yellow]")

rich.print("[bold green]Completed...[/bold green]")
# ------------------------------------------------------------------------------------------------------------------- #
