# Coffee Farm Connect

A fused-render app that maps coffee farms across the growing belt and lets buyers send an inquiry straight to a farm.

Open `index.html` in fused-render. The page draws an offline Leaflet map (vendored in `vendor/`, basemap from `world.geo.json`), lists farms from `farms.py` with filters that live in the URL, and offers an optional 3D view with markers extruded by elevation. Selecting a farm shows its listings and an inquiry form; submitting runs `inquire.py`, which appends the request to `inquiries.json` beside the app.
