# Shameless Graping
A lightweight minimalist scraping tool for searching my own name on Google, and opening all links in the first 2 pages. 
Since, searching for one's name is kinda shameless, hence the name is inspired from the _shameless scraping of google search results_

### Why?
1. Coz, I can. 
2. Maybe this will make Google think that my name is more important that it is, and put my search results at the top. 
3. Coz, I wanna learn web-scraping, and put it into practice.

---

### TO-DO:
- [x] find how to perfrom google search using links
- [x] find the proper HTML elements to read from the scraper
    * the div class names are random strings, so that cannot be used
    * the a links are too many, so need to filter them
    * filter strings are hardcoded right now
- [ ] convert the hardcoded program to one using itemloader
    * convert the strings to proper urls
    * have more string processing to filter out unnecessary strings
    * have a list of keywords that can describe me, and check on those
    * have a list of blacklisted keywords, which can be used for filter
- [ ] store the links in the DB (SQLite) - maybe make a design of the data to be stored
- [ ] code the actual program
- [ ] deploy in scrapinghub
- [ ] deploy in heroku
- [ ] refactor & make it more generic (planning needed)