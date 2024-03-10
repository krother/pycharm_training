
# Notizen aus dem PyCharm-Tutorial

## Übergeordnetet Links

Die meisten der verlinkten Seiten liegen auf:

* [http://www.academis.eu](http://www.academis.eu)
* [https://python-basics-tutorial.readthedocs.io/de/latest/](https://python-basics-tutorial.readthedocs.io/de/latest/)
* [https://www.python4data.science/de/latest/](https://www.python4data.science/de/latest/)


## Ein neues Projekt in PyCharm anlegen

* Projekt meist nützlicher als standalone Skript
* erkennbar am `.idea`-Ordner
* `.idea` kann ins `.gitignore` muß aber nicht

## Virtuelle Umgebungen

* Empfehlung: eine Environment pro Projekt, außer es ist eine "Spielwiese"
* [virtual envs mit conda](http://www.academis.eu/advanced_python/getting_started/virtualenv.html)
* eventuell muß der Pfad zu `conda.exe` (`Scripts\`) zur Umgebungsvariable `PATH` hinzugefügt werden

## Pakete installieren

* Installieren von mehreren Paketen aus dem Terminal: `pip -r requirements.txt`
* aus PyCharm mit `Tools-> Sync Requirements`
* Pakete werden nach `lib/site-packages` installiert
* pip installiert Pakete von [pypi.org](http://pypi.org/)
* statt `requirements.txt` wird neuerdings auch oft `pyproject.toml` verwendet
* siehe auch [Dependencies in PyCharm verwalten](https://www.jetbrains.com/help/pycharm/managing-dependencies.html)

## Terminal aktivieren

In der Powershell lässt sich conda aktivieren mit:

    set-executionpolicy unrestricted
    conda init powershell

siehe auch [conda in Powershell aktivieren](https://saturncloud.io/blog/activating-conda-environment-from-powershell-a-guide-for-data-scientists/)

## Importpfade

* in PyCharm beeinflusst `Mark as -> Source root` den import-Pfad
* auch die Umgebungsvariable `PYTHONPATH` enthält Verzeichnisse zum Importieren
* Um Verwirrung beim Import zu vermeiden sollten alle Pakete und Module unterschiedliche Namen haben

## Dateipfade

Beim Importieren aus mehreren Verzeichnisen musst Du für die meisten Dateien **absolute Pfade** verwenden. Folgender Zweizeiler hilft dabei:

    # ermittelt das Verzeichnis der aktuellen Datei
    BASE_PATH = os.path.split(__file__)[0]
    MY_CSV = os.path.join(BASE_PATH, "hello.csv")


## Versionskontrolle

* [Code verwalten mit Git](https://www.python4data.science/de/latest/productive/git/index.html)
* [Git Introduction](https://realpython.com/python-git-github-intro/)
* [Pro Git - Buch von Scott Chacon](https://git-scm.com/book/en/v2)

## Debugging

* [Kristians Debugging-Tutorial - Video](https://www.youtube.com/watch?v=04paHt9xG9U)
* [Kristians Debugging-Tutorial - Code](https://github.com/krother/debugging_tutorial)
* [Arten von Bugs und Debugging Techniken](http://www.academis.eu/advanced_python/error_handling/debugging.html)

## Automatische Tests

* [Kristians pytest Tutorial](http://www.academis.eu/python_testing/)
* [pytest im Python Basics Tutorial](https://python-basics-tutorial.readthedocs.io/de/latest/test/pytest/index.html)
* [pytest Doku](https://docs.pytest.org/en/latest/index.html)
- [Continuous Integration](http://www.academis.eu/advanced_python/error_handling/logging.html)

## Tools zur Codepflege

* [black](https://github.com/psf/black)
* [flake8](https://flake8.pycqa.org/en/latest/)
* [mypy](https://mypy-lang.org/)
* [pydantic](https://docs.pydantic.dev/latest/)
* [Logging](http://www.academis.eu/advanced_python/error_handling/logging.html)

## Refactoring

* [Kristians Refactoring-Tutorial - Video](https://www.youtube.com/watch?v=13hVzP3Oofs)
* [Kristians Refactoring-Tutorial - Code](hhttps://github.com/krother/refactoring_tutorial)
* [Liste von Refactorings auf sourcemaking.com](https://sourcemaking.com/refactoring)

## Python Kommandozeilenparameter

* Kommandozeilenaufrufe folgen dem Muster **PYTHON INTERPRETER_OPTS SCRIPT SCRIPT_PARAMETERS**
* jeder Teil lässt sich in den Build Configurations angeben
* Beispiel: `python -m cProfile hello.py Ada`
* Beispiel: `python -m pytest test_twenty_questions.py`


## Performance

* Standardaufruf cProfile: `python -m cProfile -s cumtime hello.py`
* im IPython Terminal auch `%time` und `%timeit`
* [snakeviz](https://jiffyclub.github.io/snakeviz/)
* [weitere Performance Werkzeuge](https://www.python4data.science/de/latest/performance/)


## Nützliche Python-Bibliotheken:

- [Malen mit Numpy](http://www.academis.eu/numpy_graphics/)


## Lizenz

(c) 2024 Dr. Kristian Rother

Diese Linkliste ist unter der Creative Commons Lizenz verfügbar (CC-BY-4.0).
Sie darf beliebig kopiert und verbreitet werden.

(die meisten der verlinkten Seiten übrigens auch)

**Viel Spaß!**
