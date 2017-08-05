#!/usr/bin/env python
import os
from app import create_app, db, assets
from app.models import *
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask_assets import ManageAssets

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User,
                Teacher=Teacher, School=School,
                Ad=Ad, Subject=Subject)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("assets", ManageAssets(assets))
manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manager.run()



