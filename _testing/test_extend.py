import sys



args = ['python',
                '-m', 'pycharm-multiprocess-debug',
                'worker'
                ]

command_line = [
    "./py_echo",
    "current time"
]


args.extend(command_line)
sys.exit()
