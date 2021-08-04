def run(flag):
    import os
    if flag is not None:
        machine_name = flag
        val = input(f"This will permanantly delete the VM \"{flag}\" and all of it's associated files. Is this ok?(y/N):  ")
        if val == 'y':
            os.system(f"VBoxManage controlvm {machine_name} savestate")
            os.system(f'VBoxManage unregistervm {machine_name} --delete')