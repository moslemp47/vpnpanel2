from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["payments"])

@router.post("/stripe/checkout")
async def stripe_checkout():
    # TODO: create checkout session
    return {"url": "https://checkout.stripe.com/test"}

@router.post("/stripe/webhook")
async def stripe_webhook():
    # TODO: verify and handle events
    return {"ok": True}

@router.post("/paypal/webhook")
async def paypal_webhook():
    return {"ok": True}

@router.post("/zarinpal/callback")
async def zarinpal_callback(Authority: str, Status: str):
    # TODO: verify with ZarinPal API
    return {"Authority": Authority, "Status": Status}

@router.post("/nextpay/callback")
async def nextpay_callback():
    return {"ok": True}

@router.post("/crypto/webhook")
async def crypto_webhook():
    return {"ok": True}
