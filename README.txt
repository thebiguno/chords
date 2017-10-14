These songs are arranged to fit in a half size binder (5.5x8.5") when printed in
duplex mode.

The margins and page size on the .odt files are designed to handle the hole punching process.

To print these, do the following steps:
1) Batch convert to PDF (you may need absolute path to soffice):
			soffice --headless --convert-to pdf *.odt
2) (Optional, for printing) Convert to booklet format (be sure to have "paper='letterpaper'" in ~/.pdfjam.conf file):
			ls *.pdf | grep -v 'book.pdf' | while read X; do pdfbook --short-edge "$X"; done
3) Merge the resulting PDFs into a single one:
			ls *.pdf | tr '\n' '\0' | xargs -0 gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=output.pdf
4) Print resulting .pdf in duplex with short edge mode.
5) Cut the paper exactly in half (on the 14cm mark)
6) Punch holes for the half size binder
