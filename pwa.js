/* PERANG DEDEMIT install support. Loaded by index.html and mobile.html. On a phone the menu runs inside mobile.html's
   iframe, but the browser offers installation to the top page, so the top page keeps the offer in
   window.__dedemitInstall and announces changes with a 'dedemit-installable' event; menu.js reads it from there. */
(() => {
  'use strict';
  if (window.top !== window) return;
  window.addEventListener('beforeinstallprompt', e => { e.preventDefault(); window.__dedemitInstall = e; window.dispatchEvent(new Event('dedemit-installable')); });
  window.addEventListener('appinstalled', () => { window.__dedemitInstall = null; window.__dedemitInstalled = true; window.dispatchEvent(new Event('dedemit-installable')); });
})();
