from setuptools import setup

setup(
    name='blurfilter',  # 应用名
    version='1.0',  # 版本号
    packages=['blurfilter'],
    install_requires=[  # 依赖列表
        'opencv-python'
    ]
)
