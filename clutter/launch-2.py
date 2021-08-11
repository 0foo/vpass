from lib import random_names
import os
import random
import yaml


def run(config):

    # Create a random machine name, ssh port
    machine_name = 'vpass-' + random_names.run()
    port_number = random.randrange(9000, 65535)

    # parameters
    vm_to_clone = config['machine_config']["base_vm_name"]
    basefolder=config["machines_dir"]


    commands = [
        f'VBoxManage clonevm {vm_to_clone} --name={machine_name} --basefolder={basefolder}  --register ',
        f'VBoxManage modifyvm {machine_name} --natpf1 "ssh,tcp,,{port_number},,22"'
    ]

    print(f"Creating {machine_name}")

    for command in commands:
        print(command)
        cmd_out = os.system(command)
        if cmd_out != 0:
            exit()

    # create config file
    config['machine_config']['ssh_port'] =  port_number

    new_machine_dir = os.path.join(basefolder, machine_name)
    new_machine_config_file = os.path.join(new_machine_dir, "vpass_config.yaml")
    with open(new_machine_config_file, 'w') as file:
        yaml.dump(config, file)

    # start machine
    os.system(f'VBoxManage startvm {machine_name} --type headless')
    print(f"{machine_name} created and started.")
