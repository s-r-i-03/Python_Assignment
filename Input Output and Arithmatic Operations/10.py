population= 80000
men= population *52/100
women=(population-men)
total_literacy= population * 48/100
literate_men= population*35/100
illiterate_men=(men-literate_men)
literate_women=(total_literacy-literate_men)
illiterate_women=(women-literate_women)
print("total no of illiterate men is",illiterate_men)
print("total no of illiterate women is",illiterate_women)
