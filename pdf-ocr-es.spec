# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['pdf-ocr-es.py'],
             pathex=['D:\\onedrive\\OneDrive Consejería de Educación\\OneDrive - Consejería de Educación, Formación y Empleo\\GITHUB\\python\\PythonUtilidades\\PDF-ocr-es'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='pdf-ocr-es',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
