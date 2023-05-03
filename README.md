# SNO's wagtail based cms


### Dev Notes

After changing css you need to regenerate the above-the-fold critical css.

1. Open `home/templates/home/header_assets.html` and `festival2023/templates/festival2023/homepage.html`
2. Comment out the compressed preloaded + critical css
3. Uncomment the bare css
4. Run the server
5. Run `node acclaimed.js`
6. Swap the comments again
