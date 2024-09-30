# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py','utils\\file_utils.py','utils\\package_utils.py','utils\\string_utils.py'
    ,'template\\serviceimpl.py','template\\service.py','template\\mapper.py','template\\eneity.py','template\\controller.py'
    ,'db\\get_database_desc.py'],
    pathex=['JavaCodeGenerate'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['SpingBootSimpleTemplate'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='codegenerate',
)
