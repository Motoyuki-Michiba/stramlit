import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image 
import time

st.title('Streamlit 超入門!')

# st.write('indication of progress bar')
# 'Start!'

# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#     latest_iteration.text(f'Iteration {i+1}')
#     bar.progress(i + 1)
#     time.sleep(0.1)
    
# 'Done!'

st.write('Interractive Widgets')

# left_column, right_column = st.beta_columns(2) 
# button = left_column.button('indicate text on right column')
# if button:
#     right_column.write('this is right column')

# expander = st.beta_expander('question')
# expander.write(' write here question')
# option = st.text_input('Please tell your hobby')

# condition = st.slider('your health condition', 0, 100, 50)
# 'your condition is', condition

# 'Your hobby is ',  option
# if st.checkbox('Show Image'):
#     img = Image.open('RedApple.jpg')
#     st.image(img, caption='Red Apple', use_column_width=True)

left_column, right_column = st.beta_columns(2)

button = left_column.button('indicate text on right column')

if button:
    right_column.write('this is right column!')
    

expander = st.beta_expander('Question!')
expander.write('write questions')
    
    
    
# text = st.text_input('Please tell me your hobby.')
# st.write('Your hobby is :', text)

# condition = st.slider('How about your codition now?', 0, 100, 50)
# 'Your condition:', condition

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.map(df)


# st.table(df.style.highlight_max(axis=1))

# """
# # 章
# ## 節
# ### 項

# ```Python
# import streamlit as st
# import numpy as np
# import pandas as pd
