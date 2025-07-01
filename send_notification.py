import requests
import os
from datetime import datetime

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
    print("Telegram bot token or chat ID not found in environment variables.")
    exit(1)

def escape_markdown_v2(text):
    """Escapes special characters for Telegram MarkdownV2."""
    # List of special characters that need to be escaped
    special_chars = '_*[]()~`>#+-|=|{}.!'
    for char in special_chars:
        text = text.replace(char, '\\' + char)
    return text

DEPLOY_TIMESTAMP = datetime.now().strftime("%B %d, %Y at %I:%M:%S %p")

GITHUB_REPO_URL = os.environ.get('GITHUB_REPO_URL', 'https://github.com/Huawei123r/my_first_monad_project')

JOURNAL_ENTRY_RAW = f"""---
**Journal Entry: MyFirstToken (Core Token Standard)**

* **Project Name:** MyFirstToken
* **Category:** Core Token Standard
* **Network:** Monad Testnet
* **Deployment Timestamp:** {DEPLOY_TIMESTAMP}
* **GitHub Repository URL:** {GITHUB_REPO_URL}
* **Monad Explorer Contract URL(s):** https://testnet.monadexplorer.com/address/0x46E4cb3B7763a5819B94F18FB1B14fb9B5208790
* **Key Files Created:**
    * `contracts/MyFirstToken.sol`
    * `scripts/DeployMyFirstToken.s.sol`
* **Project Summary:** This project deploys a basic ERC-20 token named 'MyFirstToken' with the symbol 'MFT' and an initial supply of 1,000,000 tokens. It includes a minting function accessible only by the contract owner.
* **Technical Details:**
    * Solidity Version: 0.8.20
    * Framework Used: Foundry
    * Key Libraries: OpenZeppelin (ERC20, Ownable), forge-std
    * Interaction Instructions:
        1. Ensure you have Foundry installed and configured.
        2. Set up your environment variables (MONAD_RPC_URL, PRIVATE_KEY) in a `.env` file.
        3. To check the total supply:
           `cast call 0x46E4cb3B7763a5819B94F18FB1B14fb9B5208790 "totalSupply()(uint256)"`
        4. To check your balance:
           `cast call 0x46E4cb3B7763a5819B94F18FB1B14fb9B5208790 "balanceOf(address)(uint256)" YOUR_ADDRESS`
        5. To mint new tokens (only by owner):
           `cast send 0x46E4cb3B7763a5819B94F18FB1B14fb9B5208790 "mint(address,uint256)" RECIPIENT_ADDRESS AMOUNT --rpc-url https://testnet-rpc.monad.xyz --private-key YOUR_PRIVATE_KEY`
* **Verification Status:** Verified
* **Verification Command (if applicable):** `forge script scripts/DeployMyFirstToken.s.sol --rpc-url https://testnet-rpc.monad.xyz --private-key \$PRIVATE_KEY --broadcast --verify --verifier sourcify --verifier-url https://sourcify-api-monad.blockvision.org --chain-id 10143 --contracts contracts/MyFirstToken.sol -vvvv`
---"""

# Append to dev_journal.md
with open('/home/administrator/gemini/my_first_monad_project/dev_journal.md', 'a') as f:
    f.write(JOURNAL_ENTRY_RAW)

# Send Telegram notification
telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
payload = {
    'chat_id': TELEGRAM_CHAT_ID,
    'text': escape_markdown_v2(JOURNAL_ENTRY_RAW),
    'parse_mode': 'MarkdownV2' # Use MarkdownV2 for more robust parsing
}

try:
    response = requests.post(telegram_url, json=payload)
    response.raise_for_status()  # Raise an exception for HTTP errors
    print("Telegram notification sent successfully!")
except requests.exceptions.RequestException as e:
    print(f"Error sending Telegram notification: {e}")
    print(f"Response content: {response.text if response else 'N/A'}")