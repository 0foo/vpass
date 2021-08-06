import os
def run(machine_name):
    os.system(f'VBoxManage startvm {machine_name} --type headless')
