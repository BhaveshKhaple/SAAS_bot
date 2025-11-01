# Telegram Marketplace Bot - Complete Testing Guide

## Prerequisites
- A Telegram account you can use for testing
- Access to the bot on Telegram (@YourBotUsername)
- A test phone number (ideally a secondary number for safety)
- Admin access (your user ID must be in ADMIN_IDS)

## Important Notes
⚠️ **CRITICAL**: When selling a Telegram account:
- **The verification code appears in your Telegram app**, not via SMS!
- Check the chat from "Telegram" (official) in your Telegram app
- The code usually arrives within 10-30 seconds
- If you don't see it after 2 minutes, check SMS as fallback

---

## Phase 1 Testing: Foundation & Core Bot Setup

### Test 1.1: Bot Initialization
1. Find your bot on Telegram
2. Send `/start` command
3. ✅ **Expected**: Welcome message appears with seller menu showing 6 buttons:
   - 💰 Sell TG Account
   - 💎 Buyer Menu
   - 💸 Withdraw
   - 👤 Profile
   - 🎁 Refer & Earn
   - 💬 Support

### Test 1.2: User Registration
1. Start bot with `/start`
2. Check that you're registered in the database
3. ✅ **Expected**: Bot remembers you on subsequent `/start` commands

### Test 1.3: Admin Authentication
**Note**: Only works if your user ID is in ADMIN_IDS secret
1. As admin, try admin commands: `/setprice 15.00`
2. ✅ **Expected**: Admin can execute commands
3. Try with non-admin account
4. ✅ **Expected**: Non-admin gets permission denied

---

## Phase 2 Testing: Account Selling Workflow

### Test 2.1: Phone Number Submission
1. Click **💰 Sell TG Account** button
2. Read the information message
3. Send a valid phone number in international format (e.g., `+1234567890`)
4. ✅ **Expected**: 
   - Message: "✅ Verification Code Sent!"
   - Instructions to check Telegram app
   - Bot asks for the 5-digit code

### Test 2.2: Invalid Phone Number Handling
1. Send an invalid phone number (e.g., `12345`)
2. ✅ **Expected**: Error message asking for correct format
3. Send a valid number to continue

### Test 2.3: OTP Verification (Without 2FA)
**IMPORTANT**: Use an account WITHOUT 2FA enabled for this test

1. After receiving "Code sent" message
2. **Open your Telegram app** and check the "Telegram" official chat
3. Copy the 5-digit code
4. Send the code to the bot
5. ✅ **Expected**:
   - "✅ Code verified successfully!"
   - Bot starts processing (3 steps shown)
   - Step 1: Terminating other sessions
   - Step 2: Setting up 2FA security
   - Step 3: Saving account to database
   - Button appears: "✅ I Have Logged Out"

### Test 2.4: Invalid OTP Code
1. During OTP step, send wrong code (e.g., `11111`)
2. ✅ **Expected**: Error message, can retry with correct code
3. Send correct code to continue

### Test 2.5: 2FA Password Verification
**IMPORTANT**: Use an account WITH 2FA enabled for this test

1. Follow phone number and OTP steps
2. After OTP verification
3. ✅ **Expected**: Bot asks for 2FA password
4. Send your 2FA password
5. ✅ **Expected**: Password verified, processing continues
6. Your password message should be deleted for security

### Test 2.6: Session Processing & Payment
1. After seeing "✅ I Have Logged Out" button
2. Verify you're logged out from other devices
3. Click the button
4. ✅ **Expected**:
   - Verification process runs
   - Success message with:
     - 💰 Payout amount
     - 📱 Account ID
     - 📞 Phone number
     - 💵 New balance
   - Returns to main menu

### Test 2.7: Cancellation
1. Start account selling process
2. At any step, send `/cancel`
3. ✅ **Expected**: Process cancelled, returns to main menu

### Test 2.8: Admin Price Control
**Admin only**
1. Send `/setprice 20.00`
2. ✅ **Expected**: Confirmation that price is updated
3. Start selling process again
4. ✅ **Expected**: New price shown in the initial message

---

## Phase 3 Testing: Seller Management & Payouts

### Test 3.1: Profile Section
1. Click **👤 Profile** button
2. ✅ **Expected**: Display shows:
   - Lifetime Earnings
   - Current Balance
   - Total Withdrawn
   - Accounts Sold
   - Banned Accounts
   - Referral Earnings
   - Payout Info (if set)
   - Option to set/update payout info

### Test 3.2: Set Payout Information
1. In Profile, click **💳 Set Payout Info**
2. Select payment method (e.g., UPI)
3. Enter payout details
4. ✅ **Expected**: Payout info saved and shown in profile

### Test 3.3: Withdrawal Request
1. Ensure you have balance > $0
2. Click **💸 Withdraw** button
3. Enter withdrawal amount (must be >= minimum limit)
4. ✅ **Expected**:
   - If valid: Withdrawal request created, admin notified
   - If invalid: Error message with requirements

