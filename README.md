# rental_analysis_switzerland_immoscout24
The goal of this project is to analyze and build a supervised learning model to predict the apartment rental prices in switzerland. We start the analysis by a particular city (Lausanne). Here is what each script does:

immoscoutHtml_to_text_once script is run once at the beginning to download all pages of rental apartments listed on immoscout24 (Lausanne)

ImmoscoutHtml_to_csv.py runs every day or week (as frequent as you want) to add the new listings to the existing data

html2text.py is written by Aaron Swartz; it converts an Html page to a plain text

SingleAprtListing_to_table.py is used in the above two scripts; its job is to convert a single apartment listing to a pandas dataframe

rental_analysis_lausanne.ipynb is a jupyter notebook to study, analyse and predict the rental prices based on the datas collected by the scripts listed above

[Here](https://hamedrazavi.github.io/rental_analysis.html) I have explained the process in more details. 