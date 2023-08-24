import subprocess

# Set lid close action on battery
subprocess.run(['powercfg', '-setdcvalueindex', 'SCHEME_CURRENT', 'SUB_BUTTONS_LIDACTION', '0'])
# Set lid close action when plugged in
subprocess.run(['powercfg', '-setacvalueindex', 'SCHEME_CURRENT', 'SUB_BUTTONS_LIDACTION', '0'])

# Set sleep timeout on battery to 30 minutes
subprocess.run(['powercfg', '-setdcvalueindex', 'SCHEME_CURRENT', 'SUB_SLEEP', '3'])
subprocess.run(['powercfg', '-setdcvalueindex', 'SCHEME_CURRENT', 'PERFBOOSTMODE', '0'])
subprocess.run(['powercfg', '-setdcvalueindex', 'SCHEME_CURRENT', 'PRESLEEP', '0'])
subprocess.run(['powercfg', '-setdcvalueindex', 'SCHEME_CURRENT', 'PRESLEEP', '0'])
subprocess.run(['powercfg', '-setdcvalueindex', 'SCHEME_CURRENT', 'VIDEOIDLE', '0'])
# Set sleep timeout when plugged in to "Never"
subprocess.run(['powercfg', '-setacvalueindex', 'SCHEME_CURRENT', 'SUB_SLEEP', '0'])

# Apply the power settings
subprocess.run(['powercfg', '-SetActive', 'SCHEME_CURRENT'])