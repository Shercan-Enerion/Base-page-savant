from yaml import safe_load
from config.bd import dataBase
dicti = {30: 'Grid',
         31: 'Grid',
         32: 'Grid',
         88: 'Inverter',
         33: 'Inverter',
         34: 'Inverter',
         35: 'Inverter',
         36: 'Load',
         37: 'Load',
         38: 'Grid',
         39: 'Grid',
         89: 'Grid',
         90: 'Grid',
         40: 'Inverter',
         41: 'Inverter',
         42: 'Generator',
         43: 'Grid',
         44: 'Grid',
         45: 'Grid',
         91: 'Grid',
         92: 'Grid',
         46: 'Grid',
         47: 'Inverter',
         48: 'Inverter',
         49: 'Inverter',
         50: 'Load',
         51: 'Load',
         52: 'Load',
         53: 'Load',
         54: 'Load',
         55: 'Generator',
         56: 'Battery',
         57: 'Battery',
         58: 'Battery',
         59: 'PV',
         60: 'PV',
         61: 'Battery',
         62: 'Battery',
         63: 'Load',
         64: 'Inverter',
         65: 'Grid',
         93: 'Generator',
         66: 'Generator',
         94: 'Configuration',
         95: 'Configuration',
         96: 'Configuration',
         97: 'Configuration',
         98: 'Configuration',
         99: 'Configuration',
         100: 'Configuration',
         101: 'Configuration',
         102: 'Configuration',
         103: 'Configuration',
         104: 'Configuration',
         105: 'Configuration',
         107: 'Configuration',
         108: 'Configuration',
         109: 'Configuration',
         110: 'Configuration',
         111: 'Configuration',
         112: 'Configuration',
         113: 'Configuration',
         114: 'Configuration',
         115: 'Configuration',
         116: 'Configuration',
         117: 'Configuration',
         118: 'Configuration',
         119: 'Configuration',
         120: 'Configuration',
         121: 'Configuration',
         122: 'Configuration',
         123: 'Configuration',
         124: 'Configuration',
         125: 'Configuration',
         126: 'Configuration',
         127: 'Configuration',
         128: 'Configuration',
         129: 'Configuration',
         130: 'Configuration',
         131: 'Configuration',
         132: 'Configuration',
         133: 'Configuration',
         135: 'Configuration',
         136: 'Configuration',
         29: 'Configuration',
         0: 'Configuration',
         137: 'Configuration',
         1: 'Configuration',
         2: 'Configuration',
         3: 'Configuration',
         4: 'Configuration',
         8: 'Configuration',
         12: 'Configuration',
         16: 'Configuration',
         20: 'Configuration',
         24: 'Configuration',
         5: 'Configuration',
         9: 'Configuration',
         13: 'Configuration',
         17: 'Configuration',
         21: 'Configuration',
         25: 'Configuration',
         139: 'Configuration',
         140: 'Configuration',
         141: 'Configuration',
         142: 'Configuration',
         143: 'Configuration',
         144: 'Configuration',
         6: 'Configuration',
         10: 'Configuration',
         14: 'Configuration',
         18: 'Configuration',
         22: 'Configuration',
         26: 'Configuration',
         7: 'Configuration',
         11: 'Configuration',
         15: 'Configuration',
         19: 'Configuration',
         23: 'Configuration',
         27: 'Configuration',
         145: 'Configuration',
         146: 'Configuration',
         147: 'Configuration',
         148: 'Configuration',
         149: 'Configuration',
         150: 'Configuration',
         151: 'Configuration',
         152: 'Configuration',
         153: 'Configuration',
         154: 'Configuration',
         155: 'Configuration',
         156: 'Configuration',
         157: 'Configuration',
         158: 'Configuration',
         28: 'Configuration',
         159: 'Configuration',
         106: 'Empty',
         134: 'Empty',
         138: 'Empty',
         }
with open('settings_clinet.yml', 'r',  encoding='utf8') as file:
    pr = safe_load(file)
valores = set(dicti.values())
diccion = {}
lista = []
for i in valores:
    lista.clear()
    for j in pr['data']:
        if dicti[j['register']] == i:
            lista.append(j['name'])
        diccion[i] = lista.copy()
dataBase.sendData(diccion)