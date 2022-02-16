import re
import json
from genie.metaparser import MetaParser


# ====================
# Schema for:
#  * 'show controllers'
# ====================


class ShowControllersSchema(MetaParser):
    """show controllers"""

    schema = {
        'controllers':{
           'transmit': {
              'total_bytes': int, 
                'unicast_frames': int,
                'unicast_bytes': int, 
                'multicast_frames': int,      
                'multicast_bytes': int,    
                'broadcast_frames': int,     
                'broadcast_bytes': int,    
                'system_fcs_error_frames': int,  	
                'macunderrun_frames': int, 
                'pause_frames': int, 
                'cos_0_pause_frames' : int, 	    
                'cos_1_pause_frames': int,    	   
                'cos_2_pause_frames': int,    	   
                'cos_3_pause_frames': int,    	   
                'cos_4_pause_frames': int,    	   
                'cos_5_pause_frames': int,    	   
                'cos_6_pause_frames': int,    	   
                'cos_7_pause_frames': int,    	   
                'oam_frames': int,                             
                'minimum_size_frames': int,    	  
                '65_to_127_byte_frames': int,  	 
                '128_to_255_byte_frames': int,  	 
                '256_to_511_byte_frames' : int, 	 
                '512_to_1023_byte_frames': int, 	 
                '1024_to_1518_byte_frames': int, 	
                '1519_to_2047_byte_frames': int, 	
                '2048_to_4095_byte_frames': int, 	
                '4096_to_8191_byte_frames': int, 	
                '8192_to_16383_byte_frames': int, 
                '16384_to_32767_byte_frame': int, 
                '32768_byte_frames'  : int,  	  
                'late_collision_frames': int,   	 
                'excess_defer_frames'  : int,  	  
                'good_(1_coll)_frames' : int,     
                'good_(>1_coll)_frames' : int,  	 
                'deferred_frames'    : int,  	    
                'gold_frames_dropped' : int,   	  
                'gold_frames_truncated': int,   
                'gold_frames_successful': int, 
                '1_collision_frames' : int,  
                '2_collision_frames' : int,   
                '3_collision_frames' : int,  
                '4_collision_frames' : int,   
                '5_collision_frames' : int,  
                '6_collision_frames' : int,   
                '7_collision_frames' : int,   
                '8_collision_frames' : int,   
                '9_collision_frames' : int,  
                '10_collision_frames' : int,   
                '11_collision_frames': int,    
                '12_collision_frames' : int,   
                '13_collision_frames': int,    
                '14_collision_frames' : int,   
                '15_collision_frames'  : int,  
                'excess_collision_frames' : int, 
           },
           'receive': {
                'total_bytes': int, 
                'unicast_frames': int,
                'unicast_bytes': int, 
                'multicast_frames': int,      
                'multicast_bytes': int,    
                'broadcast_frames': int,     
                'broadcast_bytes': int,
                'ipgviolation_frames' :int,
                'macunderrun_frames': int, 
                'pause_frames': int, 
                'cos_0_pause_frames' : int, 	    
                'cos_1_pause_frames': int,    	   
                'cos_2_pause_frames': int,    	   
                'cos_3_pause_frames': int,    	   
                'cos_4_pause_frames': int,    	   
                'cos_5_pause_frames': int,    	   
                'cos_6_pause_frames': int,    	   
                'cos_7_pause_frames': int,
                'oamprocessed_frames': int,
                'oamdropped_frames': int,
                'minimum_size_frames': int,    	  
                '65_to_127_byte_frames': int,  	 
                '128_to_255_byte_frames': int,  	 
                '256_to_511_byte_frames' : int, 	 
                '512_to_1023_byte_frames': int, 	 
                '1024_to_1518_byte_frames': int, 	
                '1519_to_2047_byte_frames': int, 	
                '2048_to_4095_byte_frames': int, 	
                '4096_to_8191_byte_frames': int, 	
                '8192_to_16383_byte_frames': int, 
                '16384_to_32767_byte_frame': int, 
                '32768_byte_frames'  : int,  	 
                'symbolerr_frames': int, 
                'collision_fragments': int,    
                'validundersize_frames': int, 
                'invalidoversize_frames': int, 
                'validoversize_frames': int, 
                'fcserr_frames': int, 
           }
        }
    }


