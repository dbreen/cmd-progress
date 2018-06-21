#!/usr/bin/python3
import os
import sys
import time


class Runner:
    run_ticks = 10  # Run for N ticks, pausing for an interval each time
    progress_interval = 1  # Emit progress every N seconds
    progress_filename = 'progress.txt'
    
    def __init__(self):
        self.progress = 0
    
    def run(self):
        self.clear_progress()
        if os.path.exists(self.progress_filename):
            self.fatal('Progress file exists')
        for i in range(self.run_ticks):
            self.update(int((i+1) / float(self.run_ticks) * 100))
            time.sleep(self.progress_interval)

    def update(self, progress):
        try:
            with open(self.progress_filename, 'w') as f:
                f.write(str(progress))
        except OSError as exc:
            self.fatal("Could not write progress: {}".format(exc))
    
    def clear_progress(self):
        try:
            os.unlink(self.progress_filename)
        except OSError:
            pass  # Didn't exist, no problem
    
    def fatal(self, msg, errcode=1):
        print(msg, file=sys.stderr)
        sys.exit(errcode)

if __name__ == "__main__":
    runner = Runner()
    runner.run()
