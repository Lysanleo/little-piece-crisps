// ==UserScript==
// @name         Copy tex in zhihu and wikipedia
// @homepageURL  https://github.com/Lysanleo/little-piece-crisps
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       Lysanleo
// @match        *://*.wikipedia.org/*
// @match        *://*.wikipedia.org/*
// @match        *://*.zhihu.com/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=wikipedia.org
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    function getAttributeName(url) {
        if (url.includes('wikipedia.org')) {
            return 'alt';
        } else if (url.includes('zhihu.com')) {
            return 'data-tex';
        }
        // Add more conditions for other websites here
    }

    function addDoubleClickHandler() {
        const attribute = getAttributeName(window.location.href);
        if (!attribute) return;

        document.querySelectorAll(`[${attribute}]`).forEach(e => e.ondblclick = () => navigator.clipboard.writeText(e.getAttribute(attribute)));
    }

    // Add event listener for when the page is loaded or changed
    document.addEventListener('DOMContentLoaded', addDoubleClickHandler);
    new MutationObserver(addDoubleClickHandler).observe(document.documentElement, {childList: true, subtree: true});
})();
