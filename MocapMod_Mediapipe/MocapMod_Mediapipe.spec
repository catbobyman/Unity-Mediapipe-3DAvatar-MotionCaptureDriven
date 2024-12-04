# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas = [
    ('Models/*.task', 'Models'),  # 相对路径，确保打包 Models 文件夹的所有 .task 文件
    ('.venv/Lib/site-packages/mediapipe/modules/hand_landmark/hand_landmark_tracking_cpu.binarypb', 'mediapipe/modules/hand_landmark'),
    ('.venv/Lib/site-packages/mediapipe/modules/palm_detection/palm_detection_lite.tflite', 'mediapipe/modules/palm_detection'),
    ('.venv/Lib/site-packages/mediapipe/modules/hand_landmark/hand_landmark_lite.tflite', 'mediapipe/modules/hand_landmark'),
    ('.venv/Lib/site-packages/mediapipe/modules/hand_landmark/handedness.txt', 'mediapipe/modules/hand_landmark')
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
    [],
    exclude_binaries=True,
    name='MocapMod_Mediapipe',
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
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='MocapMod_Mediapipe',
)
