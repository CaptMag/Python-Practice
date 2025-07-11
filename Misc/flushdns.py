#!/usr/bin/python
import subprocess
import time
from daemon import runner

class flushing():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pdifile_path = '/tmp/foo.pid'
        self.pidfile_timeout = 5
    def run(self):
        while True:
            print("Everything is working!")
            subprocess.run("echo", "hello", shell=True, timeout=False, check=True)
            time.sleep(10)

flush = flushing()
daemon_runner = runner.DaemonRunner(flush)
daemon_runner.do_action()
