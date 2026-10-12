def main(farm_id: str = "", farm_name: str = "", variety: str = "",
         buyer_name: str = "", buyer_email: str = "", quantity: str = "",
         message: str = ""):
    import json, os, datetime

    if not farm_id or not buyer_name or not buyer_email:
        return {"ok": False, "error": "farm_id, buyer_name and buyer_email are required"}

    path = "./inquiries.json"
    inquiries = []
    if os.path.exists(path):
        with open(path) as f:
            inquiries = json.load(f)

    inquiries.append({
        "ts": datetime.datetime.now().isoformat(timespec="seconds"),
        "farm_id": farm_id,
        "farm_name": farm_name,
        "variety": variety,
        "buyer_name": buyer_name,
        "buyer_email": buyer_email,
        "quantity": quantity,
        "message": message,
    })
    with open(path, "w") as f:
        json.dump(inquiries, f, indent=2)

    return {"ok": True, "count": len(inquiries)}
