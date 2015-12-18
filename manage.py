# -*- Encoding: utf-8 -*-
from flask.ext.script import Manager
from flask.ext.migrate import MigrateCommand
from app import make_app

PORT = 8000  # debug mode

app = make_app('development')
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    """Run server."""
    app.run(host='0.0.0.0', port=PORT, debug=True)


if __name__ == "__main__":
    manager.run()
