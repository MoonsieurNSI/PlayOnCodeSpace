### 1. Update package list and install the missing venv tool (requires sudo)
```bash
sudo apt-get update
sudo apt-get install -y python3.11-venv
```

### 2. Now try creating the virtual environment again (this will work now)
```bash
python3 -m venv venv
```

### 3. Activate the environment
```bash
source venv/bin/activate
```

### 4. Install the Jupyter kernel into this new environment
```bash
pip install ipykernel
```
------------------

### 5. Press <kbd>SHIFT + ENTER</kbd> to run cells

------------------

### 6. Snippets

- Press <kbd>CTRL + SHIFT + P</kbd>.
- Type `Snippets` and select `Preferences: Configure User Snippets`.
- Type `markdown` and select `markdown.json`. Example:
    ```json
    "Blue Box": {
    "prefix": "box-blue",
    "body": [
        "<div class=\"alert alert-block alert-info\">",
        "<b>Note:</b> $1",
        "</div>"
    ],
    "description": "Insert a Blue Info Box"
    },
    "Green Box": {
    "prefix": "box-green",
    "body": [
        "<div class=\"alert alert-block alert-success\">",
        "<b>Success:</b> $1",
        "</div>"
    ],
    "description": "Insert a Green Success Box"
    }
    ```
-----------

### 7. Force pop-up menu

- Press <kbd>CTRL + SHIFT + P</kbd>.
- Type `Settings JSON` and select `"Preferences: Open User Settings (JSON)"`.
- Add the following lines:
    ```JSON
        "[markdown]": {
        "editor.quickSuggestions": {
        "comments": "on",
        "strings": "on",
        "other": "on"
        }
        }
    ```