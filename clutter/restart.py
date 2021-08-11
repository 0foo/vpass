import os

def run(machine_name):
    os.system(f'VBoxManage controlvm {machine_name} restart')
