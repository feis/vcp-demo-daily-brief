from pathlib import Path
s = Path('preview.log').read_text(encoding='utf-8')
assert '虛構學校：抓到 3 則' in s
assert '檢索：3 則挑出 2 則' in s
assert '原文 → https://raw.githubusercontent.com/feis/vcp-demo-daily-brief/main/fixtures/news/consent.html' in s
assert '原文 → https://raw.githubusercontent.com/feis/vcp-demo-daily-brief/main/fixtures/news/lunch.html' in s
assert '沒有設定氣象署授權碼' in s
assert '沒有設定 DISCORD_WEBHOOK_URL：只印出、不送出、不記錄' in s
assert not Path('送過的.json').exists()
print('7/7：公開虛構來源、關鍵詞篩選與無發送預覽通過')
