# Tyler Mattson
#
# Varubles used:
#  max_strg        Max Storage 
#  used_strg       Used Storage 
#  avail_strg      Avaliable Storage 
#  vidPer_wk       Videos Per Week 
#  avgVid_siz      Average Video Size
#  localVid_siz    Local Video Size
#  wk_lft          Number of weeks left
#  days_reman      Days Remaining
#  newDays_reman   Days remaining after new production
#  new_prod        Amount of space new videos use
#  new_wk          The totak amount of space used per week
############################################################################
vidPer_wk = (float(input("Enter videos produced per week")))
avgVid_siz = (float(input("Enter size of video")))
used_strg = (float(input("Enter available storage")))

#NAS Storage 
max_strg = 8 
used_strg = 1.4 
avail_strg = max_strg - used_strg
max_strgGB = avail_strg * 1000

#Video Storage (previous production)
localVid_siz = avgVid_siz * vidPer_wk


#New Production
new_prod = avgVid_siz * 3
new_Wk = vidPer_wk * new_prod 


#Old Production
wk_lft = max_strgGB / localVid_siz
days_reman = wk_lft * 7 


# new
newWk_lft = max_strgGB / new_Wk 
newDays_reman = newWk_lft * 7 

 
print(f"Avaliable storage is {max_strgGB}GB") 
print ()
print ("Number of days left with current video production" ,days_reman)
print ()
print (f"Total number of days left after video production increase {newDays_reman:1.1f}")
