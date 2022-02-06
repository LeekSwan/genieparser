import re
import json
from genie.metaparser import MetaParser


# ====================
# Schema for:
#  * 'show platform software object-manager switch active f0 statistics'
# ====================


class ShowPlatformSoftwareSchema(MetaParser):
    """show platform software object-manager switch active f0 statistics"""

    schema = {
        "object_manager_statistics" : {
            "object_update" : {
                "pending_issue": int,
                "pending_acknowledgement": int
            },
            "batch_begin" : {
                "pending_issue": int,
                "pending_acknowledgement": int
            },
            "batch_end" : {
                "pending_issue": int,
                "pending_acknowledgement": int
            },
            "command": int,
            "total_objects": int,
            "stale_objects": int,
            "resolve_objects": int,
            "childless_delete_objects": int,
            "error_objects": int,
            "paused_types": int
            }
    }


# ====================
# Parser for:
#  * 'show processes memory'
# ====================
class ShowPlatformSoftware(ShowPlatformSoftwareSchema):
    """show platform software object-manager switch active f0 statistics"""
    
    cli_command = 'show platform software object-manager switch active f0 statistics'
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output


        result_dict = {}
        
        # KLANSW-9324T-1#show platform software object-manager switch active f0 statistics 
        # Forwarding Manager Asynchronous Object Manager Statistics

        # Object update: Pending-issue: 0, Pending-acknowledgement: 0
        # Batch begin:   Pending-issue: 0, Pending-acknowledgement: 0
        # Batch end:     Pending-issue: 0, Pending-acknowledgement: 0
        # Command:       Pending-acknowledgement: 0
        # Total-objects: 419
        # Stale-objects: 0
        # Resolve-objects: 0
        # Childless-delete-objects: 0
        # Error-objects: 0
        # Paused-types: 0

        p1 = re.compile(r'Object +update: +Pending-issue: +(?P<pending_issue>\d+), +Pending-acknowledgement: +(?P<pending_acknowledgement>\d+)')
        p2 = re.compile(r'Batch +begin: +Pending-issue: +(?P<pending_issue>\d+), +Pending-acknowledgement: +(?P<pending_acknowledgement>\d+)')
        p3 = re.compile(r'Batch +end: +Pending-issue: +(?P<pending_issue>\d+), +Pending-acknowledgement: +(?P<pending_acknowledgement>\d+)')
        p4 = re.compile(r'Command: +Pending-acknowledgement: +(?P<command>\d+)')
        p5 = re.compile(r'Total-objects: +(?P<total_objects>\d+)')
        p6 = re.compile(r'Stale-objects: +(?P<stale_objects>\d+)')
        p7 = re.compile(r'Resolve-objects: +(?P<resolve_objects>\d+)')
        p8 = re.compile(r'Childless-delete-objects: +(?P<childless_delete_objects>\d+)')
        p9 = re.compile(r'Error-objects: +(?P<error_objects>\d+)')
        p10 = re.compile(r'Paused-types: +(?P<paused_types>\d+)')

        for line in out.splitlines():
            line = line.strip()
            stat_dict = result_dict.setdefault('object_manager_statistics', {})

            m = p1.match(line)
            if m:
                group = m.groupdict()
                object_stats = stat_dict.setdefault('object_update', {})
                object_stats['pending_issue'] = int(group['pending_issue'])
                object_stats['pending_acknowledgement'] = int(group['pending_acknowledgement'])
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                object_stats = stat_dict.setdefault('batch_begin', {})
                object_stats['pending_issue'] = int(group['pending_issue'])
                object_stats['pending_acknowledgement'] = int(group['pending_acknowledgement'])
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                object_stats = stat_dict.setdefault('batch_end', {})
                object_stats['pending_issue'] = int(group['pending_issue'])
                object_stats['pending_acknowledgement'] = int(group['pending_acknowledgement'])
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                stat_dict['command'] = group['command']
                continue
            m = p5.match(line)
            if m:
                group = m.groupdict()
                stat_dict['total_objects'] = group['total_objects']
                continue
            m = p6.match(line)
            if m:
                group = m.groupdict()
                stat_dict['stale_objects'] = group['stale_objects']
                continue
            m = p7.match(line)
            if m:
                group = m.groupdict()
                stat_dict['resolve_objects'] = group['resolve_objects']
                continue
            m = p8.match(line)
            if m:
                group = m.groupdict()
                stat_dict['childless_delete_objects'] = group['childless_delete_objects']
                continue
            m = p9.match(line)
            if m:
                group = m.groupdict()
                stat_dict['error_objects'] = group['error_objects']
                continue
            m = p10.match(line)
            if m:
                group = m.groupdict()
                stat_dict['paused_types'] = group['paused_types']
                continue
        return result_dict
