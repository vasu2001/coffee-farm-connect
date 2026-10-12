FARMS = [
    {
        "id": "yirg-01", "name": "Kochere Highlands", "country": "Ethiopia",
        "region": "Yirgacheffe", "lat": 6.16, "lng": 38.20, "elevation": 2100,
        "farmer": "Abebe Bekele", "size_ha": 12, "contact": "abebe@kochere.et",
        "listings": [
            {"variety": "Heirloom", "process": "Washed", "roast": "Light",
             "flavors": ["jasmine", "bergamot", "lemon"], "score": 88.5,
             "price_usd_lb": 6.80, "lots_60kg": 40, "harvest": "Nov 2025"},
            {"variety": "Heirloom", "process": "Natural", "roast": "Light",
             "flavors": ["blueberry", "floral", "honey"], "score": 87.0,
             "price_usd_lb": 7.20, "lots_60kg": 22, "harvest": "Dec 2025"},
        ],
    },
    {
        "id": "huila-02", "name": "Finca El Mirador", "country": "Colombia",
        "region": "Huila", "lat": 2.53, "lng": -75.52, "elevation": 1750,
        "farmer": "Lucía Ramírez", "size_ha": 8, "contact": "lucia@elmirador.co",
        "listings": [
            {"variety": "Caturra", "process": "Washed", "roast": "Medium",
             "flavors": ["caramel", "red apple", "panela"], "score": 86.0,
             "price_usd_lb": 4.90, "lots_60kg": 60, "harvest": "Oct 2025"},
            {"variety": "Pink Bourbon", "process": "Honey", "roast": "Light",
             "flavors": ["peach", "hibiscus", "brown sugar"], "score": 89.5,
             "price_usd_lb": 9.40, "lots_60kg": 12, "harvest": "Nov 2025"},
        ],
    },
    {
        "id": "cerrado-03", "name": "Fazenda Santa Clara", "country": "Brazil",
        "region": "Cerrado Mineiro", "lat": -18.95, "lng": -46.99, "elevation": 1100,
        "farmer": "João Prado", "size_ha": 140, "contact": "joao@santaclara.br",
        "listings": [
            {"variety": "Yellow Bourbon", "process": "Pulped Natural", "roast": "Medium",
             "flavors": ["chocolate", "hazelnut", "molasses"], "score": 84.5,
             "price_usd_lb": 3.60, "lots_60kg": 300, "harvest": "Jul 2025"},
            {"variety": "Mundo Novo", "process": "Natural", "roast": "Dark",
             "flavors": ["cocoa", "toasted almond", "spice"], "score": 83.0,
             "price_usd_lb": 3.10, "lots_60kg": 420, "harvest": "Aug 2025"},
        ],
    },
    {
        "id": "nyeri-04", "name": "Gatomboya Cooperative", "country": "Kenya",
        "region": "Nyeri", "lat": -0.42, "lng": 36.95, "elevation": 1850,
        "farmer": "Wanjiku Mwangi", "size_ha": 30, "contact": "coop@gatomboya.ke",
        "listings": [
            {"variety": "SL28", "process": "Washed", "roast": "Light",
             "flavors": ["blackcurrant", "tomato", "grapefruit"], "score": 90.0,
             "price_usd_lb": 8.90, "lots_60kg": 18, "harvest": "Jan 2026"},
        ],
    },
    {
        "id": "antigua-05", "name": "Finca La Ceiba", "country": "Guatemala",
        "region": "Antigua", "lat": 14.56, "lng": -90.73, "elevation": 1600,
        "farmer": "Miguel Estrada", "size_ha": 22, "contact": "miguel@laceiba.gt",
        "listings": [
            {"variety": "Bourbon", "process": "Washed", "roast": "Medium",
             "flavors": ["milk chocolate", "orange", "almond"], "score": 85.5,
             "price_usd_lb": 4.40, "lots_60kg": 80, "harvest": "Feb 2026"},
            {"variety": "Geisha", "process": "Washed", "roast": "Light",
             "flavors": ["jasmine", "papaya", "honeysuckle"], "score": 91.5,
             "price_usd_lb": 18.00, "lots_60kg": 4, "harvest": "Feb 2026"},
        ],
    },
    {
        "id": "gayo-06", "name": "Gayo Mountain Estate", "country": "Indonesia",
        "region": "Aceh, Sumatra", "lat": 4.63, "lng": 96.84, "elevation": 1400,
        "farmer": "Rizki Siregar", "size_ha": 45, "contact": "rizki@gayomtn.id",
        "listings": [
            {"variety": "Typica", "process": "Wet Hulled", "roast": "Dark",
             "flavors": ["earthy", "cedar", "dark chocolate"], "score": 84.0,
             "price_usd_lb": 3.90, "lots_60kg": 150, "harvest": "Jun 2025"},
        ],
    },
    {
        "id": "boquete-07", "name": "Hacienda Río Cristal", "country": "Panama",
        "region": "Boquete", "lat": 8.78, "lng": -82.44, "elevation": 1700,
        "farmer": "Elena Vargas", "size_ha": 15, "contact": "elena@riocristal.pa",
        "listings": [
            {"variety": "Geisha", "process": "Natural", "roast": "Light",
             "flavors": ["strawberry", "rose", "tropical fruit"], "score": 93.0,
             "price_usd_lb": 42.00, "lots_60kg": 2, "harvest": "Mar 2026"},
            {"variety": "Catuai", "process": "Washed", "roast": "Medium",
             "flavors": ["nougat", "plum", "cane sugar"], "score": 86.5,
             "price_usd_lb": 5.20, "lots_60kg": 35, "harvest": "Mar 2026"},
        ],
    },
    {
        "id": "tarrazu-08", "name": "Cafetal Monteverde", "country": "Costa Rica",
        "region": "Tarrazú", "lat": 9.65, "lng": -84.02, "elevation": 1900,
        "farmer": "Carlos Solano", "size_ha": 10, "contact": "carlos@monteverde.cr",
        "listings": [
            {"variety": "Villa Sarchi", "process": "Honey", "roast": "Medium",
             "flavors": ["honey", "apricot", "vanilla"], "score": 87.5,
             "price_usd_lb": 6.10, "lots_60kg": 25, "harvest": "Jan 2026"},
        ],
    },
]


def main(roast: str = "", process: str = "", flavor: str = "",
         country: str = "", min_score: float = 0.0, max_price: float = 0.0):
    farms = []
    for farm in FARMS:
        listings = farm["listings"]
        if roast:
            listings = [l for l in listings if l["roast"] == roast]
        if process:
            listings = [l for l in listings if l["process"] == process]
        if flavor:
            f = flavor.lower()
            listings = [l for l in listings if any(f in fl for fl in l["flavors"])]
        if country:
            if farm["country"] != country:
                listings = []
        if min_score:
            listings = [l for l in listings if l["score"] >= min_score]
        if max_price:
            listings = [l for l in listings if l["price_usd_lb"] <= max_price]
        if listings:
            farms.append({**farm, "listings": listings})

    all_farms = FARMS
    return {
        "farms": farms,
        "total_farms": len(all_farms),
        "total_listings": sum(len(f["listings"]) for f in farms),
        "countries": sorted({f["country"] for f in all_farms}),
        "roasts": sorted({l["roast"] for f in all_farms for l in f["listings"]}),
        "processes": sorted({l["process"] for f in all_farms for l in f["listings"]}),
    }
