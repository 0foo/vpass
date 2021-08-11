from pathlib import Path
import os
import yaml
from shutil import copyfile


class Init:

    def __init__(self):

        # directories
        self.home_dir = str(Path.home())
        self.app_root_dir = str(Path.cwd().parents[0])
        self.vpass_home_dir = os.path.join(self.home_dir, 'vpass')
        self.machines_dir = os.path.join(self.vpass_home_dir, 'machines')
        self.base_vms_dir = os.path.join(self.vpass_home_dir, 'base_vms')

        # default template file
        self.app_root_template_file = os.path.join(self.app_root_dir, 'default_template.yaml')
        self.default_template_file = os.path.join(self.vpass_home_dir, 'default_template.yaml')

        # default config file
        self.vpass_config_file = os.path.join(self.vpass_home_dir, 'vpass_config.yaml')


    def start(self):
        self.create_app_structure()
        config = {
            'machines_dir': self.machines_dir,
            'base_vms_dir': self.base_vms_dir,
            'vpass_home_dir': self.vpass_home_dir,
            'default_template_file': self.default_template_file
        }


        with open(self.default_template_file , 'r') as stream:
            try:
                config['machine_config'] = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        return config


    def create_app_structure(self):
        # main vpass dir
        if not os.path.exists(self.vpass_home_dir):
            print(f"Creating {self.vpass_home_dir}")
            os.makedirs(self.vpass_home_dir)

        # template vm dir
        if not os.path.exists(self.base_vms_dir):
            print(f"Creating {self.base_vms_dir}")
            os.makedirs(self.base_vms_dir)

        # new machine dir
        if not os.path.exists(self.machines_dir):
            print(f"Creating {self.machines_dir}")
            os.makedirs(self.machines_dir)

        # config file
        if not os.path.exists(self.vpass_config_file):
            pass
            # TBI

        # template file
        if not os.path.exists(self.default_template_file):
            print(f"Creating {self.default_template_file}")
            copyfile(self.app_root_template_file, self.default_template_file)






