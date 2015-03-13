# aperto-anki command demo

This repository contains two programs written in Python.

- `receive-commands` connects to the relayr cloud via MQTT and subscribes on
a topic to receive commands for a hardcoded device id. It will run until you
hit Ctrl-C.

- `send-commands` connects to the relayr cloud via HTTP and sends 100 commands
to that hardcoded device id.

### Installation

It is advisable that you install the dependencies via `pip` and `virtualenv`.

```bash
[sudo] pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements
```

### OAuth access token

You will need to put the access token for the relayr cloud into an enviroment
variable `TOKEN`.

```bash
export TOKEN=<sometoken>
```
Please contact relayr if you don't know how to obtain your token.

### Running the programs

After the installation of the requirements simply open two terminals.

Run `./receive-commands` in one and `./send-commands` in the second.

