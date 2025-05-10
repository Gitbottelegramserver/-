import requests
from config import API_URL, API_KEY, USDT_WALLET_ADDRESS, BANK_ACCOUNT_DETAILS

def create_payment_link(user_id, method):
    if method == "usdt":
        return f"Для оплаты в USDT переведите на адрес: {USDT_WALLET_ADDRESS}"
    elif method == "bank":
        return f"Для банковского перевода: {BANK_ACCOUNT_DETAILS}"
    else:
        r = requests.post(f"{API_URL}/create_payment", json={"user_id": user_id, "amount": 100},
                          headers={"Authorization": f"Bearer {API_KEY}"})
        return r.json().get("payment_link") if r.status_code == 200 else None

def check_payment(user_id):
    r = requests.get(f"{API_URL}/check_payment", params={"user_id": user_id},
                     headers={"Authorization": f"Bearer {API_KEY}"})
    return r.status_code == 200 and r.json().get("status") == "success"
