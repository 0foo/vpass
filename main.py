import sys
from commands import help, launch, delete, list_em, status, stop, restart, start, suspend, shell, mount

# Empty condition for arguments(sys.argv always has script name as first item in the param list.)


flag = None

if len(sys.argv) > 2:
    flag = sys.argv[2]

command_list = {
    'launch': {
        'description': 'Create and start an Ubuntu instance',
        'exec': [
            'launch.run()',
            {'launch': launch}
        ]
    },
    'list': {
        'description': 'List all available instances.',
        'exec': [
            'list_em.run()',
            {'list_em': list_em}
        ]
    },
    'delete': {
        'description': 'Delete an instance.',
        'exec': [
            'delete.run(flag)',
            {'delete': delete, 'flag': flag}
        ]
    },
    'status': {
        'description': 'Get the status of an instance.',
        'exec': [
            'status.run(flag)',
            {'status': status, 'flag': flag}
        ]
    },
    'stop': {
        'description': 'Stop instances',
        'exec': [
            'stop.run(flag)',
            {'stop': stop, 'flag': flag}
        ]
    },
    'restart': {
        'description': 'Restart instances',
        'exec':[
            'restart.run(flag)',
            {'restart': restart, 'flag': flag}
        ]
    },
    'start': {
        'description': 'Start instances',
        'exec': [
            'start.run(flag)',
            {'start': start, 'flag': flag}
        ]
    },
    'suspend': {
        'description': 'Suspend running instances',
        'exec': [
            'suspend.run(flag)',
            {'suspend': suspend, 'flag': flag}
        ]
    },
    'shell': {
        'description': 'Open a shell on a running instance.',
        'exec': [
            'shell.run(flag)',
            {'shell': shell, 'flag': flag}
        ]
    },
    'mount': {
        'description': 'Mount a local directory in the instance..',
        'exec': [
            'mount.run(flag)',
            {'mount': mount, 'flag': flag}
        ]
    }
}

if len(sys.argv) <= 1 or sys.argv[1] in ['-h', '--help', 'help']:
    help.run(command_list)
    exit()

command = sys.argv[1]

if command in command_list and 'flag' in command_list[command]['exec'][1] and not flag:
    print("Please enter a machine name. Use the 'list' command to get a list of machines.")
    exit()

if command in command_list:
    exec(*command_list[command]['exec'])
else:
    print("Command not found.")


