'''
ToDo: Add retry to delete function. At the moment sometimes it will not work the first time.

'''

import shutil
import os


def run(flag, config):



    if flag is not None:
        machine_name = flag
        val = input(f"This will permanantly delete the VM \"{flag}\" and all of it's associated files. Is this ok?(y/N):  ")
        if val == 'y':
            os.system(f"VBoxManage controlvm {machine_name} savestate")
            os.system(f'VBoxManage unregistervm {machine_name} --delete')
            machine_dir_total = os.path.join(config["machines_dir"], machine_name)
            shutil.rmtree(machine_dir_total)
