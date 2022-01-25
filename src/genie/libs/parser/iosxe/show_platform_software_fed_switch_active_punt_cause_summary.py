import re
import json
from genie.metaparser import MetaParser


# ====================
# Schema for:
#  * 'show platform software fed switch active punt cause summary'
# ====================

class ShowPlatformSchema(MetaParser):
    """show platform software fed switch active punt cause summary"""

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
#  * 'show_platform_software_fed_switch_active_punt_cause_summary'
# ====================
class showPlatform(ShowPlatformSchema):
    """show platform software fed switch active punt cause summary"""
    
    cli_command = 'show platform software fed switch active punt cause summary'
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output


        result_dict = {}
        # KLANSW-9532Q-1#show platform software fed switch active punt cause summary 
        # Statistics for all causes

        # Cause  Cause Info                      Rcvd                 Dropped
        # ------------------------------------------------------------------------------
        # 7      ARP request or response         338                  0                   
        # 11     For-us data                     1038                 0                   
        # 21     RP<->QFP keepalive              890814               0                   
        # 24     Glean adjacency                 1                    0                   
        # 29     RP handled ICMP                 1                    0                   
        # 55     For-us control                  348133               0                   
        # 96     Layer2 control protocols        7444963              0                   
        # ------------------------------------------------------------------------------


        #  7      ARP request or response         338                  0  
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

                