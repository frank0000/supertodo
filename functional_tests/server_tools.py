from os import path
import subprocess
THIS_FOLDER = path.abspath(path.dirname(__file__))

def reset_database(host):
    subprocess.check_call(
        ['/usr/local/bin/fab', 'reset_database', '--host={}'.format(host), '--user=ubuntu', '-i', '/Users/fcharron/.ssh/aws_fcharron.pem'],
        cwd=THIS_FOLDER
    )


def create_session_on_server(host, email):
    return subprocess.check_output(
        [
            '/usr/local/bin/fab',
            'create_session_on_server:email={}'.format(email),
            '--host={}'.format(host),
            '--hide=everything,status',
            '--user=ubuntu', 
            '-i', 
            '/Users/fcharron/.ssh/aws_fcharron.pem'
        ],
        cwd=THIS_FOLDER
    ).decode().strip()
