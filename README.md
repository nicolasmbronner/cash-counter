# Cash Counter

Comptage de caisse pour smartphone (PWA installable, fonctionne hors ligne).
Les comptages restent dans le téléphone (localStorage), rien n'est envoyé.

- Site : https://nicolasmbronner.github.io/cash-counter/
- Fichiers : `index.html` (app complète), `manifest.webmanifest`, `sw.js` (cache hors ligne), icônes PNG. Aucune dépendance.
- Mise à jour : après toute modification, incrémenter `VERSION` dans `sw.js`, sinon le téléphone garde l'ancienne version en cache.
- Icônes : `python icons.py` (Pillow) les régénère.
- Test local : `python -m http.server` puis http://localhost:8000/ (le service worker exige http://localhost ou https).
