import os

def run(machine_name):
    os.system(f'VBoxManage showvminfo {machine_name}')
