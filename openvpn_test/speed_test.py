import sys
import json
import subprocess
import traceback


def test():
    with subprocess.Popen(args=['speedtest', '--json'],
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE) as process:
        try:
            stdout, stderr = process.communicate(timeout=60)
            sys.stdout.buffer.write(stdout)
            sys.stderr.buffer.write(stderr)
            result = json.loads(stdout)
            return result['download']
        except Exception:
            print(traceback.format_exc())
            process.kill()
            return None
