#!/usr/bin/python3
######################### BISMI ALLAH ##################################### Coding like a PRO! ###############################
import sys, time, subprocess
hex_vals = '0123456789ABCDEF'
def part_1(hex_val, power):
    dec_val = 0
    try:
        for i in range(0,len(hex_val)):
            power -= 1
            for j in range(0,len(hex_vals)):
                if hex_val[i] == hex_vals[j]:
                   dec_val += j * 16**(power)
    except IndexError:pass
    return dec_val
def part_2(hex_val, power):
    dec_val = 0
    try:
        for i in range(0,len(hex_val)):
            power -= 1
            for j in range(0,len(hex_vals)):
                if hex_val[i] == hex_vals[j]:
                   dec_val += j * 16**(power)
    except IndexError:pass
    return dec_val
while True:
      try:
          hex_val, clear, fractional_part, = "", False,''
          hex_val = input("[*] HEX: ")
          if not hex_val:continue
          f_part = False
          for i in range(len(hex_val)):
              if hex_val[i:i + 5] == 'clear':
                 clear = subprocess.Popen("clear", shell = True, stdin = subprocess.PIPE, stdout = subprocess.PIPE)
                 clear = clear.stdout.read()
                 clear = str(clear, 'utf-8')
                 print("{}".format(clear))
                 clear = True
                 break
              if hex_val[i:i + 4] in ("Exit",'exit','quit','Quit','q','Q'):
                 sys.exit(0)
              if hex_val[i] == '.' and not f_part:
                 fractional_part = hex_val[i + 1:].upper()
                 f_part = True
          if clear: continue
          hex_val = hex_val.upper()
          problem = False
          for k in range(len(hex_val)):
              if hex_val[k] == '.':continue
              problem_ = True
              for h in range(len(hex_vals)):
                  if hex_val[k] == hex_vals[h]:
                     problem_ = False
                     break
              if problem_:
                  print("[!] Invalide Hexadecimal value.")
                  problem = True
                  break
          if problem: continue
          if fractional_part:
             for i in range(len(fractional_part)):
                 if fractional_part[i] == '.':
                    print("[!] Invalide Hexadecimal value.")
                    problem = True
                    break
          if problem:continue
          intiger_part = ''
          for i in range(len(hex_val)):
              if hex_val[i] == '.':
                 break
              intiger_part += hex_val[i]
          intiger_part = part_1(intiger_part, len(intiger_part))
          fractional_part = part_2(fractional_part, 0)
          print("[+] Dec: %f" % (intiger_part + fractional_part))
      except KeyboardInterrupt:sys.stdout.write("\n")
################################################### Al hamdu liLAH ########################################################
