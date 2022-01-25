expected_output = {
    "switch": {
        "stack": {
            "1": {
                "role": "Active",
                "hw_ver": "V04",
                "state": "Ready",
                "priority": "3",
                "mac_address": "689c.e2ff.b9d9",
            },
            "3": {
                "role": "Member",
                "hw_ver": "V05",
                "state": "Ready",
                "priority": "1",
                "mac_address": "c800.84ff.4800",
            },
            "2": {
                "role": "Standby",
                "hw_ver": "V05",
                "state": "Ready",
                "priority": "2",
                "mac_address": "c800.84ff.7e00",
            },
            "4": {
                "role": "Member",
                "hw_ver": "0",
                "state": "V-Mismatch",
                "priority": "15",
                "mac_address": "00cc.fcff.7b00",
            },
        },
        "mac_address": "689c.e2ff.b9d9",
        "mac_persistency_wait_time": "Indefinite",
    }
}