while read line; do
	filename=$( echo ${line:14} | tr / _);
	curl --url $line  --output $filename ;
done < q2021-01.txt
