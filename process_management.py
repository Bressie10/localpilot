import psutil
import getpass

user = getpass.getuser()

def psFunc(desired_processes):
    processes = []

    if desired_processes is not None and desired_processes != '-u':
        return 'Please enter a valid argument'
    

    for proc in psutil.process_iter(['pid', 'name', 'username']):

        info = proc.info
        pid = info['pid']
        name = info['name']
        username = info['username']

        if desired_processes == '-u':
            if username != user:
                continue

        ps_string = f'PID: {pid} | Name: {name} | Username: {username}'
        processes.append(ps_string)
    processes = "\n".join(processes)

    return processes
