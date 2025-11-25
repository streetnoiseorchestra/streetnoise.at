# SNO's wagtail based cms

Live at `https://streetnoise.at`

Built using [Wagtail](https://wagtail.org/).

Licensed under GNU Affero General Public License v3.0 or later

(C) 2019-2025 Casey Link

### Dev Notes

``` sh
docker compose -f docker-compose.dev.yml up -d
DB_DUMP=path/to/latest/db.dump make dev-reset
make serve
make dev-makemigrations
make dev-migrate
make watch
# write code
# if you changed above the fold css, see below
make freeze # if you updated python deps
# commit code
# push
```

After changing css you need to regenerate the above-the-fold critical css.

1. Open `home/templates/home/header_assets.html` and `festival2023/templates/festival2023/homepage.html`
2. Comment out the compressed preloaded + critical css
3. Uncomment the bare css
4. Run the server
5. Run `node acclaimed.js`
6. Swap the comments again
