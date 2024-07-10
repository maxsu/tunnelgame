# -*- mode: python ; coding: utf-8 -*-

import sys

match sys.platform:
    case 'linux':
        name ='tunnelgame.sh'
    case 'darwin':
        name='tunnelgame.app'
    case 'win32':
        name='tunnelgame.exe'

a = Analysis(
    ['src/tunnelgame/__main__.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('src/tunnelgame/grammar.yaml', 'tunnelgame'),
        ('src/tunnelgame/stories', 'tunnelgame/stories'),
        ('src/tunnelgame/saves', 'tunnelgame/saves')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name=name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
