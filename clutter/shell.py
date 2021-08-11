import os, yaml

def run(machine_name, config):
    config_file = os.path.join(config["machines_dir"], machine_name, "vpass_config.yaml")
    with open(config_file, 'r') as stream:
        try:
            config_file = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    print(config_file)
    ssh_port = config_file['ssh_port']
    os.system(f'ssh -p {ssh_port} ubuntu@localhost')