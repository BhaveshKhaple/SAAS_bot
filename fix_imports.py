import os
import re

MODULE_MAPPING = {
    'database': 'src.database.database',
    'config': 'src.database.config',
    'bot': 'src.bot.bot',
    'seller_profile': 'src.seller.seller_profile',
    'seller_withdrawals': 'src.seller.seller_withdrawals',
    'account_seller': 'src.seller.account_seller',
    'buyer_menu': 'src.buyer.buyer_menu',
    'buyer_referral_program': 'src.buyer.buyer_referral_program',
    'buyer_referral_withdrawals': 'src.buyer.buyer_referral_withdrawals',
    'buy_plan': 'src.buyer.buy_plan',
    'deposit_menu': 'src.buyer.deposit_menu',
    'plan_management': 'src.buyer.plan_management',
    'reseller_panel': 'src.buyer.reseller_panel',
    'admin_controls': 'src.admin.admin_controls',
    'admin_reporting': 'src.admin.admin_reporting',
    'admin_rate_management': 'src.admin.admin_rate_management',
    'admin_deposit_management': 'src.admin.admin_deposit_management',
    'admin_reseller_management': 'src.admin.admin_reseller_management',
    'broadcast_admin': 'src.admin.broadcast_admin',
    'promo_code_management': 'src.admin.promo_code_management',
    'saas_admin_reports': 'src.admin.saas_admin_reports',
    'account_pool_manager': 'src.utils.account_pool_manager',
    'account_monitor_scheduler': 'src.utils.account_monitor_scheduler',
    'account_status_checker': 'src.utils.account_status_checker',
    'service_delivery_worker': 'src.utils.service_delivery_worker',
    'notification_system': 'src.bot.notification_system',
    'daily_report': 'src.bot.daily_report',
    'plan_expiry_handler': 'src.bot.plan_expiry_handler',
    'run_scheduler': 'src.bot.run_scheduler',
    'setup_admin': 'src.bot.setup_admin'
}

def fix_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    original = content
    
    for old_mod, new_mod in MODULE_MAPPING.items():
        content = re.sub(rf'\bfrom {old_mod} import\b', f'from {new_mod} import', content)
        content = re.sub(rf'\bimport {old_mod}\b', f'import {new_mod} as {old_mod}', content)
    
    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f'Fixed: {filepath}')
    return content != original

changed = 0
for root, dirs, files in os.walk('src'):
    for file in files:
        if file.endswith('.py'):
            if fix_file(os.path.join(root, file)):
                changed += 1

print(f'\nTotal files changed: {changed}')
