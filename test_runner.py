import json
import os
import sys
import unittest


def main(*args):
    if args:
        config_file_path = args[0]
        if os.path.exists(config_file_path):
            try:
                with open(config_file_path, 'r') as config_file:
                    config_data = json.load(config_file)

            except Exception as exp:
                print('all', 'config', '>', 'critical error when loading data from config file: %s' %
                      config_file_path)
                raise exp
        else:
            print('all', 'config', '>', 'file does not exist "%s"' % config_file_path)
            sys.exit(2)
    else:
        config_data = {}

    if config_data:
        test_names = config_data['test suites']
        test_suite = unittest.TestLoader().loadTestsFromNames(test_names)
        test_runner = unittest.TextTestRunner(verbosity=2)
        test_runner.run(test_suite)


if __name__ == '__main__':

    if len(sys.argv) > 1:
        argv = sys.argv[1:]
    else:
        argv = []

    main(*argv)
