import re
import json
from genie.metaparser import MetaParser


# ====================
# Schema for:
#  * 'show platform software fed switch active inject cause summary'
# ====================


class ShowPlatformSchema(MetaParser):
    """show platform software fed switch active inject cause summary"""

    schema = {
        "cause": {
            int: {
                "cause_info": str,
                "rcvd": int,
                "dropped": bool
            }
        }
    }


# ====================
# Parser for:
#  * 'show_platform_software_fed_switch_active_inject_cause_summary'
# ====================
class showPlatform(ShowPlatformSchema):
    """show platform software fed switch active inject cause summary"""
    
    cli_command = 'show platform software fed switch active inject cause summary'
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output


        result_dict = {}
        
        # KLANSW-9532Q-1#show platform software fed switch active inject cause summary 
        # Statistics for all causes

        # Cause  Cause Info                      Rcvd                 Dropped
        # ------------------------------------------------------------------------------
        # 1      L2 control/legacy               1511939              0                   
        # 2      QFP destination lookup          2004                 0                   
        # 5      QFP <->RP keepalive             890826               0                   
        # 7      QFP adjacency-id lookup         663543               0                   
        # 12     ARP request or response         341                  0                   
        # ------------------------------------------------------------------------------


        show_platform_capture = re.compile(r"^(?P<cause>\d+)\s+(?P<cause_info>([\S]+\s)+)\s+(?P<rcvd>\d+)\s+(?P<dropped>(0|1))")
        for line in out.splitlines():
            line = line.strip()
            m = show_platform_capture.match(line)   
            if m:
                group = m.groupdict()
                show_platform = group['cause']
                show_platform_dict = result_dict.setdefault('cause', {}).setdefault(show_platform, {})
                show_platform_dict['cause_info'] = group['cause_info']
                show_platform_dict['rcvd'] = group['rcvd']
                show_platform_dict['dropped'] = group['dropped']
                continue
        return result_dict

