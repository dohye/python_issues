import pandas as pd

# pandas에서 stack쌓을 때 concat이용 -> 아래는 4개의 데이터 프레임을 아래로 붙인것

sorted_pd = pd.concat([pd.DataFrame(dh_sorted_chars), pd.DataFrame(dh_sorted_values), pd.DataFrame(hs_sorted_chars),pd.DataFrame(hs_sorted_values)], axis=0)
#sorted_pd.to_excel('./logit_saved/change_lr_'+num_saved+'_chars.xlsx')
