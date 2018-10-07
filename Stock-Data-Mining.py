import os
from flask_script import Manager, Server
from webapp import create_app
from webapp.models import db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
manager.add_command("server", Server())

@manager.shell
def make_shell_context():
    return dict(app=app, db=db)

if __name__ == "__main__":
    manager.run()
