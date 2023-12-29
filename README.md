# triple_news

## Description
Here is a brief list of the functional features of the triple_news project:
- The project's main page displays the 10 latest news posts. The main page is available to all users. News is displayed in a curtailed form (only the first 15 words are visible).
- Each piece of news has its own page with the full text; user comments are also displayed there.
- Any user can independently register on the website.
- A logged in (authorized) user can leave, edit, and delete their own comments.
- If there are comments to a news post, the number of comments is displayed on the main page under the post.
- The project code contains a list of forbidden words that cannot be used in comments, such as "rascal" and "scoundrel."


To load prepared news after applying migrations, execute this command:
```bash
python manage.py loaddata news.json
```


## How to Work With the Repository
To begin your task, copy your repository URL and clone it.
  
### Create a virtual environment

1. Open Visual Studio Code, go to "File" / "Open Folder," and open *Dev/triple_news/*. 
2. Launch the terminal in VS Code and make sure you work from the *triple_news/* directory. If you use Windows, make sure Git Bash runs in the terminal, and not through PowerShell or anything else. Run this command:
- Linux/macOS
    
    ```bash
    python3 -m venv venv
    ```
    
- Windows
    
    ```python
    python -m venv venv
    ```
   
The virtual environment will be created in the *triple_news/* directory. The `venv` folder will appear there too and will store all the project dependencies.


### Activating the virtual environment
in the console, go to the root directory of the project *Dev/triple_news/* and run this command:
- Linux/macOS
    
    ```bash
    source venv/bin/activate
    ```
    
- Windows
    
    ```bash
    source venv/Scripts/activate
    ```
    

All commands in the terminal will now be preceded by the `(venv)` string.

💡 All the following console commands must be run with the working virtual environment.

Refresh pip:

```bash
python -m pip install --upgrade pip
```

### Install the dependencies from the *requirements.txt*:
Run the following command while you are in the *Dev/triple_news/* folder:

```bash
pip install -r requirements.txt
```

### Using migrations

    
In the directory with the manage.py file, run the command:

```bash
python manage.py migrate
```

### Running the project in dev mode

    
In the directory with the manage.py file, run the command:

```bash
python manage.py runserver
```

In response to the command, Django will report that the server is running and the project is available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
