import subprocess,sys
from pathlib import Path
for p in sorted(Path('.').glob('Q*/Implementation_Code/*.py')):
 print('\n###',p);subprocess.run([sys.executable,str(p)],check=True)
