#!/usr/bin/python

import os
import subprocess
import schedule
import time


def refresh():
    arg_name = ['username', 'password', 'cookie-directory', 'size', 'until-found',
                'skip-videos', 'skip-live-photos', 'force-size', 'force-size', 'auto-delete', 'only-print-filenames',
                'folder-structure', 'set-exif-datetime', 'smtp-username', 'smtp-password', 'smtp-host', 'smtp-port', 'smtp-no-tls',
                'notification-email', 'notification-script', 'log-level', 'no-progress-bar']

    args = ['icloudpd']
    data_path = os.environ.get('DATA_PATH')

    if data_path is None:
        data_path = "/data"
    args.append(data_path)

    for v in arg_name:
        env = os.environ.get(v.upper().replace('-', '_'))
        if env is not None:
            args.append("--" + v)
            args.append(env)

    p = subprocess.Popen("pgrep -l icloudpd", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p.wait()
    if len(p.stdout.readlines()) > 0:
        print("icloudpd is already running.")
    else:
        subprocess.Popen(args)


schedule.every(3600).seconds.do(refresh)
refresh()

while True:
    schedule.run_pending()
    time.sleep(1)


