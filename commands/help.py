
def run():
    options = {
        '-h, --help, help': 'Displays help on commandline.'
    }

    actions = {
        'delete': ,
        'list': 'List all available instances',
        'shell': 'Open a shell on a running instance',
        'start': 'Start instances',
        'stop': 'Stop running instances',
        'status': 'Get the status of an instance.',
        'suspend': 'Suspend running instances',
        'restart': 'Restart instances',
        'mount': 'Mount a local directory in the instance'
    }

    print ('Usage: vpass [options] <command>')
    print('Create, control and connect to Ubuntu instances.')

    print('Options')
    for key, value in options.items():
        print("\t" + key + '\t' + value)

    print('Available commands:')
    for key, value in actions.items():
        print("\t" + key + '\t\t' + value)