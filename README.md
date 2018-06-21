# CMD Progress - Proof of Concept

This is a proof of concept showing a web service initiating a system call, then monitoring its progress.

## Test Command

There's a `command.py` test command that will run for 10 seconds and write out `progress.txt` with a percentage 
every second. This is what the current web service will call.

## Server

This uses bottle.py as a simple web framework. The `/` root will load the page with a few buttons, and then
supports 2 other views: to initiate a command, and to retrieve progress.

To run the server, use virtualenv/pip.

Setting up a new project:

    $ virtualenv --python=python3 .venv
    $ pip install -r requirements.txt

To run the client:

    $ . .venv/bin/activate   # Only needed the first time to configure your current shell
    $ python app.py

## Client

This uses jquery to send AJAX GET requests to the server, and controls a progress bar and a few buttons. It polls
twice a second, so that it's a little smoother, since the progress file will be written once a second.

## TODO

- Use JSON messages so more info is available
- Error handling (multiple web clients, don't allow starting commands if already running)
- All buttons do the same thing - use the `cmd` param to separate
- Make the bottle `reload` work (have to restart server after all changes)
