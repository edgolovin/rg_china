while read line; do
	filename=$( echo ${line:14} | tr / _);
	echo $filename;
	curl -s --url $line  --output $filename ;
done < all_urls_before_2019.txt
