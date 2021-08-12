import os, argparse, shutil
import random_names
from pathlib import Path

# pars args
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("command", type=str, nargs='?')
parser.add_argument("machine", type=str, nargs='?')
parser.add_argument("flags", type=str, nargs='*')
args = parser.parse_args()

# arguments
command=args.command
machine_name=args.machine
flags=args.flags

# directories
home_dir = str(Path.home())
app_root_dir = str(Path.cwd())
vpass_home_dir = os.path.join(home_dir, 'vpass')
machines_dir = os.path.join(vpass_home_dir, 'machines')
vpass_config_file = os.path.join(vpass_home_dir, 'vpass_config.yaml')

def list():
    # All Virtualbox machines
    print("")
    print("All Virtual Box Machines")
    print("------")
    os.system('VBoxManage list vms')
    print("\n")
    print("All Virtual Box Running Machines")
    print("------")
    os.system('VBoxManage list runningvms')
    print("\n")
    # Vpass machines
    print("Vpass Managed Machines")
    print("------")
    dirs = os.listdir(machines_dir)
    for dir in dirs:
        if os.path.isdir(os.path.join(machines_dir, dir)):
            print(dir)
    print("\n")
    exit()


if not os.path.exists(vpass_home_dir):
    print(f"Creating {vpass_home_dir}")
    os.makedirs(vpass_home_dir)

if not os.path.exists(machines_dir):
    print(f"Creating {machines_dir}")
    os.makedirs(machines_dir)

if command == 'launch':
    if machine_name is None:
        new_machine_dir = os.path.join(machines_dir, random_names.run())
    else:
        new_machine_dir = os.path.join(machines_dir, machine_name)

    if not os.path.exists(new_machine_dir):
        print(f"Creating {new_machine_dir}")
        os.makedirs(new_machine_dir)
        os.chdir(new_machine_dir)
        os.system(f'VBoxManage setproperty machinefolder {new_machine_dir}')
        os.system(f'vagrant init ubuntu/hirsute64')
        os.system('vagrant up')
        os.system('VBoxManage setproperty machinefolder default')
    else:
        print("A very rare naming collision occurred. Please rerun the command.")
    exit()

if command == 'start':
    the_machine_dir = os.path.join(machines_dir, machine_name)
    if os.path.exists(the_machine_dir):
        os.chdir(the_machine_dir)
        os.system('vagrant up')
    else:
        os.system(f'VBoxManage startvm {machine_name} --type headless')
    exit()

if command == 'stop':
    the_machine_dir = os.path.join(machines_dir, machine_name)
    if os.path.exists(the_machine_dir):
        os.chdir(the_machine_dir)
        os.system('vagrant halt')
    else:
        os.system(f'VBoxManage controlvm {machine_name} savestate')
    exit()

if  command is None or command == 'list':
    list()

if command == 'destroy' or command == 'delete':
    the_machine_dir = os.path.join(machines_dir, machine_name)
    if os.path.exists(the_machine_dir):
        os.chdir(the_machine_dir)
        os.system(f'vagrant destroy -f')
        try:
            shutil.rmtree(the_machine_dir, ignore_errors=True)
        except OSError as e:
            print("Error: %s : %s" % (the_machine_dir, e.strerror))
    else:
        print(f"Can't find machine by the name of {machine_name}")
    exit()

if command == 'help':
    options = {

    }

    help_text = '''
    A very light wrapper around vagrant allowing control of VM\'s from anywhere on the command line.
    Simply replace the command vagrant with the command vpass and pass in a machine name, no need to manually navigate to the machines folder.
    The config files for each  machine are found at <home directory>/vpass/machines and can be changed after creation to customize the vm.
    Inspired by Ubuntu multipass.
    
    
    Usage: vpass <command> <machine> [options]
    
    Commands
    -------
    launch: launches a new instance
    list: lists all instances available with vpass
    destroy: destroys the instance
    
    Examples: 
    vpass launch 
    vpass list
    vpass ssh cocky-wozniak
    vpass suspend cocky-wozniak
    vpass up cocky-wozniak
    vpass destroy cocky-wozniak
    
    
    Any regular vagrant commands will work with vpass without the need to manually navigate to the machines directory.
    
    '''
    print(help_text)
    exit()



the_machine_dir = os.path.join(machines_dir, machine_name)
if os.path.exists(the_machine_dir):
    os.chdir(the_machine_dir)
    if len(flags) == 0:
        flags = ""
    print(f'vagrant {command} {flags}')
    print(machine_name)
    os.system(f'vagrant {command} {flags}')
else:
    print(f"Can't find machine by the name of {machine_name}")







