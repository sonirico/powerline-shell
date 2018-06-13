import subprocess
import re
from ..utils import BasicSegment, decode


class Segment(BasicSegment):
    def add_to_powerline(self):
        powerline = self.powerline
        try:
            output = decode(subprocess.check_output(['uptime'], stderr=subprocess.STDOUT))
            regex = r'load\saverage\:\s(?P<one>\d+\,\d+),\s(?P<five>\d+\,\d+),\s(?P<fifteen>\d+\,\d+)'
            match = re.compile(regex).search(output)
            
            if not match:
                return

            powerline.append('%s|%s|%s' % match.groups(), 15, 166)
        except OSError:
            return