### Test 3.4: Withdrawal Limits (Progressive)
1. Try first withdrawal with amount below $10
2. ✅ **Expected**: Error (minimum $10 for 1st withdrawal)
3. After 1st successful withdrawal, minimum should be $50
4. Test subsequent limits: $100, $500, $5000

### Test 3.5: Admin Withdrawal Management
**Admin only**
1. After user creates withdrawal request
2. Admin sends `/withdraws pending`
3. ✅ **Expected**: List of pending requests with inline buttons
4. Click a request to view details
5. ✅ **Expected**: User stats, amount, UPI info shown
6. Click **✅ Approve**
7. ✅ **Expected**: 
   - Status → approved
   - Amount deducted from user balance
   - User notified
   - Total withdrawn updated

### Test 3.6: Admin Withdrawal Rejection
1. Admin views pending withdrawal
2. Click **❌ Reject**
3. ✅ **Expected**: Status → rejected, user notified

### Test 3.7: Admin User Controls
**Admin only**
1. `/ban <username>` - Ban a user
2. ✅ **Expected**: User cannot sell accounts or withdraw
3. `/unban <username>` - Unban user
4. ✅ **Expected**: User can use bot normally again
5. `/stopwithdraw <username>` - Block withdrawals
6. ✅ **Expected**: User cannot create withdrawal requests
7. `/allowwithdraw <username>` - Allow withdrawals
8. ✅ **Expected**: User can withdraw again

---

## Phase 4 Testing: Referral System & Admin Reporting

### Test 4.1: Referral Link Generation
1. Click **🎁 Refer & Earn** button
2. ✅ **Expected**: 
   - Unique referral link shown
   - Explanation of commission
   - Current referral stats

### Test 4.2: Referral Signup
1. Copy referral link from User A's account
2. Send link to User B (in a different Telegram account)
3. User B clicks link and starts bot
4. ✅ **Expected**: User B is registered with User A as referrer

### Test 4.3: Referral Commission
1. User B (referred) sells an account
2. Check User A's profile
3. ✅ **Expected**: 
   - User A receives 10% commission (default)
   - Referral earnings updated
   - Balance increased

### Test 4.4: Admin Set Referral Rate
**Admin only**
1. Send `/setref 0.15` (15%)
2. ✅ **Expected**: Commission rate updated
3. Next referral sale should use new rate

### Test 4.5: Support Section
1. Click **💬 Support** button
2. ✅ **Expected**: Support information displayed

### Test 4.6: Admin User Statistics
**Admin only**
1. `/accsell @username` - View specific user stats
2. ✅ **Expected**: Detailed stats for that user
3. `/alluser` - List all users (page 1)
4. ✅ **Expected**: Paginated list with stats
5. Use navigation buttons to see more pages

### Test 4.7: Overall System Stats
**Admin only**
1. Send `/stats`
2. ✅ **Expected**: System-wide statistics:
   - Total users
   - Total accounts sold
   - Banned accounts
   - Total earnings distributed
   - Active accounts
   - And more

### Test 4.8: Daily Automated Report
**Admin only**
1. Wait for midnight (or manually trigger if possible)
2. ✅ **Expected**: 
   - Admin receives daily report
   - Shows 24-hour stats
   - Shows lifetime stats

---

## Phase 5 Testing: SaaS Foundation & Account Pool Manager

### Test 5.1: Buyer Menu Access
1. From main menu, click **💎 Buyer Menu**
2. ✅ **Expected**: Buyer menu shown with 7 buttons:
   - 💎 Buy Plan
   - 💰 Deposit
   - 📋 My Plans
   - 📊 Plan History
   - 🎁 Referral Program
   - 👔 Reseller Panel
   - 💬 Support

### Test 5.2: Buyer UI - Buy Plan
1. In Buyer menu, click **💎 Buy Plan**
2. ✅ **Expected**: Service pricing information shown
   - Per view rates
   - Per day view rates
   - Per reaction rates
   - Per day reaction rates

### Test 5.3: Buyer UI - Deposit
1. Click **💰 Deposit**
2. ✅ **Expected**: Instructions for adding funds shown

### Test 5.4: Buyer UI - My Plans
1. Click **📋 My Plans**
2. ✅ **Expected**: 
   - Shows active service orders
   - Or message if no active plans

### Test 5.5: Buyer UI - Plan History
1. Click **📊 Plan History**
2. ✅ **Expected**: Past orders history displayed

### Test 5.6: Buyer UI - Referral Program
1. Click **🎁 Referral Program**
2. ✅ **Expected**: Buyer-specific referral system info

### Test 5.7: Buyer UI - Reseller Panel
1. Click **👔 Reseller Panel**
2. ✅ **Expected**: Reseller management interface

