exit()
command_list = {
    'launch': {
        'description': 'Create and start an Ubuntu instance',
        'exec': [
            'launch.run(config)',
            {'launch': launch, 'config': config}
        ]
    },
    'list': {
        'description': 'List all available instances.',
        'exec': [
            'list_em.run(config)',
            {'list_em': list_em, 'config': config}
        ]
    },
    'delete': {
        'description': 'Delete an instance.',
        'exec': [
            'delete.run(flag, config)',
            {'delete': delete, 'flag': flag, 'config': config}
        ]
    },
    'status': {
        'description': 'Get the status of an instance.',
        'exec': [
            'status.run(flag, config)',
            {'status': status, 'flag': flag, 'config': config}
        ]
    },
    'stop': {
        'description': 'Stop instances',
        'exec': [
            'stop.run(flag, config)',
            {'stop': stop, 'flag': flag, 'config': config}
        ]
    },
    'restart': {
        'description': 'Restart instances',
        'exec':[
            'restart.run(flag, config)',
            {'restart': restart, 'flag': flag, 'config': config}
        ]
    },
    'start': {
        'description': 'Start instances',
        'exec': [
            'start.run(flag, config)',
            {'start': start, 'flag': flag, 'config': config}
        ]
    },
    'suspend': {
        'description': 'Suspend running instances',
        'exec': [
            'suspend.run(flag, config)',
            {'suspend': suspend, 'flag': flag, 'config': config}
        ]
    },
    'shell': {
        'description': 'Open a shell on a running instance.',
        'exec': [
            'shell.run(flag, config)',
            {'shell': shell, 'flag': flag, 'config': config}
        ]
    },
    'mount': {
        'description': 'Mount a local directory in the instance..',
        'exec': [
            'mount.run(flag, config)',
            {'mount': mount, 'flag': flag, 'config': config}
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

if flag is not None:
    if os.path.exists(the_machine_dir):
        os.chdir(the_machine_dir)

if command in command_list:
    exec(*command_list[command]['exec'])
else:
    print("Command not found.")


