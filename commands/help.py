
def run(actions):
    options = {
        '-h, --help, help': 'Displays help on commandline.'
    }


    print ('Usage: vpass [options] <command>')
    print('Create, control and connect to Ubuntu instances.')

    print('Options')
    for key, value in options.items():
        print("\t" + key + '\t' + value)

    print('Available commands:')
    for key, value in actions.items():
        print("\t" + key + '\t\t' + value['description'])