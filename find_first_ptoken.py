import requests
import json

RPC_URL = "https://solana-mainnet.g.alchemy.com/v2/NntEa1hO3JPh3ewcOpAEt"
P_TOKEN_PROGRAM = "ptokFJwJTrVCa9Kqo9x0b559V40ccBGEaRFnBPndP"
START_SLOT = 419472000
END_SLOT = 419717951

def get_signatures_for_address(address, start_slot, end_slot):
    """Get all signatures for the P-Token program in slot range"""
    signatures = []
    before = None
    
    while True:
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getSignaturesForAddress",
            "params": [
                address,
                {
                    "limit": 1000,
                    "before": before
                }
            ]
        }
        
        response = requests.post(RPC_URL, json=payload)
        data = response.json()
        
        if "result" not in data or not data["result"]:
            break
        
        for sig_info in data["result"]:
            slot = sig_info.get("slot")
            if slot < START_SLOT:
                return signatures
            if slot <= END_SLOT:
                signatures.append(sig_info)
        
        before = data["result"][-1]["signature"]
    
    return signatures

def get_transaction(signature):
    """Get transaction details"""
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getTransaction",
        "params": [signature, "json"]
    }
    
    response = requests.post(RPC_URL, json=payload)
    return response.json().get("result")

def find_mint_creations(signatures):
    """Find mint creation transactions"""
    mints = []
    
    for sig_info in signatures:
        tx = get_transaction(sig_info["signature"])
        
        if not tx or "transaction" not in tx:
            continue
        
        # Check for InitializeMint instruction
        instructions = tx["transaction"]["message"]["instructions"]
        
        for idx, instruction in enumerate(instructions):
            if "parsed" in instruction and instruction["parsed"].get("type") == "initializeMint":
                mint_address = instruction["parsed"]["info"].get("mint")
                timestamp = tx.get("blockTime")
                slot = sig_info["slot"]
                
                mints.append({
                    "mint": mint_address,
                    "slot": slot,
                    "timestamp": timestamp,
                    "signature": sig_info["signature"]
                })
                break
    
    return mints

print("🔍 Searching for first P-Token mint...")
print(f"Slot range: {START_SLOT} → {END_SLOT}")
print()

signatures = get_signatures_for_address(P_TOKEN_PROGRAM, START_SLOT, END_SLOT)
print(f"Found {len(signatures)} transactions")

mints = find_mint_creations(signatures)
mints.sort(key=lambda x: x["slot"])

if mints:
    print("\n✅ FIRST P-TOKEN MINT FOUND:")
    print("=" * 60)
    first = mints[0]
    print(f"Mint Address: {first['mint']}")
    print(f"Slot: {first['slot']}")
    print(f"Timestamp: {first['timestamp']}")
    print(f"Signature: {first['signature']}")
    print(f"Solscan: https://solscan.io/tx/{first['signature']}")
    print("=" * 60)
    
    if len(mints) > 1:
        print(f"\nFound {len(mints)} total mints in this range")
else:
    print("❌ No mints found in this range")