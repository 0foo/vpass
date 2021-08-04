import sys
from commands import help, launch, delete, list_em, status, stop, restart, start, suspend

# Empty condition for arguments(sys.argv always has script name as first item in the param list.)
if len(sys.argv) <= 1:
    help.run()
    exit()

command = sys.argv[1]
flag = None

if len(sys.argv) > 2:
    flag = sys.argv[2]

if command in ['-h', '--help', 'help']:
    help.run()
    exit()

command_list = {
    'launch': {
        'description': 'Create and start an Ubuntu instance',
        'exec': [
            'launch.run()',
            {'launch': launch}
        ]
    },
    'list': {
        'exec': [
            'list_em.run()',
            {'list_em': list_em}
        ]
    },
    'delete': {
        'description': 'test',
        'exec': [
            'delete.run(flag)',
            {'delete': delete, 'flag': flag}
        ]
    },
    'status': {
        'description': 'TBD',
        'exec': [
            'status.run(flag)',
            {'status': status, 'flag': flag}
        ]
    },
    'stop': [
        'stop.run(flag)',
        {'stop': stop, 'flag': flag}
    ],
    'restart': [
        'restart.run(flag)',
        {'restart': restart, 'flag': flag}
    ],
    'start': [
        'start.run(flag)',
        {'start': start, 'flag': flag}
    ],
    'suspend': [
        'suspend.run(flag)',
        {'suspend': suspend, 'flag': flag}
    ]
}

if command in command_list and 'flag' in command_list[command][1] and not flag:
    print("Please enter a machine name. Use the 'list' command to get a list of machines.")
    exit()

if command in command_list:
    exec(*command_list[command])
else:
    print("Command not found.")


