#!/usr/bin/env python
# coding: utf-8

# # Emotion Detection using DeepFace 

# ### Packages

# In[22]:


from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt


# ### Loading and Displaying Input Image 

# In[29]:


img1 = cv2.imread('Image.jpg')
plt.show()
plt.imshow(img1[:,:,::-1])



# ### Deep Image Analysis 

# In[30]:


result = DeepFace.analyze(img1, actions = ['emotion'])


# ### Formed Final Result

# In[31]:


print(result)


# In[ ]: