import re
import json
from genie.metaparser import MetaParser


# ====================
# Schema for:
#  * 'show processes memory'
# ====================


class ShowProcessesMemorySchema(MetaParser):
    """show processes memory"""

    schema = {
        'system_memory':{
            "processor_pool": {
                "total": int,
                "free": int,
                "used": int,
            },
            "reserve_p_pool": {
                "total": int,
                "free": int,
                "used": int,
            },
            "lsmpi_io_pool": {
                "total": int,
                "free": int,
                "used": int,
            },
            "process": {
                str: {
                    "pid": int,
                    "tty": int,
                    "allocated": int,
                    "freed": int,
                    "holding": int,
                    "getbufs": int,
                    "retbufs": int
                }
            }
        }
        
    }


# ====================
# Parser for:
#  * 'show processes memory'
# ====================
class showProcessesMemory(ShowProcessesMemorySchema):
    """show processes memory"""
    
    cli_command = 'show processes memory'
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output


        result_dict = {}
        
        # KLANSW-9532Q-1#show processes memory 
        # Processor Pool Total: 2973793036 Used:  370412528 Free: 2603380508
        # reserve P Pool Total:     102404 Used:         88 Free:     102316
        #  lsmpi_io Pool Total:    6295128 Used:    6294296 Free:        832

        #  PID TTY  Allocated      Freed    Holding    Getbufs    Retbufs Process
        #    0   0  306886392   53956232  234244744        522    4340109 *Init*          
        #    0   0       3456   68796520       3456          3          3 *Sched*         
        #    0   0  547485488  518231880    6993624       1725       1719 *Dead*          
        #    0   0          0          0     920512          0          0 *MallocLite*    
        #    1   0    1581584      45280    1587168          0          0 Chunk Manager   
        #    2   0      43648        448      61144          0          0 Load Meter      
        #    3   0      34096      28280      29944         27         27 SpanTree Helper 
        #    4   0   29302784    2287432   23365104       1946       1946 RF Slave Main Th
        #    5   0          0          0      30056          0          0 Retransmission o
        #    6   0      92336        144      29944          0          0 IPC ISSU Dispatc

        p1 = re.compile(r'Processor +Pool +Total: +(?P<total>(\d+)) +Used: +(?P<used>(\d+)) +Free: +(?P<free>(\d+))')
        p2 = re.compile(r'reserve +P +Pool +Total: +(?P<total>(\d+)) +Used: +(?P<used>(\d+)) +Free: +(?P<free>(\d+))')
        p3 = re.compile(r'lsmpi_io +Pool +Total: +(?P<total>(\d+)) +Used: +(?P<used>(\d+)) +Free: +(?P<free>(\d+))')
        show_processes_memory_capture = re.compile(r"^(?P<pid>\d+)\s+(?P<tty>\d+)\s+(?P<allocated>\d+)\s+(?P<freed>\d+)\s+(?P<holding>\d+)\s+(?P<getbufs>\d+)\s+(?P<retbufs>\d+)\s+(?P<process>[\S\s]+)")


        for line in out.splitlines():
            line = line.strip()

            mem_dict = result_dict.setdefault('system_memory', {})
            process_pool_dict = mem_dict.setdefault('processor_pool', {})
            reserve_pool_dict = mem_dict.setdefault('reserve_p_pool', {})
            lmspi_pool_dict = mem_dict.setdefault('lsmpi_io_pool', {})


            m = p1.match(line)
            if m:
                group = m.groupdict()
                process_pool_dict['total'] = int(group['total'])
                process_pool_dict['used'] = int(group['used'])
                process_pool_dict['free'] = int(group['free'])
                continue
            m = p2.match(line)
            if m:
                group = m.groupdict()
                reserve_pool_dict['total'] = int(group['total'])
                reserve_pool_dict['used'] = int(group['used'])
                reserve_pool_dict['free'] = int(group['free'])
                continue
            m = p3.match(line)
            if m:
                group = m.groupdict()
                lmspi_pool_dict['total'] = int(group['total'])
                lmspi_pool_dict['used'] = int(group['used'])
                lmspi_pool_dict['free'] = int(group['free'])
                continue
            m = show_processes_memory_capture.match(line)   
        
            if m:
                group = m.groupdict()
                show_processes_memory = group['process']
                show_processes_memory_dict = mem_dict.setdefault('process', {}).setdefault(show_processes_memory, {})
                show_processes_memory_dict['pid'] = int(group['pid'])
                show_processes_memory_dict['tty'] = int(group['tty'])
                show_processes_memory_dict['allocated'] = int(group['allocated'])
                show_processes_memory_dict['freed'] = int(group['freed'])
                show_processes_memory_dict['holding'] = int(group['holding'])
                show_processes_memory_dict['getbufs'] = int(group['getbufs'])
                show_processes_memory_dict['retbufs'] = int(group['retbufs'])
                continue
        return result_dict

