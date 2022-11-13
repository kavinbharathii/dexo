

import sys
import os

project_name = sys.argv[1]
print(f"Creating {project_name}...")
os.chdir(os.getcwd())

try:
    os.mkdir(project_name)
except OSError:
    print(f"Project: {project_name} already exists")
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
    <title>{project_name}</title>
</head>
<body>
    <div id="dev">
        <h1>{project_name} created successfully!</h1>
    </div>
</body>
</html>
'''
    )
    html.close()

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

# ------------------------------------------------- create js file ------------------------------------------------- #
with open(f'{project_name}/app.js', 'w') as js:
    js.write(
f'''
console.log('{project_name} successfully!')
'''
    )
    js.close()


print(f"Completed {project_name}")
