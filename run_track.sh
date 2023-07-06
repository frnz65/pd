watch -c -n 300 eval "python ./scraper.py -o track.csv -m 247193010 && wc -l track.csv && python plot.py && git commit ./track.csv ./map.html -m 'updated track' && git push origin main"
