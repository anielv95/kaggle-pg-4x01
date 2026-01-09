Steps to install python, pip and jupyterlab in the EC2 instance:

1. `sudo dnf install python3.12`
2. `sudo dnf install python3.12-pip`
3. `python3.12 -m pip install jupyterlab`


To run jupyter lab inside a container or in a EC2 instance:

```
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```
