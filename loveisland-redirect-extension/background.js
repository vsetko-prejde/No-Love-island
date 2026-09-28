const REDIRECT_URL = "https://www.upsvr.gov.sk/ke.html?page_id=232158";
const MATCH_PATTERN = /love[\s_-]*island/i;

function containsMatch(url) {
  return decodeURIComponent(url).match(MATCH_PATTERN) !== null;
}

chrome.webNavigation.onBeforeNavigate.addListener((details) => {
  if (details.frameId !== 0 || containsMatch(details.url) === false) {
    return;
  }

  chrome.tabs.update(details.tabId, { url: REDIRECT_URL });
}, {
  url: [{ schemes: ["http", "https"] }]
});