# ====================
# Parser for:
#  * 'show processes memory'
# ====================
class showControllers(ShowControllersSchema):
    """show controllers"""
    
    cli_command = 'show controllers'
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output


        result_dict = {}

        p1 = re.compile(r'(?P<total_t>(\d+)) +Total +bytes \s+(?P<total_r>(\d+)) +Total +bytes')
        p2 = re.compile(r'(?P<unicast_frames_t>(\d+)) +Unicast +frames \s+(?P<unicast_frames_r>(\d+)) +Unicast +frames')
        p3 = re.compile(r'(?P<unicast_bytes_t>(\d+)) +Unicast +bytes \s+(?P<unicast_bytes_r>(\d+)) +Unicast +bytes')
        p4 = re.compile(r'(?P<multicast_frames_t>(\d+)) +Multicast +frames \s+(?P<multicast_frames_r>(\d+)) +Multicast +frames')
        p5 = re.compile(r'(?P<multicast_bytes_t>(\d+)) +Multicast +bytes \s+(?P<multicast_bytes_r>(\d+)) +Multicast +bytes')
        p6 = re.compile(r'(?P<broadcast_frames_t>(\d+)) +Broadcast +frames \s+(?P<broadcast_frames_r>(\d+)) +Broadcast +frames')
        p7 = re.compile(r'(?P<broadcast_bytes_t>(\d+)) +Broadcast +bytes \s+(?P<broadcast_bytes_r>(\d+)) +Broadcast +bytes')
        p8 = re.compile(r'(?P<system_fcs_error_frames>(\d+)) +System +FCS +error +frames \s+(?P<ipgviolation_frames>(\d+)) +IpgViolation +frames')
        p9 = re.compile(r'(?P<macunderrun_frames>(\d+)) +MacUnderrun +frames \s+(?P<macoverrun_frames>(\d+)) +MacOverrun +frames')
        p10 = re.compile(r'(?P<pause_frames_t>(\d+)) +Pause +frames \s+(?P<pause_frames_r>(\d+)) +Pause +frames')
        p11 = re.compile(r'(?P<cos_0_pause_frames_t>(\d+)) +Cos +0 +Pause +frames \s+(?P<cos_0_pause_frames_r>(\d+)) +Cos +0 +Pause +frames')
        p12 = re.compile(r'(?P<cos_1_pause_frames_t>(\d+)) +Cos +1 +Pause +frames \s+(?P<cos_1_pause_frames_r>(\d+)) +Cos +1 +Pause +frames')
        p13 = re.compile(r'(?P<cos_2_pause_frames_t>(\d+)) +Cos +2 +Pause +frames \s+(?P<cos_2_pause_frames_r>(\d+)) +Cos +2 +Pause +frames')
        p14 = re.compile(r'(?P<cos_3_pause_frames_t>(\d+)) +Cos +3 +Pause +frames \s+(?P<cos_3_pause_frames_r>(\d+)) +Cos +3 +Pause +frames')
        p15 = re.compile(r'(?P<cos_4_pause_frames_t>(\d+)) +Cos +4 +Pause +frames \s+(?P<cos_4_pause_frames_r>(\d+)) +Cos +4 +Pause +frames')
        p16 = re.compile(r'(?P<cos_5_pause_frames_t>(\d+)) +Cos +5 +Pause +frames \s+(?P<cos_5_pause_frames_r>(\d+)) +Cos +5 +Pause +frames')
        p17 = re.compile(r'(?P<cos_6_pause_frames_t>(\d+)) +Cos +6 +Pause +frames \s+(?P<cos_6_pause_frames_r>(\d+)) +Cos +6 +Pause +frames')
        p18 = re.compile(r'(?P<cos_7_pause_frames_t>(\d+)) +Cos +7 +Pause +frames \s+(?P<cos_7_pause_frames_r>(\d+)) +Cos +7 +Pause +frames')
        p19 = re.compile(r'(?P<oam_frames>(\d+)) +Oam +frames \s+(?P<oamprocessed_frames>(\d+)) +OamProcessed +frames')
        p20 = re.compile(r'(?P<oam_frames>(\d+)) +Oam frames \s+(?P<oamdropped_frames>(\d+)) +OamProcessed +frames')
        p21 = re.compile(r'(?P<minimum_size_frames_t>(\d+)) +Minimum +size +frames \s+(?P<minimum_size_frames_r>(\d+)) +Minimum +size +frames')
        p22 = re.compile(r'(?P<_65_to_127_byte_frames_t>(\d+)) +65 +to +127 +byte +frames \s+(?P<_65_to_127_byte_frames_r>(\d+)) +65 +to +127 +byte +frames')
        p23 = re.compile(r'(?P<_128_to_255_byte_frames_t>(\d+)) +128 +to +255 +byte +frames \s+(?P<_128_to_255_byte_frames_r>(\d+)) +128 to 255 +byte +frames')
        p24 = re.compile(r'(?P<_256_to_511_byte_frames_t>(\d+)) +256 +to +511 +byte +frames \s+(?P<_256_to_511_byte_frames_r>(\d+)) +256 +to +511 +byte +frames')
        p25 = re.compile(r'(?P<_512_to_1023_byte_frames_t>(\d+)) +512 +to +1023 +byte +frames \s+(?P<_512_to_1023_byte_frames_r>(\d+)) +512 +to +1023 +byte +frames')
        p26 = re.compile(r'(?P<_1024_to_1518_byte_frames_t>(\d+)) +1024 +to +1518 +byte +frames \s+(?P<_1024_to_1518_byte_frames_r>(\d+)) +1024 +to +1518 +byte +frames')
        p27 = re.compile(r'(?P<_1519_to_2047_byte_frames_t>(\d+)) +1519 +to +2047 +byte +frames \s+(?P<_1519_to_2047_byte_frames_r>(\d+)) +1519 +to +2047 +byte +frames')
        p28 = re.compile(r'(?P<_2048_to_4095_byte_frames_t>(\d+)) +2048 +to +4095 +byte +frames \s+(?P<_2048_to_4095_byte_frames_r>(\d+)) +2048 +to +4095 +byte +frames')
        p29 = re.compile(r'(?P<_4096_to_8191_byte_frames_t>(\d+)) +4096 +to +8191 +byte +frames \s+(?P<_4096_to_8191_byte_frames_r>(\d+)) +4096 +to +8191 +byte +frames')
        p30 = re.compile(r'(?P<_8192_to_16383_byte_frames_t>(\d+)) +8192 +to +16383 +byte +frames(\t+|\s+)(?P<_8192_to_16383_byte_frames_r>(\d+)) +8192 +to +16383 +byte +frames')
        p31 = re.compile(r'(?P<_16384_to_32767_byte_frames_t>(\d+)) +16384 +to +32767 +byte +frame(\t+|\s+)(?P<_16384_to_32767_byte_frames_r>(\d+)) +16384 +to +32767 +byte +frame')
        p32 = re.compile(r'(?P<_32768_byte_frames_t>(\d+)) +> +32768 +byte +frames \s+(?P<_32768_byte_frames_r>(\d+)) +> +32768 +byte +frames')
        p33 = re.compile(r'(?P<late_collision_frames>(\d+)) +Late +collision +frames \s+(?P<symbolerr_frames>(\d+)) +SymbolErr +frames')
        p34 = re.compile(r'(?P<excess_defer_frames>(\d+)) +Excess +Defer +frames \s+(?P<collision_fragments>(\d+)) +Collision +fragments')
        p35 = re.compile(r'(?P<good_1_coll_frames>(\d+)) +Good +\(1 +coll\) +frames \s+(?P<validundersize_frames>(\d+)) +ValidUnderSize +frames')
        p36 = re.compile(r'(?P<good_greater_1_coll_frames>(\d+)) +Good +\(>1 +coll\) +frames \s+(?P<invalidoversize_frames>(\d+)) +InvalidOverSize +frames')
        p37 = re.compile(r'(?P<deferred_frames>(\d+)) +Deferred +frames \s+(?P<validoversize_frames>(\d+)) +ValidOverSize +frames')
        p38 = re.compile(r'(?P<gold_frames_dropped>(\d+)) +Gold +frames +dropped \s+(?P<fcserr_frames>(\d+)) +FcsErr +frames')
        p39 = re.compile(r'(?P<gold_frames_truncated>(\d+)) +Gold +frames +truncated')
        p40 = re.compile(r'(?P<gold_frames_successful>(\d+)) +Gold +frames +successful')
        p41 = re.compile(r'(?P<_1_collision_frames>(\d+)) +1 +collision +frames')
        p42 = re.compile(r'(?P<_2_collision_frames>(\d+)) +2 +collision +frames')
        p43 = re.compile(r'(?P<_3_collision_frames>(\d+)) +3 +collision +frames')
        p44 = re.compile(r'(?P<_4_collision_frames>(\d+)) +4 +collision +frames')
        p45 = re.compile(r'(?P<_5_collision_frames>(\d+)) +5 +collision +frames')
        p46 = re.compile(r'(?P<_6_collision_frames>(\d+)) +6 +collision +frames')
        p47 = re.compile(r'(?P<_7_collision_frames>(\d+)) +7 +collision +frames')
        p48 = re.compile(r'(?P<_8_collision_frames>(\d+)) +8 +collision +frames')
        p49 = re.compile(r'(?P<_9_collision_frames>(\d+)) +9 +collision +frames')
        p50 = re.compile(r'(?P<_10_collision_frames>(\d+)) +10 +collision +frames')
        p51 = re.compile(r'(?P<_11_collision_frames>(\d+)) +11 +collision +frames')
        p52 = re.compile(r'(?P<_12_collision_frames>(\d+)) +12 +collision +frames')
        p53 = re.compile(r'(?P<_13_collision_frames>(\d+)) +13 +collision +frames')
        p54 = re.compile(r'(?P<_14_collision_frames>(\d+)) +14 +collision +frames')
        p55 = re.compile(r'(?P<_15_collision_frames>(\d+)) +15 +collision +frames')
        p56 = re.compile(r'(?P<excess_collision_frames>(\d+)) +Excess +collision +frames')



        for line in out.splitlines():
            line = line.strip()
            controller_dict = result_dict.setdefault('controllers', {})
            transmit_dict = controller_dict.setdefault('transmit', {})
            receive_dict = controller_dict.setdefault('receive', {})
            
            m = p1.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['total_bytes'] = int(group['total_t'])
                receive_dict['total_bytes'] = int(group['total_r'])
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['unicast_frames'] = int(group['unicast_frames_t'])
                receive_dict['unicast_frames'] = int(group['unicast_frames_r'])
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['unicast_bytes'] = int(group['unicast_bytes_t'])
                receive_dict['unicast_bytes'] = int(group['unicast_bytes_r'])
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['multicast_frames'] = int(group['multicast_frames_t'])
                receive_dict['multicast_frames'] = int(group['multicast_frames_r'])
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['multicast_bytes'] = int(group['multicast_bytes_t'])
                receive_dict['multicast_bytes_t'] = int(group['multicast_bytes_r'])
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['broadcast_frames'] = int(group['broadcast_frames_t'])
                receive_dict['broadcast_frames'] = int(group['broadcast_frames_r'])
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['broadcast_bytes'] = int(group['broadcast_bytes_t'])
                receive_dict['broadcast_bytes'] = int(group['broadcast_bytes_r'])
                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['system_fcs_error_frames'] = int(group['system_fcs_error_frames'])
                receive_dict['ipgviolation_frames'] = int(group['ipgviolation_frames'])
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['macunderrun_frames'] = int(group['macunderrun_frames'])
                receive_dict['macoverrun_frames'] = int(group['macoverrun_frames'])
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['pause_frames'] = int(group['pause_frames_t'])
                receive_dict['pause_frames'] = int(group['pause_frames_r'])
                continue

            m = p11.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['cos_0_pause_frames'] = int(group['cos_0_pause_frames_t'])
                receive_dict['cos_0_pause_frames'] = int(group['cos_0_pause_frames_r'])
                continue

            m = p12.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['cos_1_pause_frames'] = int(group['cos_1_pause_frames_t'])
                receive_dict['cos_1_pause_frames'] = int(group['cos_1_pause_frames_r'])
                continue

            m = p13.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['cos_2_pause_frames'] = int(group['cos_2_pause_frames_t'])
                receive_dict['cos_2_pause_frames'] = int(group['cos_2_pause_frames_r'])
                continue

            m = p14.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['cos_3_pause_frames'] = int(group['cos_3_pause_frames_t'])
                receive_dict['cos_3_pause_frames'] = int(group['cos_3_pause_frames_r'])
                continue

            m = p15.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['cos_4_pause_frames'] = int(group['cos_4_pause_frames_t'])
                receive_dict['cos_4_pause_frames'] = int(group['cos_4_pause_frames_r'])
                continue

            m = p16.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['cos_5_pause_frames'] = int(group['cos_5_pause_frames_t'])
                receive_dict['cos_5_pause_frames'] = int(group['cos_5_pause_frames_r'])
                continue

            m = p17.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['cos_6_pause_frames'] = int(group['cos_6_pause_frames_t'])
                receive_dict['cos_6_pause_frames'] = int(group['cos_6_pause_frames_r'])
                continue

            m = p18.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['cos_7_pause_frames'] = int(group['cos_7_pause_frames_t'])
                receive_dict['cos_7_pause_frames'] = int(group['cos_7_pause_frames_r'])
                continue

            m = p19.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['oam_frames'] = int(group['oam_frames'])
                receive_dict['oamprocessed_frames'] = int(group['oamprocessed_frames'])
                continue

            m = p20.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['oam_frames'] = int(group['oam_frames'])
                receive_dict['oamdropped_frames'] = int(group['oamdropped_frames'])
                continue

            m = p21.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['minimum_size_frames'] = int(group['minimum_size_frames_t'])
                receive_dict['minimum_size_frames'] = int(group['minimum_size_frames_r'])
                continue

            m = p22.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['65_to_127_byte_frames'] = int(group['_65_to_127_byte_frames_t'])
                receive_dict['65_to_127_byte_frames'] = int(group['_65_to_127_byte_frames_r'])
                continue

            m = p23.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['128_to_255_byte_frames'] = int(group['_128_to_255_byte_frames_t'])
                receive_dict['128_to_255_byte_frames'] = int(group['_128_to_255_byte_frames_r'])
                continue


            m = p24.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['256_to_511_byte_frames'] = int(group['_256_to_511_byte_frames_t'])
                receive_dict['256_to_511_byte_frames'] = int(group['_256_to_511_byte_frames_r'])
                continue

            m = p25.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['512_to_1023_byte_frames'] = int(group['_512_to_1023_byte_frames_t'])
                receive_dict['512_to_1023_byte_frames'] = int(group['_512_to_1023_byte_frames_r'])
                continue

            m = p26.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['1024_to_1518_byte_frames'] = int(group['_1024_to_1518_byte_frames_t'])
                receive_dict['1024_to_1518_byte_frames'] = int(group['_1024_to_1518_byte_frames_r'])
                continue

            m = p27.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['1519_to_2047_byte_frames'] = int(group['_1519_to_2047_byte_frames_t'])
                receive_dict['1519_to_2047_byte_frames'] = int(group['_1519_to_2047_byte_frames_r'])
                continue

            m = p28.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['2048_to_4095_byte_frames'] = int(group['_2048_to_4095_byte_frames_t'])
                receive_dict['2048_to_4095_byte_frames'] = int(group['_2048_to_4095_byte_frames_r'])
                continue

            m = p29.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['4096_to_8191_byte_frames'] = int(group['_4096_to_8191_byte_frames_t'])
                receive_dict['4096_to_8191_byte_frames'] = int(group['_4096_to_8191_byte_frames_r'])
                continue

            m = p30.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['8192_to_16383_byte_frames'] = int(group['_8192_to_16383_byte_frames_t'])
                receive_dict['8192_to_16383_byte_frames'] = int(group['_8192_to_16383_byte_frames_r'])
                continue

            m = p31.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['16384_to_32767_byte_frame'] = int(group['_16384_to_32767_byte_frames_t'])
                receive_dict['16384_to_32767_byte_frame'] = int(group['_16384_to_32767_byte_frames_r'])
                continue

            m = p32.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['32768_byte_frames'] = int(group['_32768_byte_frames_t'])
                receive_dict['32768_byte_frames'] = int(group['_32768_byte_frames_r'])
                continue

            m = p33.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['late_collision_frames'] = int(group['late_collision_frames'])
                receive_dict['symbolerr_frames'] = int(group['symbolerr_frames'])
                continue

            m = p34.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['excess_defer_frames'] = int(group['excess_defer_frames'])
                receive_dict['collision_fragments'] = int(group['collision_fragments'])
                continue

            m = p35.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['good_(1_coll)_frames'] = int(group['good_1_coll_frames'])
                receive_dict['validundersize_frames'] = int(group['validundersize_frames'])
                continue

            m = p36.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['good_(>1_coll)_frames'] = int(group['good_greater_1_coll_frames'])
                receive_dict['invalidoversize_frames'] = int(group['invalidoversize_frames'])
                continue

            m = p37.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['deferred_frames'] = int(group['deferred_frames'])
                receive_dict['validoversize_frames'] = int(group['validoversize_frames'])
                continue

            m = p38.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['gold_frames_dropped'] = int(group['gold_frames_dropped'])
                receive_dict['fcserr_frames'] = int(group['fcserr_frames'])
                continue

            m = p39.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['gold_frames_truncated'] = int(group['gold_frames_truncated'])
                continue

            m = p40.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['gold_frames_successful'] = int(group['gold_frames_successful'])
                continue

            m = p41.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['1_collision_frames'] = int(group['_1_collision_frames'])
                continue

            m = p42.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['2_collision_frames'] = int(group['_2_collision_frames'])
                continue

            m = p43.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['3_collision_frames'] = int(group['_3_collision_frames'])
                continue

            m = p44.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['4_collision_frames'] = int(group['_4_collision_frames'])
                continue

            m = p45.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['5_collision_frames'] = int(group['_5_collision_frames'])
                continue

            m = p46.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['6_collision_frames'] = int(group['_6_collision_frames'])
                continue

            m = p47.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['7_collision_frames'] = int(group['_7_collision_frames'])
                continue

            m = p48.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['8_collision_frames'] = int(group['_8_collision_frames'])
                continue

            m = p49.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['9_collision_frames'] = int(group['_9_collision_frames'])
                continue

            m = p50.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['10_collision_frames'] = int(group['_10_collision_frames'])
                continue

            m = p51.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['11_collision_frames'] = int(group['_11_collision_frames'])
                continue

            m = p52.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['12_collision_frames'] = int(group['_12_collision_frames'])
                continue

            m = p53.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['13_collision_frames'] = int(group['_13_collision_frames'])
                continue

            m = p54.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['14_collision_frames'] = int(group['_14_collision_frames'])
                continue

            m = p55.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['15_collision_frames'] = int(group['_15_collision_frames'])
                continue

            m = p56.match(line)
            if m:
                group = m.groupdict()
                transmit_dict['excess_collision_frames'] = int(group['excess_collision_frames'])
                continue

        return result_dict
