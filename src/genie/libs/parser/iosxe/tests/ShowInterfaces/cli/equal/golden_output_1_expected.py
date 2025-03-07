expected_output = {
    "BDI105": {
        "bandwidth": 100000,
        "counters": {
            "in_crc_errors": 0,
            "in_errors": 0,
            "in_frame": 0,
            "in_giants": 0,
            "in_ignored": 0,
            "in_no_buffer": 0,
            "in_octets": 3929639714,
            "in_overrun": 0,
            "in_pkts": 35283845,
            "in_runts": 0,
            "in_throttles": 0,
            "last_clear": "never",
            "out_buffer_failure": 0,
            "out_buffers_swapped": 0,
            "out_errors": 0,
            "out_interface_resets": 0,
            "out_octets": 287424110,
            "out_pkts": 1933865,
            "out_underruns": 0,
            "out_unknown_protocl_drops": 0,
            "rate": {
                "in_rate": 2000,
                "in_rate_pkts": 2,
                "load_interval": 300,
                "out_rate": 0,
                "out_rate_pkts": 0,
            },
        },
        "delay": 10,
        "description": "PXMS Connexion Explore CWS L2 / Primary VLAN for CHRH",
        "enabled": True,
        "encapsulations": {"encapsulation": "802.1q vlan", "first_dot1q": "105"},
        "ipv4": {"10.95.2.253/24": {"ip": "10.95.2.253", "prefix_length": "24"}},
        "line_protocol": "up",
        "mac_address": "2c33.11ff.fbc7",
        "mtu": 1500,
        "oper_status": "up",
        "phys_address": "2c33.11ff.fbc7",
        "port_channel": {"port_channel_member": False},
        "queues": {
            "output_queue_max": 40,
            "output_queue_size": 0,
            "queue_strategy": "fifo",
        },
        "reliability": "255/255",
        "rxload": "1/255",
        "txload": "1/255",
        "type": "BDI",
    },
    "BDI106": {
        "arp_timeout": "04:00:00",
        "arp_type": "arpa",
        "bandwidth": 100000,
        "counters": {
            "in_broadcast_pkts": 0,
            "in_crc_errors": 0,
            "in_errors": 0,
            "in_frame": 0,
            "in_giants": 0,
            "in_ignored": 0,
            "in_multicast_pkts": 0,
            "in_no_buffer": 0,
            "in_octets": 1729,
            "in_overrun": 0,
            "in_pkts": 24,
            "in_runts": 0,
            "in_throttles": 0,
            "last_clear": "never",
            "out_buffer_failure": 0,
            "out_buffers_swapped": 0,
            "out_errors": 0,
            "out_interface_resets": 0,
            "out_octets": 442723849,
            "out_pkts": 4930792,
            "out_underruns": 0,
            "out_unknown_protocl_drops": 0,
            "rate": {
                "in_rate": 0,
                "in_rate_pkts": 0,
                "load_interval": 300,
                "out_rate": 0,
                "out_rate_pkts": 0,
            },
        },
        "delay": 10,
        "description": "PXMS connexion Explore CWS L2 / Backup VLAN for CHRH",
        "enabled": True,
        "encapsulations": {"encapsulation": "802.1q vlan", "first_dot1q": "106"},
        "ipv4": {"10.1.2.43/24": {"ip": "10.1.2.43", "prefix_length": "24"}},
        "last_input": "never",
        "last_output": "25w2d",
        "line_protocol": "up",
        "mac_address": "2c33.11ff.32c7",
        "mtu": 1500,
        "oper_status": "up",
        "output_hang": "never",
        "phys_address": "2c33.11ff.32c7",
        "port_channel": {"port_channel_member": False},
        "queues": {
            "input_queue_drops": 0,
            "input_queue_flushes": 0,
            "input_queue_max": 375,
            "input_queue_size": 0,
            "output_queue_max": 40,
            "output_queue_size": 0,
            "queue_strategy": "fifo",
            "total_output_drop": 0,
        },
        "reliability": "255/255",
        "rxload": "1/255",
        "txload": "1/255",
        "type": "BDI",
    },
    "Dialer1": {
        "bandwidth": 56,
        "connected": False,
        "suspended": False,
        "err_disabled": False,
        "counters": {
            "in_octets": 0,
            "in_pkts": 0,
            "last_clear": "never",
            "out_octets": 0,
            "out_pkts": 0,
            "rate": {
                "in_rate": 0,
                "in_rate_pkts": 0,
                "load_interval": 300,
                "out_rate": 0,
                "out_rate_pkts": 0,
            },
        },
        "delay": 20000,
        "enabled": True,
        "encapsulations": {"encapsulation": "hdlc"},
        "keepalive": 10,
        "dtr_pulsed": "1",
        "last_input": "never",
        "last_output": "never",
        "line_protocol": "up",
        "mtu": 1492,
        "oper_status": "up",
        "output_hang": "never",
        "port_channel": {"port_channel_member": False},
        "queues": {
            "input_queue_drops": 0,
            "input_queue_flushes": 0,
            "input_queue_max": 375,
            "input_queue_size": 0,
            "queue_strategy": "weighted",
            "total_output_drop": 0,
            "output_queue_max": 1000,
            "output_queue_size": 0,
            "threshold": 64,
            "drops": 0,
        },
        "reliability": "255/255",
        "rxload": "1/255",
        "txload": "1/255",
        "type": "Unknown",
    },
    "GigabitEthernet0": {
        "arp_timeout": "04:00:00",
        "arp_type": "arpa",
        "auto_negotiate": True,
        "bandwidth": 1000000,
        "counters": {
            "in_broadcast_pkts": 21865326,
            "in_crc_errors": 0,
            "in_errors": 0,
            "in_frame": 0,
            "in_giants": 0,
            "in_ignored": 0,
            "in_mac_pause_frames": 0,
            "in_multicast_pkts": 0,
            "in_no_buffer": 0,
            "in_octets": 31345442345,
            "in_overrun": 0,
            "in_pkts": 246659819,
            "in_runts": 0,
            "in_throttles": 0,
            "in_watchdog": 0,
            "last_clear": "never",
            "out_babble": 0,
            "out_buffer_failure": 0,
            "out_buffers_swapped": 0,
            "out_collision": 0,
            "out_deferred": 0,
            "out_errors": 0,
            "out_interface_resets": 0,
            "out_late_collision": 0,
            "out_lost_carrier": 1,
            "out_mac_pause_frames": 0,
            "out_no_carrier": 0,
            "out_octets": 24622021354,
            "out_pkts": 191782907,
            "out_underruns": 0,
            "out_unknown_protocl_drops": 0,
            "rate": {
                "in_rate": 5000,
                "in_rate_pkts": 6,
                "load_interval": 300,
                "out_rate": 3000,
                "out_rate_pkts": 4,
            },
        },
        "delay": 10,
        "duplex_mode": "full",
        "enabled": True,
        "encapsulations": {"encapsulation": "arpa"},
        "flow_control": {"receive": False, "send": False},
        "ipv4": {"172.31.0.24/16": {"ip": "172.31.0.24", "prefix_length": "16"}},
        "keepalive": 10,
        "last_input": "00:00:00",
        "last_output": "00:00:00",
        "line_protocol": "up",
        "link_type": "auto",
        "mac_address": "2c33.11ff.3149",
        "media_type": "RJ45",
        "mtu": 1500,
        "oper_status": "up",
        "output_hang": "never",
        "phys_address": "2c33.11ff.3149",
        "port_channel": {"port_channel_member": False},
        "port_speed": "1000mbps",
        "queues": {
            "input_queue_drops": 0,
            "input_queue_flushes": 2586,
            "input_queue_max": 75,
            "input_queue_size": 0,
            "output_queue_max": 40,
            "output_queue_size": 0,
            "queue_strategy": "fifo",
            "total_output_drop": 0,
        },
        "reliability": "255/255",
        "rxload": "1/255",
        "txload": "1/255",
        "type": "RP management port",
    },
    "Loopback50998": {
        "bandwidth": 8000000,
        "counters": {
            "in_abort": 0,
            "in_broadcast_pkts": 0,
            "in_crc_errors": 0,
            "in_errors": 0,
            "in_frame": 0,
            "in_giants": 0,
            "in_ignored": 0,
            "in_multicast_pkts": 0,
            "in_no_buffer": 0,
            "in_octets": 0,
            "in_overrun": 0,
            "in_pkts": 0,
            "in_runts": 0,
            "in_throttles": 0,
            "last_clear": "never",
            "out_buffer_failure": 0,
            "out_buffers_swapped": 0,
            "out_collision": 0,
            "out_errors": 0,
            "out_interface_resets": 0,
            "out_octets": 0,
            "out_pkts": 0,
            "out_underruns": 0,
            "out_unknown_protocl_drops": 0,
            "rate": {
                "in_rate": 0,
                "in_rate_pkts": 0,
                "load_interval": 300,
                "out_rate": 0,
                "out_rate_pkts": 0,
            },
        },
        "delay": 5000,
        "enabled": True,
        "encapsulations": {"encapsulation": "loopback"},
        "ipv4": {"10.1.2.32/32": {"ip": "10.1.2.32", "prefix_length": "32"}},
        "keepalive": 10,
        "last_input": "never",
        "last_output": "never",
        "line_protocol": "up",
        "mtu": 1514,
        "oper_status": "up",
        "output_hang": "never",
        "port_channel": {"port_channel_member": False},
        "queues": {
            "input_queue_drops": 0,
            "input_queue_flushes": 0,
            "input_queue_max": 75,
            "input_queue_size": 0,
            "output_queue_max": 0,
            "output_queue_size": 0,
            "queue_strategy": "fifo",
            "total_output_drop": 0,
        },
        "reliability": "255/255",
        "rxload": "1/255",
        "txload": "1/255",
        "type": "Loopback",
    },
    "TenGigabitEthernet0/1/6": {
        "arp_timeout": "04:00:00",
        "arp_type": "arpa",
        "bandwidth": 10000000,
        "auto_negotiate": False,
        "counters": {
            "in_broadcast_pkts": 0,
            "in_crc_errors": 0,
            "in_errors": 0,
            "in_frame": 0,
            "in_giants": 0,
            "in_ignored": 0,
            "in_mac_pause_frames": 0,
            "in_multicast_pkts": 0,
            "in_no_buffer": 0,
            "in_octets": 0,
            "in_overrun": 0,
            "in_pkts": 0,
            "in_runts": 0,
            "in_throttles": 0,
            "in_watchdog": 0,
            "last_clear": "never",
            "out_babble": 0,
            "out_buffer_failure": 0,
            "out_buffers_swapped": 0,
            "out_collision": 0,
            "out_deferred": 0,
            "out_errors": 0,
            "out_interface_resets": 1,
            "out_late_collision": 0,
            "out_lost_carrier": 0,
            "out_mac_pause_frames": 0,
            "out_no_carrier": 0,
            "out_octets": 0,
            "out_pkts": 0,
            "out_underruns": 0,
            "out_unknown_protocl_drops": 0,
            "rate": {
                "in_rate": 0,
                "in_rate_pkts": 0,
                "load_interval": 300,
                "out_rate": 0,
                "out_rate_pkts": 0,
            },
        },
        "delay": 10,
        "duplex_mode": "full",
        "link_type": "force-up",
        "media_type": "unknown",
        "enabled": False,
        "port_speed": "10000mbps",
        "encapsulations": {"encapsulation": "arpa"},
        "flow_control": {"receive": False, "send": False},
        "last_input": "never",
        "last_output": "never",
        "line_protocol": "down",
        "mac_address": "2c33.11ff.311f",
        "mtu": 1500,
        "oper_status": "down",
        "output_hang": "never",
        "phys_address": "2c33.11ff.311f",
        "port_channel": {"port_channel_member": False},
        "queues": {
            "input_queue_drops": 0,
            "input_queue_flushes": 0,
            "input_queue_max": 375,
            "input_queue_size": 0,
            "output_queue_max": 40,
            "output_queue_size": 0,
            "queue_strategy": "fifo",
            "total_output_drop": 0,
        },
        "reliability": "255/255",
        "rxload": "1/255",
        "txload": "1/255",
        "type": "BUILT-IN-EPA-8x10G",
    },
    "TenGigabitEthernet0/1/7": {
        "arp_timeout": "04:00:00",
        "arp_type": "arpa",
        "bandwidth": 10000000,
        "auto_negotiate": False,
        "counters": {
            "in_broadcast_pkts": 0,
            "in_crc_errors": 0,
            "in_errors": 0,
            "in_frame": 0,
            "in_giants": 0,
            "in_ignored": 0,
            "in_mac_pause_frames": 0,
            "in_multicast_pkts": 0,
            "in_no_buffer": 0,
            "in_octets": 0,
            "in_overrun": 0,
            "in_pkts": 0,
            "in_runts": 0,
            "in_throttles": 0,
            "in_watchdog": 0,
            "last_clear": "never",
            "out_babble": 0,
            "out_buffer_failure": 0,
            "out_buffers_swapped": 0,
            "out_collision": 0,
            "out_deferred": 0,
            "out_errors": 0,
            "out_interface_resets": 1,
            "out_late_collision": 0,
            "out_lost_carrier": 0,
            "out_mac_pause_frames": 0,
            "out_no_carrier": 0,
            "out_octets": 0,
            "out_pkts": 0,
            "out_underruns": 0,
            "out_unknown_protocl_drops": 0,
            "rate": {
                "in_rate": 0,
                "in_rate_pkts": 0,
                "load_interval": 300,
                "out_rate": 0,
                "out_rate_pkts": 0,
            },
        },
        "delay": 10,
        "duplex_mode": "full",
        "enabled": False,
        "encapsulations": {"encapsulation": "arpa"},
        "flow_control": {"receive": False, "send": False},
        "last_input": "never",
        "last_output": "never",
        "line_protocol": "down",
        "link_type": "force-up",
        "media_type": "unknown",
        "mac_address": "2c33.11ff.3120",
        "mtu": 1500,
        "oper_status": "down",
        "output_hang": "never",
        "port_speed": "10000mbps",
        "phys_address": "2c33.11ff.3120",
        "port_channel": {"port_channel_member": False},
        "queues": {
            "input_queue_drops": 0,
            "input_queue_flushes": 0,
            "input_queue_max": 375,
            "input_queue_size": 0,
            "output_queue_max": 40,
            "output_queue_size": 0,
            "queue_strategy": "fifo",
            "total_output_drop": 0,
        },
        "reliability": "255/255",
        "rxload": "1/255",
        "txload": "1/255",
        "type": "BUILT-IN-EPA-8x10G",
    },
    "TenGigabitEthernet0/1/86": {
        "arp_timeout": "04:00:00",
        "arp_type": "arpa",
        "bandwidth": 10000000,
        "auto_negotiate": False,
        "counters": {
            "in_broadcast_pkts": 0,
            "in_crc_errors": 0,
            "in_errors": 0,
            "in_frame": 0,
            "in_giants": 0,
            "in_ignored": 0,
            "in_mac_pause_frames": 0,
            "in_multicast_pkts": 0,
            "in_no_buffer": 0,
            "in_octets": 0,
            "in_overrun": 0,
            "in_pkts": 0,
            "in_runts": 0,
            "in_throttles": 0,
            "in_watchdog": 0,
            "last_clear": "never",
            "out_babble": 0,
            "out_buffer_failure": 0,
            "out_buffers_swapped": 0,
            "out_collision": 0,
            "out_deferred": 0,
            "out_errors": 0,
            "out_interface_resets": 1,
            "out_late_collision": 0,
            "out_lost_carrier": 0,
            "out_mac_pause_frames": 0,
            "out_no_carrier": 0,
            "out_octets": 0,
            "out_pkts": 0,
            "out_underruns": 0,
            "out_unknown_protocl_drops": 0,
            "rate": {
                "in_rate": 0,
                "in_rate_pkts": 0,
                "load_interval": 300,
                "out_rate": 0,
                "out_rate_pkts": 0,
            },
        },
        "delay": 10,
        "duplex_mode": "full",
        "enabled": False,
        "encapsulations": {"encapsulation": "arpa"},
        "flow_control": {"receive": False, "send": False},
        "last_input": "never",
        "last_output": "never",
        "line_protocol": "down",
        "link_type": "force-up",
        "media_type": "unknown",
        "port_speed": "10000mbps",
        "mac_address": "2c33.11ff.311f",
        "mtu": 1500,
        "oper_status": "down",
        "output_hang": "never",
        "phys_address": "2c33.11ff.311f",
        "port_channel": {"port_channel_member": False},
        "queues": {
            "input_queue_drops": 0,
            "input_queue_flushes": 0,
            "input_queue_max": 375,
            "input_queue_size": 0,
            "output_queue_max": 40,
            "output_queue_size": 0,
            "queue_strategy": "fifo",
            "total_output_drop": 0,
        },
        "reliability": "255/255",
        "rxload": "1/255",
        "txload": "1/255",
        "type": "BUILT-IN-EPA-8x10G",
    },
    "Tunnel1754": {
        "bandwidth": 20000,
        "counters": {
            "in_abort": 0,
            "in_broadcast_pkts": 0,
            "in_crc_errors": 0,
            "in_errors": 0,
            "in_frame": 0,
            "in_giants": 0,
            "in_ignored": 0,
            "in_multicast_pkts": 0,
            "in_no_buffer": 0,
            "in_octets": 2633533316,
            "in_overrun": 0,
            "in_pkts": 7105513,
            "in_runts": 0,
            "in_throttles": 0,
            "last_clear": "25w2d",
            "out_buffer_failure": 0,
            "out_buffers_swapped": 0,
            "out_collision": 0,
            "out_errors": 0,
            "out_interface_resets": 0,
            "out_octets": 409215038,
            "out_pkts": 3442669,
            "out_underruns": 0,
            "out_unknown_protocl_drops": 0,
            "rate": {
                "in_rate": 0,
                "in_rate_pkts": 0,
                "load_interval": 300,
                "out_rate": 0,
                "out_rate_pkts": 0,
            },
        },
        "delay": 20000,
        "description": "*** PXMS TUNNEL FGTB-Hornu - CID 102338277687",
        "enabled": True,
        "encapsulations": {"encapsulation": "tunnel"},
        "ipv4": {"10.210.226.13/30": {"ip": "10.210.226.13", "prefix_length": "30"}},
        "last_input": "never",
        "last_output": "never",
        "line_protocol": "up",
        "mtu": 9976,
        "oper_status": "up",
        "output_hang": "never",
        "port_channel": {"port_channel_member": False},
        "queues": {
            "input_queue_drops": 0,
            "input_queue_flushes": 0,
            "input_queue_max": 375,
            "input_queue_size": 0,
            "output_queue_max": 0,
            "output_queue_size": 0,
            "queue_strategy": "fifo",
            "total_output_drop": 0,
        },
        "reliability": "255/255",
        "rxload": "1/255",
        "txload": "1/255",
        "type": "Tunnel",
    },
}
