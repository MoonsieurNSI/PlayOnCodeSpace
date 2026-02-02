# PlayOnCodeSpace

> [!TIP]
> On s'amuse ici sur une VM Linux Debian mais <br>
>   >**The GitHub Codespaces infrastructure (which runs on Azure) block the ICMP protocol (the specific type of network packets that `ping` uses). They do this to prevent people from using their servers to launch DDoS attacks or scan networks.**<br>
>
> donc on oublie `ping`, `traceroute`...<br>
> mais `curl` rules the world ! 

-----------------

> [!WARNING]
> On installe un *environnement virtuel pour python* pour run les ipynb !
>   ```bash
>   sudo apt-get update
>   sudo apt-get install -y python3.11-venv
>   source venv/bin/activate
>   pip install ipykernel

---------------------

> [!WARNING]
> On peut préparer le mardown pour [jupyter](./boulot/term/ipynb/tuto.md)

# Idéallement on lance le VE

## Enregistrer session psql
sudo -i -u postgres psql -a -L /tmp/session.log