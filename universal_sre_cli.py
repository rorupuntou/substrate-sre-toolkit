#!/usr/bin/env python3
"""
Universal Substrate SRE CLI - v1.0.1
A bare-metal, agnostic control center for Substrate-based nodes.
"""
import argparse
import sys
from substrateinterface import SubstrateInterface
from substrateinterface.exceptions import SubstrateRequestException

def connect_node(rpc_url: str):
    print(f"[*] Estableciendo conexión bare-metal con: {rpc_url}")
    try:
        substrate = SubstrateInterface(url=rpc_url)
        
        # Parche SRE: Usamos llamadas RPC crudas. Esto ignora las actualizaciones 
        # de la librería de Python y le pega directo a la API del nodo.
        chain_name = substrate.rpc_request('system_chain', []).get('result', 'Desconocida')
        version = substrate.rpc_request('system_version', []).get('result', 'Desconocida')
        
        print(f"[+] Conexión exitosa. Red: {chain_name} | Core v{version}")
        return substrate
    except Exception as e:
        print(f"[-] Garrón: Falló la conexión al RPC. Error: {e}")
        sys.exit(1)

def fetch_telemetry(substrate):
    print("\n[*] Extrayendo telemetría de capa base...")
    try:
        # Extraemos el header del bloque actual
        block_header = substrate.get_block_header()
        block_num = block_header['header']['number']
        block_hash = substrate.get_block_hash(block_id=block_num)
        
        # Inyectamos una consulta RPC directa para ver la salud de los peers
        health = substrate.rpc_request('system_health', [])
        peers = health.get('result', {}).get('peers', 'N/A')
        is_syncing = health.get('result', {}).get('isSyncing', 'N/A')

        print("-" * 50)
        print(f" 📡 Sincronización     : {'Sincronizando...' if is_syncing else 'Al día (Synced)'}")
        print(f" 🔗 Peers Conectados   : {peers}")
        print(f" 📦 Altura del Bloque  : {block_num}")
        print(f" 🪪 Hash del Bloque    : {block_hash}")
        print("-" * 50)
        
    except SubstrateRequestException as e:
        print(f"[-] Error de lectura en la metadata de la red: {e}")

def main():
    parser = argparse.ArgumentParser(description="Universal Substrate SRE CLI - Control de Nodos Bare-Metal")
    parser.add_argument("--rpc", required=True, help="URL del WebSocket/HTTP (ej. wss://rpc.polkadot.io)")
    parser.add_argument("--telemetry", action="store_true", help="Extrae el estado actual del nodo y la red")
    
    args = parser.parse_args()

    # Punto de entrada agnóstico
    substrate = connect_node(args.rpc)
    
    if args.telemetry:
        fetch_telemetry(substrate)
    else:
        print("[!] No se especificó ninguna acción forense. Usá --telemetry para ver el estado.")

if __name__ == "__main__":
    main()
