#!/bin/bash



for i in {40..40}
do
   id_user=$(sed "${i}q;d" lista)
   echo $id_user $i
   ./final.sh $id_user $i
done
