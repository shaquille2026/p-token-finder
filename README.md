# p-token-finder

## Overview
Blockchain analysis tool to identify the **first legitimate p-token deployed on Solana mainnet** post-activation.

## The Finding
**SPL Token** is verified as the **FIRST real p-token token** ever minted on Solana.

**Token Address:** `9KDvApw8gAUSYEzrQLi23qSggMZKRwV99nxu877zYPdV`  
**Created:** May 14, 2026 at 15:55:57 UTC  
**Slot:** 419,717,951  
**Creator:** `F3FjaJfcyp1igqKrqVaR8njASNt96xVEz2HFDAZx7umg`

## Evidence
✅ **BATCH instruction** (p-token exclusive feature)  
✅ **652 compute units** (96% reduction vs old SPL Token)  
✅ **RR discriminator** in raw transaction data  
✅ Created within 24 hours of p-token mainnet activation  

## Methodology
- Searched all blockchain slots: **419,472,000 → 419,717,951**
- Range: p-token program activation (May 13) to SPL Token creation (May 14)
- Used Alchemy RPC API for blockchain queries
- Result: **0 earlier p-token mints detected**

All previous "first p-token" claims lacked these technical signatures—they were LARPs on the old SPL Token program.

## Usage
```bash
pip install requests
python find_first_ptoken.py
```

## Verification
🔗 **View on Solscan:** https://solscan.io/token/9KDvApw8gAUSYEzrQLi23qSggMZKRwV99nxu877zYPdV

## Technical Details
- **Program:** Solana p-token (ptokFJwJTrVCa9Kqo9x0b559V40ccBGEaRFnBPndP)
- **Implementation:** Python with requests library
- **RPC Provider:** Alchemy API

## Methodology Note
The script uses Alchemy RPC and searches for `initializeMint` instructions 
in the P-Token program's transaction history. This approach identifies mint 
creations through the primary method, though alternative creation paths may exist.

**Verification:** Findings are also independently verified through manual 
Solscan analysis of transaction signatures and technical features:
- BATCH instruction presence (P-Token exclusive)
- Compute unit consumption (652 CUs vs 4,645 old SPL)
- RR discriminator in raw transaction data

Combined methodology strengthens confidence in the result.

## Community Discussion & Engagement

**Follow the research thread on X/Twitter:**

1. **Main Finding:** https://x.com/rektprince369/status/2055255937913405745
2. **Script Verification:** https://x.com/rektprince369/status/2055292489360138545
3. **Additional Analysis:** https://x.com/rektprince369/status/2055314572198736098

**Join the X Community:** https://x.com/i/communities/1970995210541728208

For questions, feedback, or evidence of earlier p-token deployments, 
engage in the threads above or join the community discussion.

**Follow @rektprince369 for updates on p-token research.**
