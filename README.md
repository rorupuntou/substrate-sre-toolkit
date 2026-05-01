# Universal Substrate Bare-Metal SRE Toolkit

A lightweight, network-agnostic CLI suite for Substrate node operators and security researchers.

## Philosophy
- **Bare-Metal First:** Designed to run natively on Linux hosts (optimized for Arch Linux/CachyOS).
- **Zero-Container Policy:** No Docker, Kubernetes, or virtualization overhead.
- **Python Native:** Leveraging `substrate-interface` with direct RPC calls for maximum stability and performance.
- **Agnostic Architecture:** Dynamically adapts to any Substrate-based chain metadata upon handshake.

## Features
- **Node Telemetry:** Real-time extraction of peer count, block height, and synchronization status.
- **Agnostic Connection:** Connect to any Substrate RPC (Polkadot, Kusama, Parachains) using a single entry point.
- **Low Overhead:** Direct execution that leaves no resident processes or background daemons.

## Installation
Requires Python 3.10+.

```
# Clone the repository
git clone [https://github.com/rorupuntou/substrate-sre-toolkit.git](https://github.com/rorupuntou/substrate-sre-toolkit.git)
cd substrate-sre-toolkit

# Setup native environment
python -m venv .venv
source .venv/bin/activate.fish

# Install dependencies
pip install substrate-interface
