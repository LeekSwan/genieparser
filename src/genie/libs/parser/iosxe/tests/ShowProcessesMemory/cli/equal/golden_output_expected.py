expected_output = {
    "system_memory": {
        "lsmpi_io_pool": {"free": 832, "total": 6295128, "used": 6294296},
        "process": {
                "*Dead*": {
                    "allocated": 2675774192,
                    "freed": 2559881512,
                    "getbufs": 2111,
                    "holding": 43465512,
                    "pid": 0,
                    "retbufs": 351,
                    "tty": 0
                },
                "*Init*": {
                    "allocated": 678985440,
                    "freed": 347855496,
                    "getbufs": 428,
                    "holding": 304892096,
                    "pid": 0,
                    "retbufs": 2134314,
                    "tty": 0
                },
                "*MallocLite*": {
                    "allocated": 0,
                    "freed": 0,
                    "getbufs": 0,
                    "holding": 4070880,
                    "pid": 0,
                    "retbufs": 0,
                    "tty": 0
                },
                "*Sched*": {
                    "allocated": 800,
                    "freed": 4965889216,
                    "getbufs": 17,
                    "holding": 800,
                    "pid": 0,
                    "retbufs": 17,
                    "tty": 0
                },
                "Chunk Manager": {
                    "allocated": 3415536,
                    "freed": 879912,
                    "getbufs": 0,
                    "holding": 2565568,
                    "pid": 1,
                    "retbufs": 0,
                    "tty": 0
                },
            },
        "processor_pool": {"free": 9662451880, "total": 10147887840, "used": 485435960},
        "reserve_p_pool": {"free": 102316, "total": 102404, "used": 88},
    }
}