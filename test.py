badE = {'u1': 1, 'u3': 1, 'u5': 1, 'u7': 1, 'd1': 1, 'd3': 0, 'd5': 0, 'd7': 0, 'f3': 0, 'f5': 0, 'b3': 0, 'b5': 1}

bad = [k for k, v in badE.items() if v == 1]
print([k[0] for k in bad].count("f"))