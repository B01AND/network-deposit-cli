from typing import Dict, NamedTuple


DEPOSIT_CLI_VERSION = '1.2.5-LUKSO'


class BaseChainSetting(NamedTuple):
    ETH2_NETWORK_NAME: str
    GENESIS_FORK_VERSION: bytes


MAINNET = 'mainnet'
PYRMONT = 'pyrmont'
PRATER = 'prater'
L15_DEV = 'l15-dev'
L15_STAGING = 'l15-staging'
L15_PROD = 'l15-prod'


# Eth2 Mainnet setting
MainnetSetting = BaseChainSetting(ETH2_NETWORK_NAME=MAINNET, GENESIS_FORK_VERSION=bytes.fromhex('00000000'))
# Eth2 pre-launch testnet (spec v1.0.0)
PyrmontSetting = BaseChainSetting(ETH2_NETWORK_NAME=PYRMONT, GENESIS_FORK_VERSION=bytes.fromhex('00002009'))
# Eth2 testnet (spec v1.0.1)
PraterSetting = BaseChainSetting(ETH2_NETWORK_NAME=PRATER, GENESIS_FORK_VERSION=bytes.fromhex('00001020'))
# LUKSO l15 dev
L15DevSetting = BaseChainSetting(ETH2_NETWORK_NAME=L15_DEV, GENESIS_FORK_VERSION=bytes.fromhex('63a55317'))
# LUKSO l15 staging
L15StagingSetting = BaseChainSetting(ETH2_NETWORK_NAME=L15_STAGING, GENESIS_FORK_VERSION=bytes.fromhex('73a55317'))
# LUKSO l15 prod
L15ProdSetting = BaseChainSetting(ETH2_NETWORK_NAME=L15_PROD, GENESIS_FORK_VERSION=bytes.fromhex('83a55317'))


ALL_CHAINS: Dict[str, BaseChainSetting] = {
    MAINNET: MainnetSetting,
    PYRMONT: PyrmontSetting,
    PRATER: PraterSetting,
    L15_DEV: L15DevSetting,
    L15_STAGING: L15StagingSetting,
    L15_PROD: L15ProdSetting,
}


def get_chain_setting(chain_name: str = MAINNET) -> BaseChainSetting:
    return ALL_CHAINS[chain_name]
