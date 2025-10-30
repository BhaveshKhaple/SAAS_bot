import asyncio
import logging
from telegram import Bot
from database import Database
from config import BOT_TOKEN, ADMIN_IDS
from datetime import datetime

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

db = Database()

async def send_daily_report():
    if not BOT_TOKEN or not ADMIN_IDS:
        logger.error("BOT_TOKEN or ADMIN_IDS not configured")
        return
    
    try:
        bot = Bot(token=BOT_TOKEN)
        
        daily_stats = db.get_daily_stats()
        system_stats = db.get_system_stats()
        
        report_date = datetime.now().strftime('%Y-%m-%d')
        
        report_message = f"""
📊 **Daily Report - {report_date}**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**📈 Last 24 Hours:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👥 New Users: {daily_stats['new_users_24h']}
📱 New Accounts Sold: {daily_stats['new_accounts_24h']}
🚫 New Bans: {daily_stats['new_bans_24h']}
💸 New Withdrawal Requests: {daily_stats['new_withdrawals_24h']}
💰 Amount Withdrawn: ${daily_stats['withdrawn_24h']:.2f}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**📊 Overall System Stats:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👥 **Users:**
• Total: {system_stats['total_users']}
• Banned: {system_stats['banned_users']}

📱 **Accounts:**
• Total Sold: {system_stats['total_accounts_sold']}
• Active: {system_stats['active_accounts']}
• Banned: {system_stats['banned_accounts']}

💰 **Financials:**
• Current Seller Balances: ${system_stats['total_seller_balance']:.2f}
• Total Withdrawn: ${system_stats['total_withdrawn']:.2f}
• Total Referral Earnings: ${system_stats['total_referral_earnings']:.2f}

💸 **Withdrawals:**
• Pending: {system_stats['pending_withdrawals']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC
"""
        
        for admin_id in ADMIN_IDS:
            try:
                await bot.send_message(
                    chat_id=admin_id,
                    text=report_message,
                    parse_mode='Markdown'
                )
                logger.info(f"Daily report sent to admin {admin_id}")
            except Exception as e:
                logger.error(f"Failed to send report to admin {admin_id}: {e}")
        
        logger.info("Daily report process completed")
        
    except Exception as e:
        logger.error(f"Error generating daily report: {e}")

if __name__ == "__main__":
    asyncio.run(send_daily_report())
