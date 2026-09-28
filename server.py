from flask import Flask, render_template_string

app = Flask(__name__)

# Enterprise Financial Config 
FINANCIAL_CONFIG = {
    "paypal_url": "https://paypal.me",
    "vodafone_cash": "01000111438",
    "merchant_name": "S**** M******"
}

# Fully English High-Converting UI Optimized for Global Revenue
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hala AI Gate | Cosmic Behavioral Decoder</title>
    <style>
        body { background-color: #0B192C; color: #FFFFFF; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; padding: 20px; direction: ltr; }
        .container { max-width: 600px; margin: auto; background: #15304b; padding: 30px; border-radius: 15px; border: 2px solid #E1B057; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
        h1 { color: #E1B057; font-size: 28px; }
        .btn { background-color: #4A148C; color: white; padding: 12px 25px; border: none; border-radius: 8px; cursor: pointer; text-decoration: none; display: inline-block; margin: 10px; font-weight: bold; font-size: 16px; transition: 0.3s; }
        .btn:hover { background-color: #6a1b9a; transform: scale(1.05); }
        .btn-viral { background-color: #25D366; }
        .btn-viral:hover { background-color: #1ebd58; }
        .payment-box { margin-top: 25px; padding: 15px; background: #0B192C; border-radius: 8px; border: 1px dashed #E1B057; display: none; }
        .viral-box { background: #1e466e; padding: 20px; border-radius: 10px; margin-top: 20px; border: 1px solid #4A148C; }
        .counter { font-size: 20px; color: #E1B057; font-weight: bold; margin: 10px 0; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌌 Hala AI Gate</h1>
        <p>The universe doesn't work randomly... and neither do you. Your evolutionary cosmic code and behavioral critical blindspots are 100% calculated.</p>
        
        <!-- Automated Viral Lock System -->
        <div id="viralSection" class="viral-box">
            <h3 style="color:#E1B057;">🔓 Free Unlock Protocol:</h3>
            <p>To view your results and download your full strategic PDF blueprint, share this portal link with 3 friends or groups on WhatsApp / Instagram Stories:</p>
            <div class="counter">Remaining Shares: <span id="shareCount">3</span></div>
            <button onclick="triggerViralShare()" class="btn btn-viral">📢 Share Now on WhatsApp / Instagram</button>
        </div>

        <!-- Hidden Monetization Box -->
        <div id="paymentSection" class="payment-box">
            <h3 style="color: #25D366;">✅ Portal Unlocked Successfully!</h3>
            <p>Your Core Leadership Energy Index for this cycle: <strong>92%</strong></p>
            <hr style="border: 0.5px solid #E1B057;">
            <p>To unlock the deep analytical year-round PDF report and mitigation matrix:</p>
            <a href="{{ config.paypal_url }}" target="_blank" class="btn">💳 Instant Global Checkout | Visa & Mastercard (\$4.99)</a>
            <p style="font-size: 14px; color: #b0c4de; margin-top: 15px;">Local Mobile Wallet Option (Egypt Region Only): Send to <strong>{{ config.vodafone_cash }}</strong></p>
        </div>
    </div>

    <script>
        let sharesLeft = 3;
        const currentUrl = encodeURIComponent(window.location.href);
        const shareText = encodeURIComponent("🌌 Incredible! I just decoded my cosmic behavioral code and discovered my critical life blindspots for free with Professor Hala's AI. Try it now and see your percentage: ");

        function triggerViralShare() {
            const whatsappUrl = `https://whatsapp.com{shareText}${currentUrl}`;
            window.open(whatsappUrl, '_blank');
            
            if (sharesLeft > 1) {
                sharesLeft--;
                document.getElementById('shareCount').innerText = sharesLeft;
            } else {
                document.getElementById('viralSection').style.display = 'none';
                document.getElementById('paymentSection').style.display = 'block';
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, config=FINANCIAL_CONFIG)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
