from typing import Dict, NamedTuple


DEPOSIT_CLI_VERSION = '1.2.1-lukso'


class BaseChainSetting(NamedTuple):
    ETH2_NETWORK_NAME: str
    GENESIS_FORK_VERSION: bytes


MAINNET = 'mainnet'
PYRMONT = 'pyrmont'
PRATER = 'prater'
L15_LUKSO_DEV = 'l15-testnet-dev'
L15_LUKSO_STAGING = 'l15-testnet-staging'
L15_LUKSO_PROD = 'l15-testnet-prod'


# Eth2 Mainnet setting
MainnetSetting = BaseChainSetting(ETH2_NETWORK_NAME=MAINNET, GENESIS_FORK_VERSION=bytes.fromhex('00000000'))
# Eth2 pre-launch testnet (spec v1.0.0)
PyrmontSetting = BaseChainSetting(ETH2_NETWORK_NAME=PYRMONT, GENESIS_FORK_VERSION=bytes.fromhex('00002009'))
# Eth2 testnet (spec v1.0.1)
PraterSetting = BaseChainSetting(ETH2_NETWORK_NAME=PRATER, GENESIS_FORK_VERSION=bytes.fromhex('00001020'))
# LUKSO l15 testnet dev
LuksoDevSetting = BaseChainSetting(ETH2_NETWORK_NAME=L15_LUKSO_DEV, GENESIS_FORK_VERSION=bytes.fromhex('63a55317'))
# LUKSO l15 testnet staging
LuksoStagingSetting = BaseChainSetting(ETH2_NETWORK_NAME=L15_LUKSO_STAGING, GENESIS_FORK_VERSION=bytes.fromhex('73a55317'))
# LUKSO l15 testnet prod
LuksoProdSetting = BaseChainSetting(ETH2_NETWORK_NAME=L15_LUKSO_PROD, GENESIS_FORK_VERSION=bytes.fromhex('83a55317'))


ALL_CHAINS: Dict[str, BaseChainSetting] = {
    MAINNET: MainnetSetting,
    PYRMONT: PyrmontSetting,
    PRATER: PraterSetting,
    L15_LUKSO_DEV: LuksoDevSetting,
    L15_LUKSO_STAGING: LuksoStagingSetting,
    L15_LUKSO_PROD: LuksoProdSetting,
}


def get_chain_setting(chain_name: str = MAINNET) -> BaseChainSetting:
    return ALL_CHAINS[chain_name]
