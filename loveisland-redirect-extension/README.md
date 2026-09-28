# LoveIsland URL Redirect

This Chrome/Edge extension redirects any top-level HTTP or HTTPS URL containing `LoveIsland` (case-insensitive) to:

`https://www.upsvr.gov.sk/ke.html?page_id=232158`

## Install in Chrome or Edge

1. Open `chrome://extensions` in Chrome, or `edge://extensions` in Edge.
2. Go to `manage extensions`
3. Turn on **Developer mode**.
4. Select **Load unpacked**.
5. Choose this `loveisland-redirect-extension` folder.
6. Open or refresh a URL containing `LoveIsland` to test it.

The extension runs locally and does not send browsing data anywhere.

If there is a problem with selecting correct file just select the next in the whole folder, that should fix it

## Run as a Python script

Python is not required for the browser extension, but you can run the standalone
redirect script with the Python launcher on Windows:

```powershell
py redirect_url.py "https://www.youtube.com/c/LoveIsland%C4CeskoSlovensko"
```

Any URL containing `LoveIsland` is opened at the redirect destination. Other
HTTP and HTTPS URLs are opened unchanged.

This script only processes URLs passed to it. Automatically intercepting every
URL opened by Chrome requires the extension above or browser proxy integration.
