import os

def run():
    print('All Vm\'s')
    os.system(f'VBoxManage list vms')
    print('\n\nRunning VM\'s')
    os.system('VBoxManage list runningvms')


