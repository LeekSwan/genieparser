import re
import json
from genie.metaparser import MetaParser


# ====================
# Schema for:
#  * 'show file systems'
# ====================



class ShowFileSystemsSchema(MetaParser):
    """show file systems"""

    schema = {
        "file_systems": {
            str: {
                "size": int,
                "free": int,
                "type": str,
                "flags": str,
            }
        }
    }


# ====================
# Parser for:
#  * 'show_platform_software_fed_switch_active_punt_cause_summary'
# ====================
class showFileSystems(ShowFileSystemsSchema):
    """show file systems"""
    
    cli_command = 'show file systems'
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}
        # KLANSW-9532Q-1#show file systems 
        # File Systems:

        # Size(b)       Free(b)      Type  Flags  Prefixes
        #         -             -    opaque     rw   system:
        #         -             -    opaque     rw   tmpsys:
        # *  11250098176    3785482240      disk     rw   bootflash: flash:
        # 11250171904    2152726528      disk     rw   bootflash-1:
        # 1651314688     166285312      disk     rw   crashinfo:
        # 1651507200     159383552      disk     rw   crashinfo-1:
        # 236154740736  222120800256      disk     rw   disk0:
        # 236155043840  220535455744      disk     rw   disk0-1:
        # 8061177856    7947182080      disk     ro   webui:
        # 33554432      33128830     nvram     rw   stby-nvram:
        #         -             -    opaque     rw   null:
        #         -             -    opaque     ro   tar:
        #         -             -   network     rw   tftp:
        # 33554432      33131902     nvram     rw   nvram:
        #         -             -    opaque     wo   syslog:
        #         -             -   network     rw   rcp:
        #         -             -   network     rw   http:
        #         -             -   network     rw   ftp:
        #         -             -   network     rw   scp:
        #         -             -   network     rw   sftp:
        #         -             -   network     rw   https:
        #         -             -    opaque     ro   cns:
        #         -             -     nvram     rw   stby-rcsf:
        # 11250098176    2152091648      disk     rw   stby-bootflash:
        #         -             -      disk     rw   stby-usbflash0:
        # 1651314688     159084544      disk     rw   stby-crashinfo:
        # 236154740736  220535107584      disk     rw   stby-disk0:
        #         -             -    opaque     rw   revrcsf:



        #  7      ARP request or response         338                  0  

        # show_file_system_capture = re.compile(r"^\*?(?P<size>(\d+|-))\s+(?P<free>(\d+|-))\s+(?P<type>\S+)\s+(?P<flags>\S+)\s+(?P<prefixes>(([\S]+\s)+))")
        show_file_system_capture = re.compile(r"^(\*\s+)?(?P<size>(\d+|-))\s+(?P<free>(\d+|-))\s+(?P<type>\S+)\s+(?P<flags>\S+)\s+(?P<prefixes>(\S+(\s|))+)")
        for line in out.splitlines():
            line = line.strip()
            
            # print(line)
            m = show_file_system_capture.match(line)   
            if m:
                group = m.groupdict()
                show_file_system = group['prefixes']
                show_file_system_dict = result_dict.setdefault('file_systems', {}).setdefault(show_file_system, {})
                show_file_system_dict['size'] = group['size']
                show_file_system_dict['free'] = group['free']
                show_file_system_dict['type'] = group['type']
                show_file_system_dict['flags'] = group['flags']
                continue
        return result_dict