from setuptools import setup

setup(
    name="electrum-doged-server",
    version="0.9",
    scripts=['run_electrum_doged_server','electrum-doged-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumdogedserver':'src'
        },
    py_modules=[
        'electrumdogedserver.__init__',
        'electrumdogedserver.utils',
        'electrumdogedserver.storage',
        'electrumdogedserver.deserialize',
        'electrumdogedserver.networks',
        'electrumdogedserver.blockchain_processor',
        'electrumdogedserver.server_processor',
        'electrumdogedserver.processor',
        'electrumdogedserver.version',
        'electrumdogedserver.ircthread',
        'electrumdogedserver.stratum_tcp',
        'electrumdogedserver.stratum_http'
    ],
    description="DogecoinDark Electrum Server",
    author="sunerok",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/doged/electrum-doged-server/",
    long_description="""Server for the Electrum Lightweight DogecoinDark Wallet"""
)