### Test 5.8: Switch Between Seller/Buyer Menus
1. From Buyer menu, go back to Seller menu
2. From Seller menu, go to Buyer menu
3. ✅ **Expected**: Seamless navigation, balances displayed correctly

### Test 5.9: Admin Account Pool Manager
**Admin only**
1. Send `/accounts` command
2. ✅ **Expected**: 
   - List of all sold accounts
   - Status (Active, Banned, Full)
   - Join count for each
   - Pagination if many accounts

### Test 5.10: Add Account Manually
**Admin only**
1. Click **Add Account** button in account pool
2. Follow prompts to add session string
3. ✅ **Expected**: Account added to pool

### Test 5.11: Remove Account
**Admin only**
1. In account pool, select an account
2. Click **Remove** button
3. ✅ **Expected**: Account removed from pool

### Test 5.12: Account Status Checker
**Automated - Admin only**
1. Wait for scheduled check (every 6 hours)
2. OR manually run the checker if possible
3. ✅ **Expected**: 
   - All accounts checked for ban status
   - Database updated with current status
   - Admin notified of any changes

### Test 5.13: Low Pool Alert
**Automated - Admin only**
1. Ensure active accounts < 100
2. ✅ **Expected**: 
   - Admin receives low pool alert
   - Alert shows current count

---

## Common Issues & Troubleshooting

### Issue 1: "Not receiving verification code"
**Solution**: 
- ✅ Check the official "Telegram" chat in your Telegram app (NOT SMS!)
- Wait 2 minutes before assuming failure
- Ensure phone number is correct
- Check SMS as last resort

### Issue 2: "Session expired" error
**Solution**:
- Start the process again from the beginning
- Don't wait too long between steps

### Issue 3: "Invalid verification code"
**Solution**:
- Make sure you're entering the latest code
- Code must be 5 digits
- Don't include spaces or dashes

### Issue 4: "2FA password incorrect"
**Solution**:
- Ensure you're using the correct 2FA password
- Your password message will be deleted automatically for security

### Issue 5: Withdrawal request not showing
**Solution**:
- Ensure you have set payout information first
- Check minimum withdrawal limits
- Verify you're not banned or withdrawal-blocked

---

## Database Verification Queries
**For developers/admins with database access:**

```sql
-- Check user registration
SELECT * FROM users WHERE user_id = YOUR_USER_ID;

-- Check sold accounts
SELECT * FROM sold_accounts WHERE seller_user_id = YOUR_USER_ID;

-- Check withdrawal requests
SELECT * FROM withdrawals WHERE user_id = YOUR_USER_ID;

-- Check referral relationships
SELECT * FROM users WHERE referred_by = YOUR_USER_ID;

-- Check system settings
SELECT * FROM settings;

-- Check SaaS rates
SELECT * FROM saas_rates;
```

---

## Success Criteria Summary

### Phase 1 ✅
- [x] Bot responds to /start
- [x] User registration works
- [x] Admin authentication works
- [x] Main menu displays correctly

### Phase 2 ✅
- [x] Phone number validation works
- [x] Verification code sent successfully
- [x] **FIXED**: Users can receive and enter OTP codes
- [x] 2FA password handling works
- [x] Account processing completes
- [x] Payment credited correctly
- [x] Admin can set account price

### Phase 3 ✅
- [x] Profile displays user stats
- [x] Payout info can be set
- [x] Withdrawal requests work
- [x] Progressive limits enforced
- [x] Admin can approve/reject withdrawals
- [x] Admin can ban/unban users
- [x] Admin can control withdrawal permissions

### Phase 4 ✅
- [x] Referral links generated
- [x] Referral signup tracking works
- [x] Commission payout works
- [x] Admin can set referral rate
- [x] Support section displays
- [x] Admin reporting commands work
- [x] Daily automated reports work

### Phase 5 ✅
- [x] Buyer menu accessible
- [x] All 7 buyer buttons present
- [x] Service pricing displayed
- [x] Deposit instructions shown
- [x] Plans interfaces work
- [x] Buyer referral program shown
- [x] Reseller panel accessible
- [x] Admin account pool manager works
- [x] Manual account add/remove works
- [x] Automated account status checking works
- [x] Low pool alerts work

---

## Next Steps / Known Limitations

### Working Features ✅
- Complete Phase 1-5 seller side functionality
- Complete Phase 1-5 buyer side UI (informational)
- Referral system for both sellers and buyers
- Admin controls and reporting
- Account pool management

### Not Yet Implemented ⚠️
- **Actual service delivery** (views/reactions to channels)
- **Payment integration** for buyer deposits
- **Promo code management UI** for admins
- **Reseller approval workflow**
- **Real-time delivery monitoring**
- **Order processing automation**

These features are planned for future phases (Phase 6+).

---

## Contact & Support
For issues or questions:
- Contact bot support via the Support button
- Check logs for detailed error messages
- Report bugs to the development team
