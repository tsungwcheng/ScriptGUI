# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\wcheng\\PycharmProjects\\ScriptGUI', 'C:\\Python27\\libs', 'C:\\Python27\\Lib\\site-packages','C:\\Python34\\Lib\\site-packages', 'C:\\Python33\\libs', 'C:\\Python33\\Lib\\site-packages'],
             binaries=[],
             datas=[],
             hiddenimports=['serial.win32'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main')