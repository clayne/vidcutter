#!/usr/bin/env python3
# -*- mode: python -*-

import os
import sys
import PyQt5

block_cipher = None

a = Analysis(['..\\..\\vidcutter\\__main__.py'],
             pathex=[
                 os.path.join(sys.modules['PyQt5'].__path__[0], 'Qt', 'bin'),
                 'C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\ucrt\\DLLs\\x64',
                 '..\\..'
             ],
             binaries=[],
             datas=[
                 ('..\\..\\vidcutter\\__init__.py', '.'),
                 ('..\\..\\CHANGELOG', '.'),
                 ('..\\..\\LICENSE', '.'),
                 ('..\\..\\README.md', '.'),
                 ('..\\..\\mpv-1.dll', '.'),
                 ('libmpv\\64\\mpv-1.dll', '.'),
                 ('..\\..\\bin\\*.*', 'bin')
                 # ('libmpv\\64\\d3dcompiler_43.dll', '.'),
                 # ('libmpv\\64\\d3dcompiler_47.dll', '.')
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['numpy'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='vidcutter',
          debug=False,
          strip=False,
          upx=False,
          console=False , icon='..\\..\\data\\icons\\vidcutter.ico')
