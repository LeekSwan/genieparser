from pydoc import cli
import re
import json
from genie.metaparser import MetaParser


# ====================
# Schema for:
#  * 'show switch'
# ====================


class ShowSwitchSchema(MetaParser):
    """Schema for show switch"""

    schema = {
        "mac_address": str,
        "mac_persistency_wait_time": str,
        "switch": {
            "stack": {
                int: {
                    "role": str,
                    "mac_addresss": str,
                    "priority": int,
                    "hw_ver": str,
                    "state": str
                }
            }
        }
    }


# ====================
# Parser for:
#  * 'show switch'
# ====================
class ShowSwitch(ShowSwitchSchema):
    """Parser for show switch"""
    
    cli_command = 'show switch'
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output


        ap_summary_dict = {}
        # ====================
        # KLANSW-9532Q-1#show switch 
        # Switch/Stack Mac Address : 00a7.42d7.a200 - Local Mac Address
        # Mac persistency wait time: Indefinite
        #                                              H/W   Current
        # Switch#   Role    Mac Address     Priority Version  State 
        # -------------------------------------------------------------------------------------
        #  1       Standby  00a7.42d7.a200     5      V02     Ready                               
        # *2       Active   00a7.42d7.8680     12     V02     Ready     
        # ====================


        # Switch/Stack Mac Address : 00a7.42d7.a200 - Local Mac Address
        switch_stack_mac_address_capture = re.compile(r"^Switch/Stack\s+Mac\s+Address\s+:+\s+(?P<mac_address>\S+)")

        # Mac persistency wait time: Indefinite
        mac_persistency_wait_time_capture = re.compile(r"^Mac\s+persistency\s+wait\s+time:\s+(?P<mac_persistency_wait_time>(Indefinite))")

        #  1       Standby  00a7.42d7.a200     5      V02     Ready  
        show_switch_capture = re.compile(r"^\*?(?P<stack>\d+)\s+(?P<role>(Active|Standby|Member))\s+(?P<mac_address>\S+)\s+(?P<priority>\d+)\s+(?P<hw_ver>\S+)\s+(?P<state>(Ready|Version Mismatch|V-Mismatch))")
        
        for line in out.splitlines():
            line = line.strip()
            m = switch_stack_mac_address_capture.match(line)
            switch = ap_summary_dict.setdefault('switch', {})
            if m:
                group = m.groupdict()
                switch.setdefault('mac_address', group['mac_address'])
                continue

            m = mac_persistency_wait_time_capture.match(line)
            if m:
                group = m.groupdict()
                switch.setdefault('mac_persistency_wait_time', group['mac_persistency_wait_time'])
                continue

            m = show_switch_capture.match(line)
            if m:
                group = m.groupdict()
                show_switch = group['stack']
                show_switch_dict = ap_summary_dict.setdefault('switch', {}).setdefault('stack', {}).setdefault(show_switch, {})
                show_switch_dict['role'] = group['role']
                show_switch_dict['mac_address'] = group['mac_address']
                show_switch_dict['priority'] = group['priority']
                show_switch_dict['hw_ver'] = group['hw_ver']
                show_switch_dict['state'] = group['state']
                continue
        return ap_summary_dict
