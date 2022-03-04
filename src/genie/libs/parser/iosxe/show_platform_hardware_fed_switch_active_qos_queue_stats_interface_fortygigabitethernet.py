import re
import json
from genie.metaparser import MetaParser


class ShowPlatformHardwareSchema(MetaParser):
    """show platform hardware fed switch active qos queue stats interface FortyGigabitEthernet 1/1/2"""

    schema = {
        'global_hard_limit': int,
        'global_soft_limit': int,
        'global_hard_buf_count': int,
        'global_soft_buf_count': int,
        'hardware_enqueue_counters': {
            'asic': int,
            'core': int,
            'port': int,
            'q': {
                int: {
                    'buffer_count': int,
                    'enqueue_th0' : int,
                    'enqueue_th1' : int,
                    'enqueue_th2' : int,
                    'q_policer' : int,
                }
            }
        },
        'hardware_drop_counters': {
            'asic': int,
            'core': int,
            'port': int,
            'q': {
                int: {
                    'drop_th0' : int,
                    'drop_th1' : int,
                    'drop_th2' : int,
                    's_buf_drop' : int,
                    'q_eb_drop' : int,
                    'q_policer_drop' : int,
                }
            }
        }
    }


# ====================
# Parser for:
#  * 'show platform hardware fed switch active qos queue stats interface FortyGigabitEthernet 1/1/2'
# ====================
class ShowPlatformHardware(ShowPlatformHardwareSchema):
    """show platform hardware fed switch active qos queue stats interface FortyGigabitEthernet 1/1/2"""
    
    cli_command = 'show platform hardware fed switch active qos queue stats interface FortyGigabitEthernet 1/1/2'
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output


        result_dict = {}
        
        # GlobalHardLimit:  6127   |   GlobalHardBufCount: 0
        # GlobalSoftLimit: 13721   |   GlobalSoftBufCount: 0
        p1 = re.compile(r'GlobalHardLimit: +(?P<global_hard_limit>\d+) +\| +GlobalHardBufCount: +(?P<global_hard_buf_count>\d+)')
        p2 = re.compile(r'GlobalSoftLimit: +(?P<global_soft_limit>\d+) +\| +GlobalSoftBufCount: +(?P<global_soft_buf_count>\d+)')

        # Asic:0 Core:0 DATA Port:37 Hardware Enqueue Counters
        p3 = re.compile(r'Asic: *(?P<asic>\d+) *Core: *(?P<core>\d+) *DATA *Port: *(?P<port>\d+) *Hardware *Enqueue *Counters')

        #  Q Buffers          Enqueue-TH0          Enqueue-TH1          Enqueue-TH2             Qpolicer
        #    (Count)              (Bytes)              (Bytes)              (Bytes)              (Bytes)ergo
        # -- ------- -------------------- -------------------- -------------------- --------------------
        #  0       0                    0               104748             11638025                    0
        p4 = re.compile(r'(?P<q>\d+)\s+(?P<buffer_count>\d+)\s+(?P<enqueue_th0>\d+)\s+(?P<enqueue_th1>\d+)\s+(?P<enqueue_th2>\d+)\s+(?P<q_policer>\d+)$')

        # Asic:0 Core:0 DATA Port:37 Hardware Drop Counters
        p5 = re.compile(r'Asic: *(?P<asic>\d+) *Core: *(?P<core>\d+) *DATA *Port: *(?P<port>\d+) *Hardware *Drop *Counters')

        # Q             Drop-TH0             Drop-TH1             Drop-TH2             SBufDrop              QebDrop         QpolicerDrop
        #                 (Bytes)              (Bytes)              (Bytes)              (Bytes)              (Bytes)              (Bytes)
        # -- -------------------- -------------------- -------------------- -------------------- -------------------- --------------------
        # 0                    0                    0                    0                    0                    0                    0
        p6 = re.compile(r'(?P<q>\d+)\s+(?P<drop_th0>\d+)\s+(?P<drop_th1>\d+)\s+(?P<drop_th2>\d+)\s+(?P<s_buf_drop>\d+)\s+(?P<q_eb_drop>\d+)\s+(?P<q_policer_drop>\d+)')

        for line in out.splitlines():
            line = line.strip()
            hardware_enqueue_dict = result_dict.setdefault('hardware_enqueue_counters', {})
            hardware_drop_dict = result_dict.setdefault('hardware_drop_counters', {})
            hardware_drop_q_dict = hardware_drop_dict.setdefault('q', {})
            hardware_enqueue_q_dict = hardware_enqueue_dict.setdefault('q', {})

            m = p1.match(line)
            if m:
                group = m.groupdict()
                result_dict['global_hard_limit'] = int(group['global_hard_limit'])
                result_dict['global_hard_buf_count'] = int(group['global_hard_buf_count'])
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                result_dict['global_soft_limit'] = int(group['global_soft_limit'])
                result_dict['global_soft_buf_count'] = int(group['global_soft_buf_count'])
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                hardware_enqueue_dict['asic'] = int(group['asic'])
                hardware_enqueue_dict['core'] = int(group['core'])
                hardware_enqueue_dict['port'] = int(group['port'])
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                q_dict = hardware_enqueue_q_dict.setdefault(group['q'], {})
                q_dict['buffer_count'] = int(group['buffer_count'])
                q_dict['enqueue_th0'] = int(group['enqueue_th0'])
                q_dict['enqueue_th1'] = int(group['enqueue_th1'])
                q_dict['enqueue_th2'] = int(group['enqueue_th2'])
                q_dict['q_policer'] = int(group['q_policer'])
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                hardware_drop_dict['asic'] = int(group['asic'])
                hardware_drop_dict['core'] = int(group['core'])
                hardware_drop_dict['port'] = int(group['port'])
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                q_dict = hardware_drop_q_dict.setdefault(group['q'], {})
                q_dict['drop_th0'] = int(group['drop_th0'])
                q_dict['drop_th1'] = int(group['drop_th1'])
                q_dict['drop_th2'] = int(group['drop_th2'])
                q_dict['s_buf_drop'] = int(group['s_buf_drop'])
                q_dict['q_eb_drop'] = int(group['q_eb_drop'])
                q_dict['q_policer_drop'] = int(group['q_policer_drop'])
                continue

        return result_dict
